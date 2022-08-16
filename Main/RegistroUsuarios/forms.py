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

    password1 = forms.CharField(label="Contraseña", widget=forms.PasswordInput)
    password2 = forms.CharField(label="Repetir contraseña", widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['email', 'first_name', 'last_name']

    def clean_password2(self):

        password2 = self.cleaned_data["password2"]
        if password2 != self.cleaned_data["password1"]:
            raise forms.ValidationError("Las contraseñas no coinciden..")
        return password2

class AvatarFormulario(forms.ModelForm):

    class Meta:
        model=Avatar
        fields=('imagen',)