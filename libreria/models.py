from django.db import models

# Create your models here.


class Libro(models.Model):
    id = models.AutoField(primary_key=True)
    titulo = models.CharField(max_length=100, verbose_name='Titulo', null=True)
    imagen = models.ImageField(max_length=100, verbose_name='Imagen', upload_to='imagenes/')
    descripcion = models.CharField(max_length=255, verbose_name='Descripcion', null=True)

    def delete(self, using=None, keep_parents=False):
        self.imagen.storage.delete(self.imagen.name)
        super().delete()
