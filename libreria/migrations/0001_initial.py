# Generated by Django 4.1 on 2022-08-30 02:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Libro',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('titulo', models.CharField(max_length=100, null=True, verbose_name='Titulo')),
                ('imagen', models.ImageField(upload_to='imagenes/', verbose_name='Imagen')),
                ('descripcion', models.CharField(max_length=255, null=True, verbose_name='Descripcion')),
            ],
        ),
    ]
