from django.db import models
from user.models import User

# Create your models here.
class Market(models.Model):
    name = models.CharField(max_length=100, default=None)
    adresse = models.CharField(max_length=100, default=None)
    image = models.ImageField(
                verbose_name='photo de profile',
                upload_to='media'
                )

    def __str__(self):
        return self.name

class Shop(models.Model):
    name = models.CharField(max_length=50, default=None)
    description = models.CharField(max_length=150, default=None)
    market = models.ForeignKey(Market, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.ImageField(verbose_name='image', upload_to='media', null=True)

    def __str__(self):
        return self.name 

class Category(models.Model):
    name = models.CharField(max_length=50, default=None)
    description = models.CharField(max_length=150, default=None)
    shop = models.ManyToManyField(Shop)
    image = models.ImageField(verbose_name='image', upload_to='media', null=True)

    def __str__(self):
        return self.name

class Article(models.Model):
    name = models.CharField(max_length=50, default=None)
    description = models.CharField(max_length=150, default=None)
    qte = models.IntegerField()
    image = models.ImageField(verbose_name='image', upload_to='media', null=True)

    def __str__(self):
        return self.name