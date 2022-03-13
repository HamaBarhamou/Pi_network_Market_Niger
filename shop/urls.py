# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    urls.py                                            :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: bissaka- <bissaka-@student.s19.be>         +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2022/01/31 18:10:03 by bissaka-          #+#    #+#              #
#    Updated: 2022/02/02 00:17:54 by bissaka-         ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from django.urls import path
from . import views
from shop.views import categories, ft_article_detaille#,article

urlpatterns = [
    #path('', views.index, name='index'),
    path('contacter', views.ft_NousContacter, name='ContacteNous'),
    path('merci', views.ft_Merci, name='merci'),
    path('', categories.as_view(),name='index'),
    #path('<int:pk>/article',article.as_view(),name='article'),
    path('<int:pk_categorie>/article',views.ft_article,name='article'),
    path('<int:pk_categorie>/article/<int:pk_article>',views.ft_article_detaille,name='articleDetaille')
]
