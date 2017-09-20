from django import forms
from album.models import Photo


class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = '__all__'