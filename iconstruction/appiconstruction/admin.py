from django.contrib import admin
from .models import *

# Administración de bodegas en el panel
@admin.register(Bodega)
class BodegaAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'ubicacion', 'responsable', 'activa']
    list_filter = ['activa']
    search_fields = ['nombre', 'ubicacion']

# Administración de materiales
@admin.register(Material)
class MaterialAdmin(admin.ModelAdmin):
    list_display = ['codigo', 'nombre', 'categoria', 'stock_actual', 'stock_minimo', 'bodega']
    list_filter = ['categoria', 'bodega', 'activo']
    search_fields = ['codigo', 'nombre']

# Administración de herramientas
@admin.register(Herramienta)
class HerramientaAdmin(admin.ModelAdmin):
    list_display = ['codigo', 'nombre', 'categoria', 'estado', 'bodega']
    list_filter = ['categoria', 'estado', 'bodega']
    search_fields = ['codigo', 'nombre']

# Administración de proyectos
@admin.register(Proyecto)
class ProyectoAdmin(admin.ModelAdmin):
    list_display = ['codigo', 'nombre', 'estado', 'fecha_inicio', 'fecha_termino_planificada']
    list_filter = ['estado']
    search_fields = ['codigo', 'nombre']

# Administración de actividades dentro de proyectos
@admin.register(Actividad)
class ActividadAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'proyecto', 'estado', 'porcentaje_avance']
    list_filter = ['estado', 'proyecto']
    search_fields = ['nombre', 'proyecto__nombre']

# Registros simples sin configuración extra
admin.site.register(CategoriaMaterial)
admin.site.register(CategoriaHerramienta)
