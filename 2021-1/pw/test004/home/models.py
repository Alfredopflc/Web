from django.db import models

class Usuario(models.Model):
    name = models.CharField(max_length=20)
    producto = models.CharField(max_length=20)
    num = models.IntegerField()

    def __str__(self):
        return self.name
