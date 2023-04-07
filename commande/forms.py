from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['status', 'total_amount']
        widgets = {
            'status': forms.Select(choices=Order.STATUS_CHOICES),
            'total_amount': forms.NumberInput(attrs={'min': 0})
        }
