from django.db import models

class Publicite(models.Model):
    image = models.ImageField(verbose_name='image', upload_to='publicites')
    description = models.CharField(max_length=255)
    lien = models.URLField()
    duree_diffusion = models.IntegerField(default=7) # Durée de diffusion en jours
    prix = models.DecimalField(max_digits=7, decimal_places=2)

    def __str__(self):
        return self.description
