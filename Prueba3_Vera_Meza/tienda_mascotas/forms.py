from django import forms
from django.forms import ModelForm
from django.forms import widgets
from django.forms.models import ModelChoiceField
from .models import Producto
from django.contrib.auth.forms import UserCreationForm #clase proveniente de django para creación de usuarios
from django.contrib.auth.forms import User # importa clase desde el ADMIN DE DJANGO

class ProductoForm(forms.ModelForm):      #creación de clase formulario para productos
    class Meta:
        model = Producto # Nombre de la Clase
        fields = ['idProducto', 'marca', 'precioProducto', 'stock',
                  'categoria','imagen'] #Atributo de la Clase
        labels = {
            'idProducto': 'ID Producto',
            'marca': 'Marca',
            'precioProducto': 'Precio Producto',
            'stock': 'Stock',
            'categoria': 'Categoria',
            'imagen': 'Imagen'
        } #cierre labels

        widgets = {
            'idProducto': forms.TextInput(
                attrs={ #atributos del widgets
                    'class': 'form-control',
                    'placeholder': 'Ingrese Código de Producto...',
                    'id': 'id',

                }
            ),

            'marca': forms.TextInput(
                attrs={ #atributos del widgets
                    'class': 'form-control',
                    'placeholder': 'Ingrese marca....',
                    'id': 'marca',
                }
            ),
            
            'precioProducto':forms.TextInput(
                attrs={ #atributos del widgets
                    'class': 'form-control',
                    'placeholder': 'Ingrese modelo....',
                    'id': 'modelo',
                } 
                
            ),    
               
            'stock': forms.TextInput(
                attrs={ #atributos del widgets
                    'class': 'form-control',
                    'placeholder': 'Ingrese stock....',
                    'id': 'stock',
                } 
                
            ),

            'categoria': forms.Select(
               attrs={ #atributos del widgets
                    'class': 'form-control',
                    'id': 'stock',
                }  
            ),

            'imagen': forms.FileInput(
               attrs={ #atributos del widgets
                    'class': 'form-control',
                    'placeholder': 'Ingrese imagen',
                    'id': 'imagen',
                    #NO QUEREMOS QUE SEA REQUERIDA X ESO NO AGREGAMOS EL ID
                }  
            ),

            
        }#cierre de widgets
'''
class RegistroUserForm(UserCreationForm):  #al agregar esta clase de formulario , automaticamente se crean username y password en el formulario 
    pass                                    #solo se debe agregar pass para que solicite los campos principales
'''

class RegistroUserForm(UserCreationForm):  
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email','password1','password2']
        labels = {
            'username': 'Nombre de Usuario',
            'first_name': 'Primer Nombre',
            'last_name': 'Apellido Paterno',
            'email': 'Correo Electrónico',
            'password1': 'clave',
            'password2': 'Reingrese su clave'
        } #cierre labels

        widgets = {
            'username': forms.TextInput(
                attrs={ #atributos del widgets
                    'class': 'form-control',
                    'placeholder': 'Ingrese un Nombre para su usuario',
                    'id': 'id',

                }
            ),

            'first_name': forms.TextInput(
                attrs={ #atributos del widgets
                    'class': 'form-control',
                    'placeholder': 'Ingrese su Nombre',
                    'id': 'first_name',
                }
            ),
            
            'last_name':forms.TextInput(
                attrs={ #atributos del widgets
                    'class': 'form-control',
                    'placeholder': 'Ingrese su apellido paterno',
                    'id': 'last_name',
                } 
                
            ),    
               
            'email': forms.TextInput(
                attrs={ #atributos del widgets
                    'class': 'form-control',
                    'placeholder': 'ejemplo correo@correo.cl',
                    'id': 'email',
                } 
                
            ),

            'password1': forms.TextInput(
               attrs={ #atributos del widgets
                    'class': 'form-control',
                    'placeholder': 'Cree una Contraseña Robusta',
                    'id': 'password1',
                }  
            ),

            'password2': forms.TextInput(
               attrs={ #atributos del widgets
                    'class': 'form-control',
                    'placeholder': 'Repita su contraseña',
                    'id': 'password2',
                }  
            ),

            
        }#cierre de widgets