# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    forms.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: bissaka- <bissaka-@student.s19.be>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/01/31 20:19:25 by bissaka-          #+#    #+#              #
#    Updated: 2022/01/31 20:19:26 by bissaka-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

import email
from django import forms

class NousContacter(forms.Form):
    nom = forms.CharField(label='Votre nom', max_length=100)
    prenom = forms.CharField(label='Votre prenom', max_length=100)
    message = forms.CharField(widget=forms.Textarea)
    email = forms.EmailField(label='adresse email')
    