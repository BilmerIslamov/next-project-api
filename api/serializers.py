from rest_framework.serializers import ModelSerializer
from .models import *


class NewsSerializer(ModelSerializer):
    class Meta:
        model = News
        fields = '__all__'


class NavigatsionSeralizers(ModelSerializer):
    class Meta:
        model = Navigation
        fields = "__all__"


class NewsCategorySerializer(ModelSerializer):
    class Meta:
        model = NewsCategory
        fields = '__all__'


class NewsArticleSerializer(ModelSerializer):
    class Meta:
        model = NewsCategory
        fields = ('category_title', 'slug')


# class NewsSerializer(ModelSerializer):
#     news_category = NewsArticleSerializer()
#
#     class Meta:
#         model = News
#         fields = '__all__'


class CategorySeralizers(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSeralizers(ModelSerializer):
    product_category = CategorySeralizers()

    class Meta:
        model = Product
        fields = '__all__'
