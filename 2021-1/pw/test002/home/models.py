from django.db import models

class Usuario(models.Model):
    name = models.CharField(max_length=32)
    correo = models.CharField(max_length=32)
    ID = models.IntegerField()

    def __str__(self):
        return self.name

        #

        