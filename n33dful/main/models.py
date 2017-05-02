from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Tag(models.Model):
    nombre = models.CharField(max_length=45)

class Sexo(models.Model):
    nombre_sexo = models.CharField(max_length=15)

    def __str__(self):
        return "{0}".format(self.nombre_sexo)

class Escuela(models.Model):
    nombre = models.CharField(max_length=230)

    def __str__(self):
        return "{0}".format(self.nombre)

class Usuario(models.Model):
    id_user = models.OneToOneField(User, on_delete=models.CASCADE)
    #nickname = models.CharField(max_length=45)
    id_escuela = models.ForeignKey(Escuela, on_delete=models.CASCADE)
    id_sexo = models.ForeignKey(Sexo, on_delete=models.CASCADE)
    nombre = models.CharField(max_length=45)
    apellido = models.CharField(max_length=45)
    fecha_nacimiento = models.DateField(auto_now=False,auto_now_add=False)
    #password = models.CharField(max_length=45)
    correo = models.CharField(max_length=60)
    fecha_creacion = models.DateTimeField(auto_now=False, auto_now_add=True)

    def __str__(self):
        return "{0}".format(self.nombre)


class Publicacion(models.Model):
    id_autor = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    nombre_publicacion = models.CharField(max_length = 45)
    descripcion = models.TextField()
    path_archivo = models.CharField(max_length = 200)
    fecha_creacion = models.DateTimeField(auto_now=False, auto_now_add=True)
    fecha_modificacion = models.DateTimeField(auto_now=True, auto_now_add=False)

class Comentario(models.Model):
    texto_comentario = models.TextField()

class PublicacionComentario(models.Model):
    id_comentario = models.ForeignKey(Comentario, on_delete=models.CASCADE)
    id_autor_comentario = models.ForeignKey(Usuario, on_delete=models.CASCADE)
    id_publicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE)

class Seguidores(models.Model):
    id_usuario = models.ForeignKey(Usuario, related_name="id_usuario")
    id_seguidor = models.ForeignKey(Usuario, related_name="id_seguidor")

class PublicacionTag(models.Model):
    id_tag = models.ForeignKey(Tag, on_delete=models.CASCADE)
    id_publicacion = models.ForeignKey(Publicacion, on_delete=models.CASCADE)
