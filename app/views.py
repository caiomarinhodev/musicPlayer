# Create your views here.
from django.shortcuts import render, redirect

from .models import Musica


def reproduzir_musica(request):
    musicas = Musica.objects.all()
    return render(request, 'reprodutor_musica/reproduzir_musica.html', {'musicas': musicas})


def carregar_musica(request):
    if request.method == 'POST':
        nome = request.POST.get('nome')
        arquivo = request.FILES.get('arquivo')
        Musica.objects.create(nome=nome, arquivo=arquivo)
    return redirect('reproduzir_musica')
