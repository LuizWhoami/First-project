from django.urls import path
from app_cadastro import views

urlpatterns = [
    #rota, view_responsavel e nome de referencia
    #01 usuarios
    path('',views.home,name='home'),
    #usuarios.com/usuarios
    path('usuarios/',views.usuarios,name='listagem_emails')
]
