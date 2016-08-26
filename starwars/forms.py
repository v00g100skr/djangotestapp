from django import forms
from .models import Characters


class CharacterForm(forms.Form):
    name = forms.CharField(max_length=48)
    height = forms.CharField(max_length=8)
    mass = forms.CharField(max_length=8)
    hair_color = forms.CharField(max_length=16)
    skin_color = forms.CharField(max_length=16)
    eye_color = forms.CharField(max_length=16)
    birth_year = forms.CharField(max_length=8)
    gender = forms.CharField(max_length=8)
    pic = forms.FileField(
        label='Select a file', required=False
    )


class CharacterItemForm(forms.ModelForm):
    class Meta:
        model = Characters
        fields = ('name', 'height', 'mass', 'hair_color', 'skin_color', 'eye_color', 'birth_year', 'gender', 'pic')