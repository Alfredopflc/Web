from django.db import models

class Usuario(models.Model):
    lenguajes = models.CharField(max_length=20)
    usuarios = models.CharField(max_length=20)
    ID = models.IntegerField()

    def __str__(self):
        return self.lenguajes
#