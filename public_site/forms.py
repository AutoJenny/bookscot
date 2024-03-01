from django import forms
from .models import ContactEntry

class ContactEntryForm(forms.ModelForm):
    class Meta:
        model = ContactEntry
        fields = ['forename', 'email', 'message']  # Adjust fields as needed
