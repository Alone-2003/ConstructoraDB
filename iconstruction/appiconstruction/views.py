from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from .models import *
from .forms import *

# ==================== DASHBOARD ====================

@login_required
def dashboard(request):
    """
    Vista principal del sistema. Muestra métricas rápidas
    y últimos registros de proyectos y materiales.
    """
    total_proyectos = Proyecto.objects.count()
    proyectos_activos = Proyecto.objects.filter(estado='en_curso').count()
    materiales_bajo_stock = Material.objects.filter(stock_actual__lt=models.F('stock_minimo')).count()
    herramientas_prestadas = Herramienta.objects.filter(estado='prestada').count()

    materiales = Material.objects.all()[:5]
    proyectos = Proyecto.objects.all()[:5]

    context = {
        'total_proyectos': total_proyectos,
        'proyectos_activos': proyectos_activos,
        'materiales_bajo_stock': materiales_bajo_stock,
        'herramientas_prestadas': herramientas_prestadas,
        'materiales': materiales,
        'proyectos': proyectos,
    }
    return render(request, 'appiconstruction/dashboard.html', context)

# ==================== MATERIALES ====================

@login_required
def lista_materiales(request):
    """
    Lista general de materiales con opción de buscar por código,
    nombre o categoría.
    """
    materiales = Material.objects.all()
    query = request.GET.get('q')

    if query:
        materiales = materiales.filter(
            Q(codigo__icontains=query) |
            Q(nombre__icontains=query) |
            Q(categoria__nombre__icontains=query)
        )

    context = {'materiales': materiales}
    return render(request, 'appiconstruction/materiales/lista_materiales.html', context)


@login_required
def agregar_material(request):
    """
    Formulario para registrar un nuevo material en la bodega.
    """
    if request.method == 'POST':
        form = MaterialForm(request.POST)
        if form.is_valid():
            material = form.save()
            messages.success(request, f'Material "{material.nombre}" agregado correctamente.')
            return redirect('lista_materiales')
    else:
        form = MaterialForm()

    return render(request, 'appiconstruction/materiales/form_material.html', {'form': form, 'titulo': 'Agregar Material'})


@login_required
def editar_material(request, pk):
    """
    Permite modificar datos de un material ya existente.
    """
    material = get_object_or_404(Material, pk=pk)
    if request.method == 'POST':
        form = MaterialForm(request.POST, instance=material)
        if form.is_valid():
            form.save()
            messages.success(request, 'Material actualizado correctamente.')
            return redirect('lista_materiales')
    else:
        form = MaterialForm(instance=material)

    return render(request, 'appiconstruction/materiales/form_material.html', {'form': form, 'titulo': 'Editar Material'})


@login_required
def eliminar_material(request, pk):
    """
    Confirma y elimina un material del sistema.
    """
    material = get_object_or_404(Material, pk=pk)

    if request.method == 'POST':
        nombre = material.nombre
        material.delete()
        messages.success(request, f'Material "{nombre}" eliminado permanentemente.')
        return redirect('lista_materiales')

    return render(request, 'appiconstruction/materiales/eliminar_material.html', {'material': material})


# ==================== HERRAMIENTAS ====================

@login_required
def lista_herramientas(request):
    """
    Muestra todas las herramientas y permite filtrarlas por texto.
    """
    herramientas = Herramienta.objects.all()
    query = request.GET.get('q')

    if query:
        herramientas = herramientas.filter(
            Q(codigo__icontains=query) |
            Q(nombre__icontains=query) |
            Q(categoria__nombre__icontains=query)
        )

    return render(request, 'appiconstruction/herramientas/lista_herramientas.html', {'herramientas': herramientas})


@login_required
def agregar_herramienta(request):
    """
    Registrar una nueva herramienta en la bodega.
    """
    if request.method == 'POST':
        form = HerramientaForm(request.POST)
        if form.is_valid():
            herramienta = form.save()
            messages.success(request, f'Herramienta "{herramienta.nombre}" agregada correctamente.')
            return redirect('lista_herramientas')
    else:
        form = HerramientaForm()

    return render(request, 'appiconstruction/herramientas/form_herramienta.html', {'form': form, 'titulo': 'Agregar Herramienta'})


@login_required
def editar_herramienta(request, pk):
    """
    Edita la información de una herramienta registrada.
    """
    herramienta = get_object_or_404(Herramienta, pk=pk)

    if request.method == 'POST':
        form = HerramientaForm(request.POST, instance=herramienta)
        if form.is_valid():
            form.save()
            messages.success(request, 'Herramienta actualizada correctamente.')
            return redirect('lista_herramientas')
    else:
        form = HerramientaForm(instance=herramienta)

    return render(request, 'appiconstruction/herramientas/form_herramienta.html', {'form': form, 'titulo': 'Editar Herramienta'})


