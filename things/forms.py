"""Forms of the project."""

# Create your forms here.

from django import forms
from django.core.exceptions import ValidationError
from .models import Thing

class ThingForm(forms.ModelForm):
#     """Form of the project."""

    class Meta:
        """Meta class of the form."""
        model = Thing
        # The description field must be displayed as a Textarea. The quantity field must be displayed as NumberInput.

        fields = ['name', 'description', 'quantity']

        widgets = {
            'description': forms.Textarea,
            'quantity': forms.NumberInput
        }


