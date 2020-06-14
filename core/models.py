from django.db import models


# Este Modelo me permitira actualizar la seccion de cursos
class cursos(models.Model):
    nombre = models.CharField(max_length=150)
    descripcion = models.TextField(null=True, blank=True)
    dia = models.CharField(max_length=2, null=True, blank=True)
    mes = models.CharField(max_length=10, null=True, blank=True)
    año = models.IntegerField(null=True, blank=True)
    numcomentarios = models.IntegerField(null=True, blank=True)
    numvistas = models.IntegerField(null=True, blank=True)
    foto = models.ImageField(upload_to='cursos/foto', null=True)
    orden = models.IntegerField(null=True, blank=True)

    def __str__(self):
        return self.nombre

    class Meta:
        ordering = ['orden']


class temario(models.Model):
    tema = models.CharField(max_length=150)
    minutos = models.IntegerField(null=True, blank=True)
    nivel = models.CharField(max_length=150)
    curso = models.ForeignKey(cursos, on_delete=models.CASCADE, null=True, blank=True,related_name='temario')

    def __str__(self):
        return self.tema

    class Meta:
        ordering = ['id']


# Este Modelo me permitira actualizar la seccion de comentarios de alumnos
class comentariosalumnos(models.Model):
    nombre = models.CharField(max_length=150)
    comentario = models.TextField(null=True, blank=True)
    foto = models.ImageField(upload_to='comentarios/foto', blank=True, null=True)

    def __str__(self):
        return self.nombre


# Este Modelo me permitira actualizar la seccion de portafolios
class portafolio(models.Model):
    nombre = models.CharField(max_length=150)
    link = models.CharField(max_length=150)
    categoria = models.CharField(max_length=250)
    foto = models.ImageField(upload_to='portafolio/foto', blank=True, null=True)

    def __str__(self):
        return self.nombre


# Este Modelo me permitira actualizar la seccion de personal mis datos principales
class personal(models.Model):
    textobienvenida = models.TextField(null=True, blank=True)
    fotofondo = models.ImageField(upload_to='portada/fotofondo', blank=True, null=True)
    textoacerca = models.TextField(null=True, blank=True)
    fotoperfil = models.ImageField(upload_to='portada/fotoperfil', blank=True, null=True)
    pdf = models.FileField(upload_to='pdf', null=True, blank=True)
    videopresentacion = models.CharField(max_length=150)


class experiencia(models.Model):
    empresa = models.CharField(max_length=150)
    cargo = models.CharField(max_length=150)
    año = models.IntegerField(null=True, blank=True)
    funciones = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.empresa

    class Meta:
        ordering = ['año']

# Create your models here.
