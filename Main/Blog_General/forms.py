

from django import forms

from Blog_General.models import Publicacion

from .models import Comentario


# Damos formato al formulario de NewComment.
class NewCommentForm(forms.ModelForm):
    class Meta:
        model= Comentario
        fields= ("body",)
        widgets= {
            'body': forms.Textarea(
                attrs={
                    'placeholder': 'Comenta aqui',
                    'width': 38,
                    'height': 100,
                    'cols': '115',
                    'rows': '3',
                    
                }
            )
        }
        

# Damos formato al form de PublicacionForm        
class PublicacionForm(forms.ModelForm):
    class Meta:
        model= Publicacion
        fields= ("titulo", "contenido", "imagen", "descripcion")
        widgets= {
            'titulo': forms.TextInput(
                attrs={
                    'placeholder': 'Es necesario un titulo para realizar el Post',
                    'width': 38,
                    'height': 100,
                    'cols': '115',
                    'rows': '3',
                    'class': 'form-control', 
                    'type': 'text',
                    'data-sb-validations':'required',
                    
                }
            ),
            'contenido': forms.Textarea(
                attrs={
                    'placeholder': 'Es necesario un contenido para realizar el Post',
                    'width': 38,
                    'height': 100,
                    'cols': '115',
                    'rows': '3',
                    'class': 'form-control', 
                    'type': 'text',
                    'data-sb-validations':'required',
                    'type':'textarea',
                    'style':'height:314px;',
                    
                }
            ),
            'imagen': forms.TextInput(
                attrs={
                    'placeholder': 'Es necesario una imagen para realizar el Post',
                    'width': 38,
                    'height': 100,
                    'cols': '115',
                    'rows': '3',
                    'class': 'form-control', 
                    'type': 'text',
                    'data-sb-validations':'required',
                    
                }
            ),
            'descripcion': forms.TextInput(
                attrs={
                    'placeholder': 'Es necesario una descripcion para realizar el Post',
                    'width': 38,
                    'height': 100,
                    'cols': '115',
                    'rows': '3',
                    'class': 'form-control', 
                    'type': 'text',
                    'data-sb-validations':'required',
                    'type':'textarea',
                    'style':'height:90px;',
                    
                }
            )
        }