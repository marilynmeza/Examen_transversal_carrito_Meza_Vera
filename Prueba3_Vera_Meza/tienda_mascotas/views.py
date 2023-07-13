# Create your views here.
from django.shortcuts import render,redirect
from tienda_mascotas.models import Producto, Boleta, detalle_boleta
from .forms import ProductoForm #importamos nuestra clase desde el formulario
from .forms import RegistroUserForm #importamos nuestra clase desde el formulario para registro de usuarios
from django.contrib import messages #para poder ver los mensajes
from django.contrib.auth import authenticate, login #para autenticacion de usuarios
from tienda_mascotas.compras import Carrito
# Create your views here.

def inicio (request):
    return render(request,'inicio.html')

def cards (request):
    return render(request,'cards.html')

def alimentos (request):
    return render(request,'alimentos.html')

def valida(request):
    return render(request,'valida.html')

def venta(request):
    return render(request,'venta.html')

#Vaya a la clase Producto y traiga 
# todos los objetos y envielos como parametros al template productos_stock
def productos_stock(request):
    productos= Producto.objects.raw('Select * from tienda_mascotas_producto')
    datos = {
        'productitos' :  productos 

    }

    return render(request,'productos_stock.html',datos) 
    '''
    productos = Producto.objects.all()  #argumento productos, 
                                        #le solicita a la clase Producto que me traiga todos los objetos
    datos = {
        'productitos' :  productos 

    } #diccionario, nombre asignado datos, se compone del dato que va a recibir la informacion entre comillas simple
    # ademas es el que llega al HTML , el productos que se le asigna es el que declaramos anteriormente
    return render(request,'productos_stock.html',datos) 

    '''
    #PROGRAMACION DE MANERA NATIVA EN PYTHON METODO CREAR
def crear(request):
        if request.method=="POST":
            productoform = ProductoForm(request.POST, request.FILES)
            #si mi objeto que estoy creando es valido
            if productoform.is_valid():
                #para agregar filas forma nativa --> save (similar al insert, creara un nuevo objeto)
                productoform.save()
                return redirect('productos_stock')
                #redireccionaremos para otro template, se debe implementar la biblioteca redirect
                
        else:
            productoform=ProductoForm()
        return render(request, 'crear.html', {'productoform': productoform})  
   
    #metodo recibe dos parametros, solicitud web, recibe un id -->id producto
    #2da linea, asignamosnombre_objeto_eliminado = ClasedelProducto.llamamosobjeto.get (claveprimaria = asignele el valor id)
    #get --> realiza busqueda precisa y UNICA
    #3ra nombreobjeto.funcioneliminar
    #4ta linea redirija a productos_stock
def eliminar(request, id):
    productoEliminado = Producto.objects.get(idProducto = id )  #obtenemos un objeto por su ID
    productoEliminado.delete()
    return redirect('productos_stock')


#metodo modificar recibe dos parametros al igual que eliminar
#2da linea, asignamosnombre_objeto_eliminado = ClasedelProducto.llamamosobjeto.get(claveprimaria =  asignele el valor id)
#get --> realiza busqueda precisa y UNICA
#3ra creamos diccionario que enviaremos al html
#4ta 'form' --> nombre asignado al diccionario en el html : tendrá una instancia del ProductoForm
#4ta, a su vez el objeto ProductoForm tendrá una instancia del productoModificado 
def modificar(request, id):
    productoModificado = Producto.objects.get(idProducto = id )  #obtenemos un objeto por su ID
    datos = {
        'form': ProductoForm(instance=productoModificado) #devuelve el objeto instanciado
                                                        #de acuerdo al idProducto
    }
    if request.method=='POST': # si lo solicitado . method es igual a POST
        # le enviamos un formulario que instancie la data , para el almacenamiento (instance=prod...)
        formulario = ProductoForm (data=request.POST , files=request.FILES , instance =productoModificado)
       # formulario = ProductoForm (data=request.FILES, instance =productoModificado)
        if formulario.is_valid():      #preguntamos si mi formulario es valido
            formulario.save()          #entonces el objeto formulario almacenelo
            return redirect('productos_stock') #redireccione al listado de los productos
    return render(request,'modificar.html', datos) #renderizamos a la solicitud, en el templed modificar, aqui podremos ver el diccionario datos

#METODO PARA REGISTRAR AL USUARIO E INICIAR SESION

def registrar(request):
    data ={
        'form': RegistroUserForm()
    }
    formulario = RegistroUserForm(data=request.POST)
    if formulario.is_valid():
        formulario.save()
        user = authenticate(username=formulario.cleaned_data["username"],
                            password=formulario.cleaned_data["password1"]
                            )
        login(request, user)
        messages.success(request, "Bienvenid@! Te has registrado exitosamente!")
        return redirect('inicio')
    data["form"] = formulario   #sobreescribimos el form
    return render(request, 'registration/registro.html',data)

def mostrar(request):
    producto = Producto.objects.all() #similar a un select
    datos={         #definimos un diccionario
        'productitos': producto
    }
    return render(request,'mostrar.html', datos)



# CARRITO DE COMPRAS  ... revisar!!!
def tienda(request):
    producto = Producto.objects.all()
    datos={
        'productitos': producto
    }
    return render(request, 'mostrar.html', datos)


def agregar_producto(request,id):
    carrito_compra= Carrito(request)
    producto = Producto.objects.get(idProducto=id)
    carrito_compra.agregar(producto=producto)
    return redirect('tienda')

def eliminar_producto(request, id):
    carrito_compra= Carrito(request)
    producto = Producto.objects.get(idProducto=id)
    carrito_compra.eliminar(producto=producto)
    return redirect('tienda')

def restar_producto(request, id):
    carrito_compra= Carrito(request)
    producto = Producto.objects.get(idProducto=id)
    carrito_compra.restar(producto=producto)
    return redirect('tienda')

def limpiar_carrito(request):
    carrito_compra= Carrito(request)
    carrito_compra.limpiar()
    return redirect('tienda')    


#ARREGLAR LO SIGUIENTE:

def generarBoleta(request):
    precio_total=0
    for key, value in request.session['carrito'].items():
        precio_total = precio_total + int(value['precio']) * int(value['cantidad'])
    boleta = Boleta(total = precio_total)
    boleta.save()
    productos = []
    for key, value in request.session['carrito'].items():
            producto = Producto.objects.get(idProducto = value['producto_id'])
            cant = value['cantidad']
            subtotal = cant * int(value['precio'])
            detalle = detalle_boleta(id_boleta = boleta, id_producto = producto, cantidad = cant, subtotal = subtotal)
            detalle.save()
            productos.append(detalle)
    datos={
        'productos':productos,
        'fecha':boleta.fechaCompra,
        'total': boleta.total
    }
    request.session['boleta'] = boleta.id_boleta
    carrito = Carrito(request)
    carrito.limpiar()
    return render(request, 'detallecarrito.html',datos)
    