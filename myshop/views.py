# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    views.py                                           :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: bissaka- <bissaka-@student.s19.be>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/02/02 11:17:57 by bissaka-          #+#    #+#              #
#    Updated: 2022/02/02 12:04:43 by bissaka-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from django.http import HttpResponseRedirect

def ft_acceuille(request):
    
    return HttpResponseRedirect('shop')
