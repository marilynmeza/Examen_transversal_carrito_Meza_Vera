# Generated by Django 4.2.2 on 2023-06-18 04:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tienda_mascotas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='producto',
            name='imagen',
            field=models.ImageField(null=True, upload_to='imagenes', verbose_name='Imagen'),
        ),
    ]
