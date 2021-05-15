from django.db import models

class Usuario(models.Model):
    personaje = models.CharField(max_length=20)
    color = models.CharField(max_length=20)
    ID = models.IntegerField()

    def __str__(self):
        return self.personaje
        