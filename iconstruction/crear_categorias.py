import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'iconstruction.settings')
django.setup()

from appiconstruction.models import CategoriaMaterial, CategoriaHerramienta

def crear_categorias():
    print("=== CREANDO CATEGORÍAS ===")
    
    # Categorías de Materiales
    categorias_material = [
        {'nombre': 'Materiales Básicos', 'descripcion': 'Materiales fundamentales para construcción'},
        {'nombre': 'Acabados', 'descripcion': 'Materiales para acabados y terminaciones'},
        {'nombre': 'Estructuras', 'descripcion': 'Materiales estructurales y de soporte'},
        {'nombre': 'Fontanería', 'descripcion': 'Materiales para instalaciones sanitarias'},
        {'nombre': 'Electricidad', 'descripcion': 'Materiales eléctricos y de iluminación'},
        {'nombre': 'Pinturas y Barnices', 'descripcion': 'Pinturas, barnices y productos relacionados'},
        {'nombre': 'Madera y Derivados', 'descripcion': 'Maderas, aglomerados y derivados'},
        {'nombre': 'Metales', 'descripcion': 'Perfiles, tubos y accesorios metálicos'},
        {'nombre': 'Vidrios y Cerámicos', 'descripcion': 'Vidrios, cerámicos y porcelanatos'}
    ]
    
    print("\n📦 Categorías de Material:")
    for cat_data in categorias_material:
        cat, created = CategoriaMaterial.objects.get_or_create(
            nombre=cat_data['nombre'],
            defaults=cat_data
        )
        if created:
            print(f"   ✅ Creada: {cat.nombre}")
        else:
            print(f"   ℹ️ Ya existe: {cat.nombre}")
    
    # Categorías de Herramientas
    categorias_herramienta = [
        {'nombre': 'Herramientas Manuales', 'descripcion': 'Herramientas de uso manual básico'},
        {'nombre': 'Equipos Eléctricos', 'descripcion': 'Herramientas y equipos eléctricos'},
        {'nombre': 'Equipos de Medición', 'descripcion': 'Instrumentos de medición y nivelación'},
        {'nombre': 'Equipos de Seguridad', 'descripcion': 'Equipos de protección personal'},
        {'nombre': 'Maquinaria Pesada', 'descripcion': 'Maquinaria y equipos pesados'},
        {'nombre': 'Herramientas de Corte', 'descripcion': 'Herramientas especializadas para corte'},
        {'nombre': 'Equipos de Soldadura', 'descripcion': 'Equipos para soldadura y unión'},
        {'nombre': 'Andamios y Escaleras', 'descripcion': 'Andamios, escaleras y accesorios'},
        {'nombre': 'Herramientas de Sujeción', 'descripcion': 'Herramientas para sujeción y fijación'}
    ]
    
    print("\n🔧 Categorías de Herramienta:")
    for cat_data in categorias_herramienta:
        cat, created = CategoriaHerramienta.objects.get_or_create(
            nombre=cat_data['nombre'],
            defaults=cat_data
        )
        if created:
            print(f"   ✅ Creada: {cat.nombre}")
        else:
            print(f"   ℹ️ Ya existe: {cat.nombre}")
    
    # Resumen
    print(f"\n📊 RESUMEN:")
    print(f"   Materiales: {CategoriaMaterial.objects.count()} categorías")
    print(f"   Herramientas: {CategoriaHerramienta.objects.count()} categorías")
    print("🎉 ¡Categorías listas para usar!")

if __name__ == '__main__':
    crear_categorias()