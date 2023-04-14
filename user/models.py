from django.db import models
from django.contrib.auth.models import AbstractUser
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.
class User(AbstractUser):
    USER_TYPE_CHOICES = (
      (2, 'Vendor'),
      (3, 'Customer'),
      (4, 'Deliveryman')
    )

    fonction = models.PositiveSmallIntegerField(choices=USER_TYPE_CHOICES, null=True, default=3)
    avatar = models.ImageField(verbose_name='photo de profile', upload_to='avatar')
    #phone_number = models.CharField(verbose_name='Numéro de téléphone', max_length=15)
    phone_number = PhoneNumberField(blank=True, verbose_name='Numéro de téléphone')

    def __str__(self):
        fonction = ""
        for loop in self.USER_TYPE_CHOICES:
            if loop[0] == self.fonction:
                fonction = loop[1]
                break
        return "{} : {}".format(self.username, fonction)
