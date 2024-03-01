from django import forms
from .models import Template, DataSet

class TestForm(forms.Form):
    template = forms.ModelChoiceField(queryset=Template.objects.all())
    data_set = forms.ModelChoiceField(queryset=DataSet.objects.all())
