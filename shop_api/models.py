from django.db import models
from users.models import User

# Create your models here.


class Category(models.Model):
    category_name = models.CharField(max_length=50, verbose_name='Категории')


class Product(models.Model):
    product_name = models.CharField(max_length=100, verbose_name='Товар')
    category = models.ForeignKey(Category, related_name='products', verbose_name='Категория', on_delete=models.PROTECT)
    image = models.ImageField(verbose_name='Фотография', upload_to='product/')
    url = models.CharField(max_length=300, verbose_name='Ссылка')


class Order(models.Model):
    user = models.ForeignKey(User, related_name='orders', verbose_name='Пользователь', on_delete=models.PROTECT)
    products = models.ManyToManyField(Product, related_name='products', verbose_name='Продукты')
    created_date = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    total_price = models.IntegerField(verbose_name='Цена')
