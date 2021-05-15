from django.db import models

class Usuario(models.Model):
    name = models.CharField(max_length=20)
    address = models.CharField(max_length=20)
    age = models.IntegerField()

    def __str__(self):
        return self.name
#