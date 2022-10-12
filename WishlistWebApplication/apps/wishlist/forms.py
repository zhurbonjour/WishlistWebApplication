from django import forms
from .models import Wish


class WishesForm(forms.ModelForm):

    class Meta:
        model = Wish
        fields = ['wish']
        widgets = {
            'wish': forms.TextInput(attrs={'class': 'mt-1'})
        }

    def __init__(self, *args, **kwargs):
        super(WishesForm, self).__init__(*args, **kwargs)
        self.fields['wish'].label = ''
        self.fields['wish'].widget.attrs['placeholder'] = \
            'Подгони по-братски...'


class DescriptionForm(forms.ModelForm):

    class Meta:
        model = Wish
        fields = ['description']
        widgets = {
            'description': forms.TextInput(attrs={'class': 'mt-1'})
        }

    def __init__(self, *args, **kwargs):
        super(DescriptionForm, self).__init__(*args, **kwargs)
        self.fields['description'].label = ''
        self.fields['description'].widget.attrs['placeholder'] = \
                'Хочу такое, чтобы ух какое...'

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
