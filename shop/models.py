# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    models.py                                          :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: bissaka- <bissaka-@student.s19.be>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/01/31 18:11:45 by bissaka-          #+#    #+#              #
#    Updated: 2022/01/31 18:11:48 by bissaka-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from django.db import models

# Create your models here.

class Categories(models.Model):
    nom = models.CharField(max_length=200)
    image=models.ImageField()

    def __str__(self):
        return self.nom

class Articles(models.Model):
    categories = models.ForeignKey(Categories, on_delete=models.CASCADE)
    nom = models.CharField(max_length=200)
    prix=models.IntegerField()
    image=models.ImageField()
    qte=models.IntegerField()

    def __str__(self):
        return self.nom
    