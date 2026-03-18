from django import forms
from .models import Mitigationaction

class MitigationForm(forms.ModelForm):
    class Meta:
        model = Mitigationaction
        fields = ['actiontaken']
        widgets = {
            'actiontaken': forms.Textarea(attrs={'class': 'form-control', 'rows': 4, 'placeholder': 'Describe the steps taken to mitigate this risk...'}),
        }
