from django.db import models
from autoslug import AutoSlugField
from django.utils.text import slugify
from django.urls import reverse


# model navigation

class Navigation(models.Model):
    navigation_title = models.CharField(max_length=20, verbose_name="навигация по заголовку")

    def __str__(self):
        return self.navigation_title

    class Meta:
        verbose_name = "Навигация"
        verbose_name_plural = "Навигации"


# model news

class NewsCategory(models.Model):
    category_title = models.CharField(max_length=50)
    slug = AutoSlugField(unique=True, populate_from='category_title', editable=True)

    def str(self):
        return self.category_title

    class Meta:
        verbose_name = "Категория новостей"
        verbose_name_plural = "Категории новостей"


class News(models.Model):
    news_title = models.CharField(max_length=50, verbose_name="")
    news_text = models.TextField(verbose_name="")
    news_category = models.ForeignKey(NewsCategory, on_delete=models.CASCADE)
    news_image = models.ImageField(upload_to="media/photo/news/", verbose_name="")
    news_video = models.TextField(max_length=250, verbose_name="", null=True, blank=True)
    news_video_file = models.FileField(upload_to='media/video/news', blank=True, null=True)
    news_created = models.DateTimeField(auto_now_add=True)
    news_slug = AutoSlugField(unique=True, populate_from='news_title', editable=True)

    def str(self):
        return self.news_title

    class Meta:
        verbose_name = "Новость"
        verbose_name_plural = "Новости"


# model product


class Category(models.Model):
    category_title = models.CharField(max_length=100, )
    slug = AutoSlugField(unique=True, populate_from='category_title', editable=True)

    def __str__(self):
        return self.category_title

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"


class Product(models.Model):
    product_title = models.CharField(max_length=150, verbose_name="Название продукта")
    product_price = models.TextField(max_length=50, verbose_name="Цена продукта")
    product_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    product_discount = models.TextField(max_length=50, verbose_name="Скидка на продукт")
    product_weight = models.TextField(max_length=50, verbose_name="Вес изделия")
    product_image = models.ImageField(upload_to="media/photo/product/", verbose_name="Изображение продукта")
    product_created = models.DateTimeField(auto_now_add=True)
    product_slug = AutoSlugField(unique=True, populate_from='news_title', editable=True)

    def __str__(self):
        return self.product_title

    class Meta:
        verbose_name = 'Продукт'
        verbose_name_plural = 'Продукты'
