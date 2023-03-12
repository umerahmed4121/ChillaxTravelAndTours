from django import forms
from .models import *

class ImageForm(forms.Form):

    required_css_class = 'tour_input tour_input_From'
    images = forms.FileField(widget=forms.ClearableFileInput(attrs={'multiple': True,}),required=False)
