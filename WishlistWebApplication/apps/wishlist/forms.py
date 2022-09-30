from django import forms
from .models import Wish


class WishesForm(forms.ModelForm):

    class Meta:
        model = Wish
        fields = ['wish']


class DescriptionForm(forms.ModelForm):

    class Meta:
        model = Wish
        fields = ['description', 'image']
        widgets ={
            'description': forms.Textarea(attrs={'class': 'form-input'}),
            'image': forms.ImageField()
        }