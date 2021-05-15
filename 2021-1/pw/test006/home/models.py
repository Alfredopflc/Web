from django.db import models

class Usuario(models.Model):
    plataforma = models.CharField(max_length=20)
    descargas = models.CharField(max_length=20)
    ID= models.IntegerField()

    def __str__(self):
        return self.plataforma