@login_required
def eliminar_herramienta(request, pk):
    """
    Elimina una herramienta luego de confirmación.
    """
    herramienta = get_object_or_404(Herramienta, pk=pk)

    if request.method == 'POST':
        nombre = herramienta.nombre
        herramienta.delete()
        messages.success(request, f'Herramienta "{nombre}" eliminada permanentemente.')
        return redirect('lista_herramientas')

    return render(request, 'appiconstruction/herramientas/eliminar_herramienta.html', {'herramienta': herramienta})


# ==================== BODEGAS ====================

@login_required
def lista_bodegas(request):
    """
    Lista todas las bodegas creadas en el sistema.
    """
    bodegas = Bodega.objects.all()
    return render(request, 'appiconstruction/bodegas/lista_bodegas.html', {'bodegas': bodegas})


@login_required
def agregar_bodega(request):
    """
    Formulario para crear una nueva bodega.
    """
    if request.method == 'POST':
        form = BodegaForm(request.POST)
        if form.is_valid():
            bodega = form.save()
            messages.success(request, f'Bodega "{bodega.nombre}" agregada correctamente.')
            return redirect('lista_bodegas')
    else:
        form = BodegaForm()

    return render(request, 'appiconstruction/bodegas/form_bodega.html', {'form': form, 'titulo': 'Agregar Bodega'})


@login_required
def editar_bodega(request, pk):
    """
    Modificación de una bodega ya existente.
    """
    bodega = get_object_or_404(Bodega, pk=pk)

    if request.method == 'POST':
        form = BodegaForm(request.POST, instance=bodega)
        if form.is_valid():
            form.save()
            messages.success(request, 'Bodega actualizada correctamente.')
            return redirect('lista_bodegas')
    else:
        form = BodegaForm(instance=bodega)

    return render(request, 'appiconstruction/bodegas/form_bodega.html', {'form': form, 'titulo': 'Editar Bodega'})


@login_required
def eliminar_bodega(request, pk):
    """
    Elimina una bodega del registro.
    """
    bodega = get_object_or_404(Bodega, pk=pk)

    if request.method == 'POST':
        nombre = bodega.nombre
        bodega.delete()
        messages.success(request, f'Bodega "{nombre}" eliminada permanentemente.')
        return redirect('lista_bodegas')

    return render(request, 'appiconstruction/bodegas/eliminar_bodega.html', {'bodega': bodega})


@login_required
def detalle_bodega(request, pk):
    """
    Muestra materiales y herramientas asignadas a una bodega.
    """
    bodega = get_object_or_404(Bodega, pk=pk)
    materiales = Material.objects.filter(bodega=bodega)
    herramientas = Herramienta.objects.filter(bodega=bodega)

    return render(request, 'appiconstruction/bodegas/detalle_bodega.html', {
        'bodega': bodega,
        'materiales': materiales,
        'herramientas': herramientas,
    })


# ==================== PROYECTOS ====================

@login_required
def lista_proyectos(request):
    """
    Lista de proyectos con filtro opcional por estado.
    """
    proyectos = Proyecto.objects.all()
    estado_filter = request.GET.get('estado')

    if estado_filter:
        proyectos = proyectos.filter(estado=estado_filter)

    return render(request, 'appiconstruction/proyectos/lista_proyectos.html', {'proyectos': proyectos})


@login_required
def agregar_proyecto(request):
    """
    Crea un nuevo proyecto dentro del sistema.
    """
    if request.method == 'POST':
        form = ProyectoForm(request.POST)
        if form.is_valid():
            proyecto = form.save()
            messages.success(request, f'Proyecto "{proyecto.nombre}" agregado correctamente.')
            return redirect('lista_proyectos')
    else:
        form = ProyectoForm()

    return render(request, 'appiconstruction/proyectos/form_proyecto.html', {'form': form, 'titulo': 'Agregar Proyecto'})


@login_required
def editar_proyecto(request, pk):
    """
    Edita los datos de un proyecto específico.
    """
    proyecto = get_object_or_404(Proyecto, pk=pk)

    if request.method == 'POST':
        form = ProyectoForm(request.POST, instance=proyecto)
        if form.is_valid():
            form.save()
            messages.success(request, 'Proyecto actualizado correctamente.')
            return redirect('lista_proyectos')
    else:
        form = ProyectoForm(instance=proyecto)

    return render(request, 'appiconstruction/proyectos/form_proyecto.html', {'form': form, 'titulo': 'Editar Proyecto'})


@login_required
def eliminar_proyecto(request, pk):
    """
    Elimina un proyecto del registro general.
    """
    proyecto = get_object_or_404(Proyecto, pk=pk)

    if request.method == 'POST':
        nombre = proyecto.nombre
        proyecto.delete()
        messages.success(request, f'Proyecto "{nombre}" eliminado permanentemente.')
        return redirect('lista_proyectos')

    return render(request, 'appiconstruction/proyectos/eliminar_proyecto.html', {'proyecto': proyecto})
