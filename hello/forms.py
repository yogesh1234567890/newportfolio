from django import forms
from hello.models import Photos

class PhotoForm(forms.ModelForm):
    class Meta:
        model = Photos
        fields=['logo_image','first_image','second_image']