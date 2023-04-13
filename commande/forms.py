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
        
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super().__init__(*args, **kwargs)
        if user.fonction == 3:
            self.fields['status'].choices = [('confirmed', 'Confirmée')]
            self.initial['status'] = 'confirmed'
        else:
            self.fields['status'].choices = [(s, s.capitalize()) for s in Order.STATUS_CHOICES if s not in ('pending', 'confirmed')]


class PaymentForm(forms.Form):
    PAYMENT_CHOICES = [
        ('cash_on_delivery', 'Payer à la livraison'),
        ('pi_network', 'Payer par Pi Network'),
        ('credit_card', 'Credit card'),
        ('paypal', 'PayPal'),
        ('cash_on_delivery', 'Cash on delivery'),
    ]
    payment = forms.ChoiceField(choices=PAYMENT_CHOICES, widget=forms.RadioSelect())