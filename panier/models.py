from django.db import models
from django.contrib.auth import get_user_model
from shop.models import Article
from django.core.exceptions import ValidationError


# Create your models here.
class Cart(models.Model):
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Cart of {self.user.username}"
    
    def clear_cart(self):
        self.cartitem_set.all().delete()
    

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, on_delete=models.CASCADE)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    qte = models.IntegerField(default=1)

    def __str__(self):
        return f"{self.qte} x {self.article.name} in cart of {self.cart.user.username}"
    
    def clean(self):
        if self.qte < 1:
            raise ValidationError('La quantité doit être supérieure à zéro.')