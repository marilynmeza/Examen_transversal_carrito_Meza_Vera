# Generated by Django 4.2.2 on 2023-06-18 04:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda_mascotas', '0002_producto_imagen'),
    ]

    operations = [
        migrations.AlterField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(blank=True, null=True, upload_to='imagenes', verbose_name='Imagen'),
        ),
    ]
