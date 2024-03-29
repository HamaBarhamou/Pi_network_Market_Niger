from django.db import models
from django.contrib.auth import get_user_model
from shop.models import Article
from panier.models import Cart

class Order(models.Model):
    STATUS_CHOICES = [
        ('pending', 'En attente'),
        ('confirmed', 'Confirmée'),
        ('shipped', 'Expédiée'),
        ('delivered', 'Livrée'),
        ('cancelled', 'Annulée')
    ]
    
    PAYMENT_METHOD_CHOICES = [
        ('cash_on_delivery', 'Payer à la livraison'),
        ('pi_network', 'Payer par Pi Network'),
        ('credit_card', 'Credit card'),
        ('paypal', 'PayPal'),
        ('cash_on_delivery', 'Cash on delivery'),
    ]

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=STATUS_CHOICES, default='pending', max_length=20)
    total_amount = models.DecimalField(max_digits=7, decimal_places=2)
    payment_method = models.CharField(choices=PAYMENT_METHOD_CHOICES, default='cash_on_delivery', max_length=20)
    # Date d'expédition de la commande
    shipped_at = models.DateTimeField(null=True, blank=True)
    # Date de livraison de la commande
    delivered_at = models.DateTimeField(null=True, blank=True)
    # Identifiant de suivi de la commande
    tracking_id = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self):
        return f"Commande {self.id} de {self.user.username}"
    
    def get_total_cost(self):
        total_cost = sum(item.qte * item.article.price for item in self.orderitem_set.all())
        return total_cost



class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    qte = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.qte} x {self.article.name} dans la commande {self.order.id}"
