def clean_password2(self):

    password2 = self.cleaned_data["password2"]
    if password2 != self.cleaned_data["password1"] or password2.isnumeric() or len(password2) < 8:
        raise forms.ValidationError("...")
            
    return password2