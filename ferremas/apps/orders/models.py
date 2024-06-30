from django.db import models
from django.contrib.auth.models import User

class Orden(models.Model):
    usuario = models.ForeignKey(User, on_delete=models.CASCADE)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    estado = models.CharField(max_length=20, choices=[('PENDIENTE', 'Pendiente'), ('COMPLETADO', 'Completado')])
    creado = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Orden {self.id} - {self.usuario.username}"
