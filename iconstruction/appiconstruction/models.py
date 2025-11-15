from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse

# Modelo principal para gestionar bodegas
class Bodega(models.Model):
    nombre = models.CharField(max_length=100)        # Nombre identificador
    ubicacion = models.CharField(max_length=200)     # Dirección o punto físico
    responsable = models.ForeignKey(User, on_delete=models.CASCADE)  # Usuario encargado
    telefono = models.CharField(max_length=15, blank=True)
    activa = models.BooleanField(default=True)       # Control simple de activación
    
    class Meta:
        verbose_name = "Bodega"
        verbose_name_plural = "Bodegas"
    
    def __str__(self):
        return self.nombre
    
    def get_absolute_url(self):
        return reverse('detalle_bodega', kwargs={'pk': self.pk})


# Categorías para agrupar materiales
class CategoriaMaterial(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)

    def __str__(self):
        return self.nombre


# Modelo para materiales dentro de bodegas
class Material(models.Model):
    UNIDADES = [
        ('unidad', 'Unidad'),
        ('kg', 'Kilogramo'),
        ('m', 'Metro'),
        ('m2', 'Metro cuadrado'),
        ('m3', 'Metro cúbico'),
        ('l', 'Litro'),
    ]
    
    codigo = models.CharField(max_length=50, unique=True)     # Código único
    nombre = models.CharField(max_length=200)
    categoria = models.ForeignKey(CategoriaMaterial, on_delete=models.CASCADE)
    unidad_medida = models.CharField(max_length=10, choices=UNIDADES)
    stock_minimo = models.IntegerField(default=0)             # Nivel mínimo permitido
    stock_actual = models.IntegerField(default=0)
    bodega = models.ForeignKey(Bodega, on_delete=models.CASCADE)
    fecha_vencimiento = models.DateField(null=True, blank=True)
    activo = models.BooleanField(default=True)
    
    class Meta:
        verbose_name_plural = "Materiales"
    
    def __str__(self):
        return f"{self.codigo} - {self.nombre}"
    
    def get_absolute_url(self):
        return reverse('lista_materiales')
    
    @property
    def estado_stock(self):
        # Devuelve un estado simple según stock actual
        if self.stock_actual <= 0:
            return 'agotado'
        elif self.stock_actual < self.stock_minimo:
            return 'bajo'
        return 'normal'


# Categorías para herramientas
class CategoriaHerramienta(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField(blank=True)
    
    def __str__(self):
        return self.nombre


# Herramientas dentro del sistema
class Herramienta(models.Model):
    ESTADOS = [
        ('disponible', 'Disponible'),
        ('prestada', 'Prestada'),
        ('mantencion', 'En Mantención'),
        ('danada', 'Dañada'),
    ]
    
    codigo = models.CharField(max_length=50, unique=True)
    nombre = models.CharField(max_length=200)
    categoria = models.ForeignKey(CategoriaHerramienta, on_delete=models.CASCADE)
    estado = models.CharField(max_length=20, choices=ESTADOS, default='disponible')
    bodega = models.ForeignKey(Bodega, on_delete=models.CASCADE)
    fecha_adquisicion = models.DateField()
    vida_util = models.IntegerField(help_text="Meses de vida útil")  # Tiempo estimado
    activa = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.codigo} - {self.nombre}"
    
    def get_absolute_url(self):
        return reverse('lista_herramientas')


# Gestión de proyectos
class Proyecto(models.Model):
    ESTADOS_PROYECTO = [
        ('planificacion', 'Planificación'),
        ('en_curso', 'En Curso'),
        ('suspendido', 'Suspendido'),
        ('completado', 'Completado'),
    ]
    
    codigo = models.CharField(max_length=50, unique=True)
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_inicio = models.DateField()
    fecha_termino_planificada = models.DateField()
    fecha_termino_real = models.DateField(null=True, blank=True)
    estado = models.CharField(max_length=20, choices=ESTADOS_PROYECTO, default='planificacion')
    supervisor = models.ForeignKey(User, on_delete=models.CASCADE, related_name='proyectos_supervisados')
    
    def __str__(self):
        return f"{self.codigo} - {self.nombre}"
    
    def get_absolute_url(self):
        return reverse('lista_proyectos')


# Actividades asociadas a proyectos
class Actividad(models.Model):
    ESTADOS_ACTIVIDAD = [
        ('pendiente', 'Pendiente'),
        ('en_progreso', 'En Progreso'),
        ('completada', 'Completada'),
        ('atrasada', 'Atrasada'),
    ]
    
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    fecha_inicio_planificada = models.DateField()
    fecha_termino_planificada = models.DateField()
    fecha_inicio_real = models.DateField(null=True, blank=True)
    fecha_termino_real = models.DateField(null=True, blank=True)
    porcentaje_avance = models.IntegerField(default=0)
    estado = models.CharField(max_length=20, choices=ESTADOS_ACTIVIDAD, default='pendiente')
    
    class Meta:
        verbose_name_plural = "Actividades"
    
    def __str__(self):
        return f"{self.proyecto.codigo} - {self.nombre}"


# Movimientos de material (entrada, salida o ajustes)
class MovimientoMaterial(models.Model):
    TIPOS_MOVIMIENTO = [
        ('entrada', 'Entrada'),
        ('salida', 'Salida'),
        ('ajuste', 'Ajuste'),
    ]
    
    material = models.ForeignKey(Material, on_delete=models.CASCADE)
    tipo = models.CharField(max_length=10, choices=TIPOS_MOVIMIENTO)
    cantidad = models.IntegerField()
    bodega = models.ForeignKey(Bodega, on_delete=models.CASCADE)
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE, null=True, blank=True)
    responsable = models.ForeignKey(User, on_delete=models.CASCADE)
    fecha = models.DateTimeField(auto_now_add=True)        # Fecha automática
    observaciones = models.TextField(blank=True)
    
    def __str__(self):
        return f"{self.tipo} - {self.material.nombre}"


# Préstamos de herramientas
class PrestamoHerramienta(models.Model):
    herramienta = models.ForeignKey(Herramienta, on_delete=models.CASCADE)
    obrero = models.ForeignKey(User, on_delete=models.CASCADE)
    proyecto = models.ForeignKey(Proyecto, on_delete=models.CASCADE)
    fecha_prestamo = models.DateTimeField(auto_now_add=True)
    fecha_devolucion_estimada = models.DateField()
    fecha_devolucion_real = models.DateTimeField(null=True, blank=True)
    estado_devolucion = models.CharField(max_length=100, blank=True)
    observaciones = models.TextField(blank=True)
    
    def __str__(self):
        return f"Préstamo: {self.herramienta.nombre} - {self.obrero.username}"
