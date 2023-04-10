# Generated by Django 4.1.5 on 2023-04-10 12:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('commande', '0002_order_payment_method'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='payment_method',
            field=models.CharField(choices=[('cash_on_delivery', 'Payer à la livraison'), ('pi_network', 'Payer par Pi Network'), ('credit_card', 'Credit card'), ('paypal', 'PayPal'), ('cash_on_delivery', 'Cash on delivery')], default='cash_on_delivery', max_length=20),
        ),
    ]
