from django.db import models

class Usuarios(models.Model):
    id_usuario = models.AutoField(primary_key=True)
    nome = models.TextField(max_length=255, blank=True)
    email = models.TextField(max_length=30, blank=True)