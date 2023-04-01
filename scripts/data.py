import pathlib
from django.contrib.auth import get_user_model
from django.core.files import File
from django.core.files.images import ImageFile
from django.utils.text import slugify
from faker import Faker
from django.conf import settings
import os
from shop.models import Shop, Category, Article
from user.models import User


BASE_DIR = settings.BASE_DIR
image_path1 = pathlib.Path(BASE_DIR) / 'scripts' / 'shop-image-default.png'
image_path2 = pathlib.Path(BASE_DIR) / 'scripts' / 'default-store.jpg'

# suppression des objets existants
Article.objects.all().delete()
Category.objects.all().delete()
Shop.objects.all().delete()
User.objects.all().delete()

# création de données fictives
fake = Faker()

# création des utilisateurs
User = get_user_model()

users = []
for i in range(5):
    username = fake.user_name()
    email = fake.email()
    password = 'Jaimelep0ulet'
    fonction = 2
    user = User.objects.create_user(username=username, email=email, password=password, fonction=fonction)
    users.append(user)

# création de magasins pour chaque utilisateur
shops = []
for user in users:
    name = fake.company()
    description = fake.text()
    shop = Shop.objects.create(name=name, description=description, user=user)
    shops.append(shop)

# création de catégories pour chaque magasin
categories = []
for shop in Shop.objects.all():
    for i in range(10):
        name = fake.word()
        description = fake.text()
        image_path1 = os.path.abspath(image_path1)
        #image = ImageFile(open(image_path1, 'rb'))
        category = Category.objects.create(
            name=name,
            description=description,
            shop=shop,
            #image=image
        )
        categories.append(category) # Ajout de la catégorie créée à la liste

# création d'articles pour chaque catégorie
for category in categories:
    for i in range(10):
        name = fake.word()
        description = fake.text()
        qte = fake.random_int(min=1, max=1000)
        price = fake.random_int(min=100, max=10000)
        image_path2 = os.path.abspath(image_path2)
        #image = ImageFile(open(image_path2, 'rb'))
        article = Article.objects.create(
                    name=name,
                    description=description,
                    qte=qte,
                    price=price,
                    #image=image,
                    category=category,
                    vendeur=category.shop.user
                    )

# lancer le script
# python manage.py runscript scripts.data.py -v2
