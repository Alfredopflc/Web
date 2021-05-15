from django.db import models

class Usuario(models.Model):
    juego = models.CharField(max_length=20)
    consola = models.CharField(max_length=20)
    ID = models.IntegerField()

    def __str__(self):
        return self.juego
