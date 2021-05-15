from django.db import models

class Usuario(models.Model):
    componente = models.CharField(max_length=20)
    color = models.CharField(max_length=20)
    costo = models.IntegerField()

    def __str__(self):
        return self.componente
        