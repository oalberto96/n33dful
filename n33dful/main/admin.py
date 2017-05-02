from django.contrib import admin
from .models import Usuario, Publicacion, Escuela, Sexo

# Register your models here.
admin.site.register(Usuario)
admin.site.register(Publicacion)
admin.site.register(Escuela)
admin.site.register(Sexo)
