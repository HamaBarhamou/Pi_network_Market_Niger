# Generated by Django 4.1.5 on 2023-04-07 14:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_cart_cartitem'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cartitem',
            name='article',
        ),
        migrations.RemoveField(
            model_name='cartitem',
            name='cart',
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.DeleteModel(
            name='CartItem',
        ),
    ]
