from django.shortcuts import render
from .models import Usuarios

def home(request):
    return render(request,'usuarios/home.html')

def usuarios(request):
    novo_usuario = Usuarios()
    novo_usuario.nome = request.POST.get('nome')
    novo_usuario.email = request.POST.get('email')
    novo_usuario.save()

    #exibir usuarios em nova pagina

    usuarios2 = {
        'usuarios': Usuarios.objects.all()
    }
    return render(request,'usuarios/usuarios.html',usuarios2)