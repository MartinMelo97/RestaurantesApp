from django import forms
from django.contrib.auth.models import User


class RegistroForm(forms.ModelForm):

    password = forms.CharField(label="Contraseña",
                               widget=forms.PasswordInput)

    password2 = forms.CharField(label="Repite tu contraseña",
                                widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError("Los password no coinciden")
        return cd['password2']