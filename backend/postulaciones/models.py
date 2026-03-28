from django.db import models
from django.conf import settings

class Postulacion(models.Model):
    usuario = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=200)
    empresa = models.CharField(max_length=200)
    link = models.URLField()
    modalidad = models.CharField(max_length=50)
    rubro = models.CharField(max_length=100, blank=True, null=True)
    fecha_postulacion = models.DateTimeField(auto_now_add=True)
    fecha_aplicacion = models.DateField(auto_now_add=True)
    
    class Meta:
        unique_together = ['usuario', 'link', 'fecha_aplicacion']