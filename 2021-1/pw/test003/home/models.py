from django.db import models

class Usuario(models.Model):
    name = models.CharField(max_length=20)
    apellido = models.CharField(max_length=20)
    ID = models.IntegerField()

    def __str__(self):
        return self.name
    
    #