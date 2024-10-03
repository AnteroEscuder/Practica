from django.shortcuts import render
from .models import Animal, Protectora, Colaborador

def animales_list(request):
    animales = Animal.objects.all()
    return render(request, 'animales_list.html', {'animales': animales})

def protectoras_list(request):
    protectoras = Protectora.objects.all()
    return render(request, 'protectoras_list.html', {'protectoras': protectoras})

def colaboradores_list(request):
    colaboradores = Colaborador.objects.all()
    return render(request, 'colaboradores_list.html', {'colaboradores': colaboradores})