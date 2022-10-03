from django import forms
from .models import Wish


class WishesForm(forms.ModelForm):

    class Meta:
        model = Wish
        fields = ['wish']


class DescriptionForm(forms.ModelForm):

    class Meta:
        model = Wish
        fields = ['description']


class ImageForm(forms.ModelForm):

    class Meta:
        model = Wish
        fields = ['image']

    # def save(self, commit=True):
    #     image = super(ImageForm, self).save()
    #     image.image = self.cleaned_data['image']
    #     if commit:
    #         image.save()
    #     return image


class TestImageForm(forms.ModelForm):

    class Meta:
        model = Wish
        fields = ['wish', 'description', 'image']
