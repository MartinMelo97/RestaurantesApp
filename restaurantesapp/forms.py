from django import forms
from .models import RestaurantModel

class RestaurantForm(forms.ModelForm):
    class Meta:
        model = RestaurantModel
        fields = ['name', 'is_open', 'is_closed']