
from django import forms

class RunSetForm(forms.Form):
    group   = forms.CharField(max_length=64)
    machine = forms.CharField(max_length=64)
    phase   = forms.CharField(max_length=64)
    # stem    = forms.CharField(max_length=3*64+2)