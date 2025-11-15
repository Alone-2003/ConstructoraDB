from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    # Dashboard y autenticación
    path('', views.dashboard, name='dashboard'),
    path('login/', auth_views.LoginView.as_view(template_name='appiconstruction/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='logout'),
    
    # MATERIALES - URLs completas
    path('materiales/', views.lista_materiales, name='lista_materiales'),
    path('materiales/agregar/', views.agregar_material, name='agregar_material'),
    path('materiales/editar/<int:pk>/', views.editar_material, name='editar_material'),
    path('materiales/eliminar/<int:pk>/', views.eliminar_material, name='eliminar_material'),
    
    # HERRAMIENTAS - URLs completas
    path('herramientas/', views.lista_herramientas, name='lista_herramientas'),
    path('herramientas/agregar/', views.agregar_herramienta, name='agregar_herramienta'),
    path('herramientas/editar/<int:pk>/', views.editar_herramienta, name='editar_herramienta'),
    path('herramientas/eliminar/<int:pk>/', views.eliminar_herramienta, name='eliminar_herramienta'),
    
    # BODEGAS - URLs completas
    path('bodegas/', views.lista_bodegas, name='lista_bodegas'),
    path('bodegas/agregar/', views.agregar_bodega, name='agregar_bodega'),
    path('bodegas/editar/<int:pk>/', views.editar_bodega, name='editar_bodega'),
    path('bodegas/eliminar/<int:pk>/', views.eliminar_bodega, name='eliminar_bodega'),
    path('bodegas/<int:pk>/', views.detalle_bodega, name='detalle_bodega'),
    
    # PROYECTOS - URLs completas
    path('proyectos/', views.lista_proyectos, name='lista_proyectos'),
    path('proyectos/agregar/', views.agregar_proyecto, name='agregar_proyecto'),
    path('proyectos/editar/<int:pk>/', views.editar_proyecto, name='editar_proyecto'),
    path('proyectos/eliminar/<int:pk>/', views.eliminar_proyecto, name='eliminar_proyecto'),
]