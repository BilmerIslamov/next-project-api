# Generated by Django 4.2.4 on 2023-08-21 07:08

import autoslug.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Category",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("category_title", models.CharField(max_length=100)),
                (
                    "slug",
                    autoslug.fields.AutoSlugField(
                        editable=True, populate_from="category_title", unique=True
                    ),
                ),
            ],
            options={
                "verbose_name": "Категория",
                "verbose_name_plural": "Категории",
            },
        ),
        migrations.CreateModel(
            name="Navigation",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "navigation_title",
                    models.CharField(
                        max_length=20, verbose_name="навигация по заголовку"
                    ),
                ),
            ],
            options={
                "verbose_name": "Навигация",
                "verbose_name_plural": "Навигации",
            },
        ),
        migrations.CreateModel(
            name="NewsCategory",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("category_title", models.CharField(max_length=50)),
                (
                    "slug",
                    autoslug.fields.AutoSlugField(
                        editable=True, populate_from="category_title", unique=True
                    ),
                ),
            ],
            options={
                "verbose_name": "Категория новостей",
                "verbose_name_plural": "Категории новостей",
            },
        ),
        migrations.CreateModel(
            name="Product",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "product_title",
                    models.CharField(max_length=150, verbose_name="Название продукта"),
                ),
                (
                    "product_price",
                    models.TextField(max_length=50, verbose_name="Цена продукта"),
                ),
                (
                    "product_discount",
                    models.TextField(max_length=50, verbose_name="Скидка на продукт"),
                ),
                (
                    "product_weight",
                    models.TextField(max_length=50, verbose_name="Вес изделия"),
                ),
                (
                    "product_image",
                    models.ImageField(
                        upload_to="media", verbose_name="Изображение продукта"
                    ),
                ),
                ("product_created", models.DateTimeField(auto_now_add=True)),
                (
                    "product_slug",
                    autoslug.fields.AutoSlugField(
                        editable=True, populate_from="news_title", unique=True
                    ),
                ),
                (
                    "product_category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="api.category"
                    ),
                ),
            ],
            options={
                "verbose_name": "Продукт",
                "verbose_name_plural": "Продукты",
            },
        ),
        migrations.CreateModel(
            name="News",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("news_title", models.CharField(max_length=50, verbose_name="")),
                ("news_text", models.TextField(verbose_name="")),
                ("news_image", models.ImageField(upload_to="media", verbose_name="")),
                (
                    "news_video",
                    models.TextField(
                        blank=True, max_length=250, null=True, verbose_name=""
                    ),
                ),
                (
                    "news_video_file",
                    models.FileField(blank=True, null=True, upload_to="video_media"),
                ),
                ("news_created", models.DateTimeField(auto_now_add=True)),
                (
                    "news_slug",
                    autoslug.fields.AutoSlugField(
                        editable=True, populate_from="news_title", unique=True
                    ),
                ),
                (
                    "news_category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="api.newscategory",
                    ),
                ),
            ],
            options={
                "verbose_name": "Новость",
                "verbose_name_plural": "Новости",
            },
        ),
    ]
