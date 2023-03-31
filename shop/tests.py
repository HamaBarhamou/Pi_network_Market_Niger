from django.test import TestCase
from django.contrib.auth import get_user_model
from django.urls import reverse

from .models import Shop, Category, Article


class ShopModelTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpass'
        )
        self.shop = Shop.objects.create(
            name='Test Shop',
            description='Test Shop Description',
            user=self.user,
            image='shop/test.png'
        )

    def test_shop_str(self):
        self.assertEqual(str(self.shop), self.shop.name)

    """ def test_shop_get_absolute_url(self):
        self.assertEqual(self.shop.get_absolute_url(), reverse('shop:vendeur_detail', args=[str(self.user.id)])) """


class CategoryModelTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpass'
        )
        self.shop = Shop.objects.create(
            name='Test Shop',
            description='Test Shop Description',
            user=self.user,
            image='shop/test.png'
        )
        self.category = Category.objects.create(
            name='Test Category',
            description='Test Category Description',
            shop=self.shop,
            image='shop/test.png'
        )

    def test_category_str(self):
        self.assertEqual(str(self.category), self.category.name)


class ArticleModelTest(TestCase):

    def setUp(self):
        self.user = get_user_model().objects.create_user(
            username='testuser',
            email='testuser@example.com',
            password='testpass'
        )
        self.shop = Shop.objects.create(
            name='Test Shop',
            description='Test Shop Description',
            user=self.user,
            image='shop/test.png'
        )
        self.category = Category.objects.create(
            name='Test Category',
            description='Test Category Description',
            shop=self.shop,
            image='shop/test.png'
        )
        self.article = Article.objects.create(
            name='Test Article',
            description='Test Article Description',
            qte=10,
            price=100,
            image='shop/test.png',
            category=self.category,
            vendeur=self.user
        )

    def test_article_str(self):
        self.assertEqual(str(self.article), self.article.name)

    def test_article_get_absolute_url(self):
        self.assertEqual(self.article.get_absolute_url(), reverse('shop:vendeur_detail', args=[str(self.user.id)]))
        
    def test_article_get_absolute_url2(self):
        article = Article.objects.create(
            name="test article",
            description="test description",
            qte=10,
            price=15.99,
            category=self.category,
            vendeur=self.user
        )
        self.assertEqual(article.get_absolute_url(), reverse('shop:vendeur_detail', args=[str(self.user.id)]))
