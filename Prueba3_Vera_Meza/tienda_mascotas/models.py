import datetime
from distutils.command.upload import upload
from django.db import models
from django.contrib.auth import get_user_model
from django.conf import settings
from django.contrib.auth.models import User

# Create your models here.
class Categoria(models.Model):
    idCategoria = models.IntegerField(primary_key=True, verbose_name="Id de Categoria")
    nombreCategoria = models.CharField(max_length=50, blank=True, verbose_name="Nombre de Categoria")

    def __str__(self):
        return self.nombreCategoria #permite acceder a los objetos a través de su nombre en el admin

class Producto(models.Model):
    idProducto = models.IntegerField(primary_key=True, verbose_name="Id Producto")
    marca = models.CharField(max_length=30, verbose_name="Marca del Producto")
    precioProducto =models.IntegerField (verbose_name="Precio Producto")
    stock = models.IntegerField(verbose_name= "Cantidad en Stock", blank=False)
    imagen = models.ImageField(upload_to="imagenes", null=True,blank=True, verbose_name='Imagen')
    categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE, verbose_name="Categoria") #atributo para enlazar las dos clases

    def get_internal_type(self):
        return 'idProducto'
    
    
    ''' NO ME RESULTA DEVOLVER EL NÚMERO INCREMENTAL AUTOMATICO VISUALMENTE
    def __str__(self):
        return self.idProducto
        
        '''
    
    '''CARRITO Y BOLETA'''
class Boleta(models.Model):
    id_boleta=models.AutoField(primary_key=True)
    total=models.BigIntegerField()
    fechaCompra=models.DateTimeField(blank=False, null=False, default = datetime.datetime.now)
    
    def __str__(self):
        return str(self.id_boleta)

class detalle_boleta(models.Model):
    id_boleta = models.ForeignKey('Boleta', blank=True, on_delete=models.CASCADE)
    id_detalle_boleta = models.AutoField(primary_key=True)
    id_producto = models.ForeignKey('Producto', on_delete=models.CASCADE)
    cantidad = models.IntegerField()
    subtotal = models.BigIntegerField()

    def __str__(self):
        return str(self.id_detalle_boleta)