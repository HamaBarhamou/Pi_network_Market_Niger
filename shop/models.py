from django.db import models
from django.contrib.auth import get_user_model
from django.urls import reverse
from django.core.exceptions import ValidationError



class Shop(models.Model):
    name = models.CharField(max_length=50, default=None)
    description = models.TextField(default=None)
    user = models.OneToOneField(get_user_model(), on_delete=models.CASCADE)
    image = models.ImageField(
        verbose_name='image',
        upload_to='shop',
        default=None
    )

    def __str__(self):
        return self.name 


class Category(models.Model):
    name = models.CharField(max_length=50, default=None)
    description = models.TextField(max_length=150, default=None)
    shop = models.ForeignKey(Shop, on_delete=models.CASCADE)
    image = models.ImageField(verbose_name='image', upload_to='shop', null=True)

    def __str__(self):
        return self.name


class Article(models.Model):
    name = models.CharField(max_length=50, default=None)
    description = models.TextField(default=None)
    qte = models.IntegerField()
    price = models.DecimalField(max_digits=7, decimal_places=2)
    image = models.ImageField(verbose_name='image', upload_to='shop', null=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    views_count = models.IntegerField(default=0)
    vendeur = models.ForeignKey(get_user_model(), on_delete=models.CASCADE)

    def __str__(self):
        return self.name
    
    def get_absolute_url(self):
        return reverse('shop:vendeur_detail', args=[str(self.vendeur.id)])
    
    def clean(self):
        if self.qte <= 0:
            raise ValidationError('La quantité doit être supérieure à zéro.')
        if self.price <= 0:
            raise ValidationError('Le prix doit être supérieur à zéro.')
