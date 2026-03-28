from django.db import models
from django.contrib.auth.models import AbstractUser

class Usuario(AbstractUser):
    pais = models.CharField(max_length=100, blank=True, null=True)
    hora_postulacion = models.CharField(max_length=5, blank=True, null=True)
    cv = models.FileField(upload_to='cvs/', blank=True, null=True)
    modalidades_preferidas = models.JSONField(default=list)
    rubros_preferidos = models.JSONField(default=list)
    postulaciones_activas = models.BooleanField(default=True)