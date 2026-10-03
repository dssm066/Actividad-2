from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models


class Personaje(models.Model):
    nombre = models.CharField(max_length=100)
    serie = models.CharField(max_length=100)
    descripcion = models.TextField()
    edad = models.IntegerField(
        validators=[
            MinValueValidator(0),
            MaxValueValidator(150)
        ]
    )
    fecha_creacion = models.DateField(auto_now_add=True)
    principal = models.BooleanField(default=False)

    usuario = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name='personajes'
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=['usuario', 'serie', 'nombre'],
                name='unique_personaje_usuario_serie_nombre'
            )
        ]
        ordering = ['nombre']

    def __str__(self):
        return self.nombre