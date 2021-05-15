from django.contrib import admin

from .models import Usuario, Administrador, Docente, Alumno, Materia, Periodo, Calificacion

admin.site.register(Usuario)
admin.site.register(Administrador)
admin.site.register(Docente)
admin.site.register(Alumno)
admin.site.register(Materia)
admin.site.register(Periodo)
admin.site.register(Calificacion)

# Register your models here.
