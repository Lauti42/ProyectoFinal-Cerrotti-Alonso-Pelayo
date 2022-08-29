

from django import forms

from Blog_General.models import Publicacion

from .models import BlogImagen, Comentario


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


    def __init__(self, *args, **kwargs):
        super(PublicacionForm, self).__init__(*args, **kwargs)
        self.fields['publicado'].required = False
        self.fields['muestra_superior'].required = False
        self.fields['muestra_inferior'].required = False 
        self.fields['likes'].required= False
        
        

    
    class Meta:
        model= Publicacion
        fields= ("titulo", "descripcion", "contenido","publicado",'muestra_superior','muestra_inferior','likes')
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
            ),
            'publicado': forms.HiddenInput(
                attrs={
                    
                    'style':"visibility: hidden;",
                    
                }
            ),
            'muestra_superior': forms.HiddenInput(
                attrs={
                    'style':"visibility: hidden;",
                    
                }
            ),
            'muestra_inferior': forms.HiddenInput(
                attrs={

                    'style':"visibility: hidden;",
                    
                }
            ),
            'likes': forms.HiddenInput(
                attrs={

                    'style':"visibility: hidden;",
                    
                }
            ),
        }

class PublicacionFormAdmin(forms.ModelForm):


    def __init__(self, *args, **kwargs):
        super(PublicacionFormAdmin, self).__init__(*args, **kwargs)
        self.fields['publicado'].required = False
        self.fields['muestra_superior'].required = False
        self.fields['muestra_inferior'].required = False 
        self.fields['likes'].required= False
        
        

    
    class Meta:
        model= Publicacion
        fields= ("titulo", "descripcion", "contenido","publicado",'muestra_superior','muestra_inferior','likes')
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
            ),
            
        }        


class BlogImagenForm(forms.ModelForm):

    class Meta:
        model=BlogImagen
        fields=('imagen',) 
        widgets= {
            'imagen': forms.FileInput(
                attrs={
                    'type': 'file',
                    'class': 'form-control',
                
                }
            ),
        }