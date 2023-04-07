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

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=STATUS_CHOICES, default='pending', max_length=20)
    total_amount = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return f"Commande {self.id} de {self.user.username}"

class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    qte = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.qte} x {self.article.name} dans la commande {self.order.id}"
