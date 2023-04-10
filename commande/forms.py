from django import forms
from .models import Order


class OrderForm(forms.ModelForm):
    class Meta:
        model = Order
        fields = ['status', 'total_amount']
        widgets = {
            'status': forms.Select(choices=Order.STATUS_CHOICES),
            'total_amount': forms.NumberInput(attrs={'min': 0}),
        }

class PaymentForm(forms.Form):
    PAYMENT_CHOICES = [
        ('cash_on_delivery', 'Payer à la livraison'),
        ('pi_network', 'Payer par Pi Network'),
        ('credit_card', 'Credit card'),
        ('paypal', 'PayPal'),
        ('cash_on_delivery', 'Cash on delivery'),
    ]
    payment = forms.ChoiceField(choices=PAYMENT_CHOICES, widget=forms.RadioSelect())