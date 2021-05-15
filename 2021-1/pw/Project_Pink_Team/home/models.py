from django.db import models 
#


class Usuario(models.Model):
    Nombre = models.CharField(max_length=32)
    Apellido = models.CharField(max_length=32)
    Celular = models.CharField(max_length=10, blank=True)
    CURP = models.CharField(max_length=18)
    FechaNacimiento = models.DateTimeField()
    Direccion = models.CharField(max_length=100)
    Correo = models.CharField(max_length=50)

    def __str__(self):
        return self.Nombre


class Administrador(models.Model):
    Nombre = models.CharField(max_length=50)
    Permisos = models.BooleanField(default=False)
    ID_Usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.Permisos

class Docente(models.Model):
    Titulo = models.CharField(max_length=50)
    ID_Usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.Titulo

class Alumno(models.Model):
    Grado = models.CharField(max_length=10)
    ID_Usuario = models.ForeignKey(Usuario, on_delete=models.CASCADE)

    def __str__(self):
        return self.Grado

class Periodo(models.Model):
    NombrePeriodo = models.CharField(max_length=50)

    def __str__(self):
        return self.NombrePeriodo

class Materia(models.Model):
    Materia = models.CharField(max_length=50)
    Horario = models.CharField(max_length=8)
    ID_Periodo = models.ForeignKey(Periodo, on_delete=models.CASCADE)
    ID_Docente = models.ForeignKey(Docente, on_delete=models.CASCADE)

    def __str__(self):
        return self.Materia

class Calificacion(models.Model):
    NoControl = models.ForeignKey(Alumno, on_delete=models.CASCADE)
    ID_Materia = models.ForeignKey(Materia, on_delete=models.CASCADE)
    Bimestre1 = models.FloatField()
    Bimestre2 = models.FloatField()
    Bimestre3 = models.FloatField()
    Bimestre4 = models.FloatField()
    Bimestre5 = models.FloatField()
    Promedio = models.FloatField()

    def __str__(self):
        return self.Promedio

# Create your models here.
