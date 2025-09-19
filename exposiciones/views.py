from django.shortcuts import render
from .models import Exposicion

def lista_exposiciones(request):
    categoria = request.GET.get('categoria', 'Todas')
    if categoria == 'Todas':
        exposiciones = Exposicion.objects.all().order_by('-created_at')
    else:
        exposiciones = Exposicion.objects.filter(categoria=categoria).order_by('-created_at')

    categorias = ['Todas'] + [c[0] for c in Exposicion._meta.get_field('categoria').choices]
    return render(request, 'exposiciones/lista.html', {'exposiciones': exposiciones, 'categorias': categorias, 'selected': categoria})
