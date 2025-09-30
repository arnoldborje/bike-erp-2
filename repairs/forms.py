from django import forms
from .models import Repair

class RepairForm(forms.ModelForm):
    class Meta:
        model = Repair
        fields = ['bike', 'description', 'cost', 'status']
        widgets = {
            'bike': forms.Select(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'cost': forms.NumberInput(attrs={'class': 'form-control'}),
            'status': forms.Select(attrs={'class': 'form-control'}),
        }