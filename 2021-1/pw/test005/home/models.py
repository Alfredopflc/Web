from django.db import models

class Usuario(models.Model):
    producto = models.CharField(max_length=20)
    color = models.CharField(max_length=20)
    cantidad = models.IntegerField()

    def __str__(self):
        return self.producto
