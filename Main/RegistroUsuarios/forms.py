from django import forms
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth.models import User
from RegistroUsuarios.models import Avatar
class PreferenciasFormulario(forms.Form):

    lenguaje = forms.CharField()
    backofront = forms.CharField()
    pais = forms.CharField()
    trabajo = forms.CharField() 

class AvatarFormulario(forms.Form):

    avatar = forms.ImageField()

class UserEditForm(UserChangeForm):

    password = forms.CharField(
        help_text="",
        widget=forms.HiddenInput(), required=False
    )

    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput(attrs={'class': 'form-control'}))
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput(attrs={'class': 'form-control'}))

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name','username']
        widgets= {
            'imagen': forms.FileInput(
                attrs={
                    'type': 'file',
                    'class': 'form-control',
                
                }
            ),
            'email': forms.EmailInput(
                attrs={
                    'type': 'email',
                    'class': 'form-control',
                    'placeholder': 'Email',
                    'required': 'true',
                    'data-sb-validations':'required|email',
                    'data-sb-errors':'Email no válido',
                    'data-sb-required-message':'Email requerido',
                }
            ),
            'first_name': forms.TextInput(
                attrs={
                    'type': 'text',
                    'class': 'form-control',
                    'placeholder': 'Nombre',
                    'required': 'true',
                    'data-sb-validations':'required',
                    'data-sb-errors':'Nombre requerido',
                    'data-sb-required-message':'Nombre requerido',
                }
            ),
            'last_name': forms.TextInput(
                attrs={
                    'type': 'text',
                    'class': 'form-control',
                    'placeholder': 'Apellido',
                    'required': 'true',
                    'data-sb-validations':'required',
                    'data-sb-errors':'Apellido requerido',
                    'data-sb-required-message':'Apellido requerido',
                }
            ),
            'username': forms.TextInput(
                attrs={
                    'type': 'text',
                    'class': 'form-control',
                    'placeholder': 'Nombre de usuario',
                    'required': 'true',
                    'data-sb-validations':'required',
                    'data-sb-errors':'Nombre de usuario requerido',
                    'data-sb-required-message':'Nombre de usuario requerido',
                }
            ),
            'password': forms.PasswordInput(
                attrs={
                    'type': 'password',
                    'class': 'form-control',
                    'placeholder': 'Contraseña',
                    'required': 'true',
                    'data-sb-validations':'required',
                    'data-sb-errors':'Contraseña requerida',
                    'data-sb-required-message':'Contraseña requerida',
                }
            ),
            
        }

    def clean_password2(self):

        password2 = self.cleaned_data["password2"]
        if password2 != self.cleaned_data["password1"]:
            raise forms.ValidationError("Las contraseñas no coinciden..")
        return password2

class AvatarFormulario(forms.ModelForm):

    class Meta:
        model=Avatar
        fields=('imagen',) 
        widgets= {
            'imagen': forms.FileInput(
                attrs={
                    'type': 'file',
                    'class': 'form-control',
                
                }
            ),
        }