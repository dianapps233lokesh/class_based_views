from django import forms
from .models import GeeksModel

class GeeksForm(forms.ModelForm):
    model=GeeksModel
    fields=['title','description']