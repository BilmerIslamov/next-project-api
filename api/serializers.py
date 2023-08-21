from rest_framework.serializers import ModelSerializer, SerializerMethodField
from .models import *


# class NewsSerializer(ModelSerializer):
#     class Meta:
#         model = News
#         fields = '__all__'


class NavigatsionSeralizers(ModelSerializer):
    class Meta:
        model = Navigation
        fields = ('id', 'navigation_title')


class NewsCategorySerializer(ModelSerializer):
    class Meta:
        model = NewsCategory
        fields = ('id', 'category_title', 'slug')


class NewsArticleSerializer(ModelSerializer):
    class Meta:
        model = NewsCategory
        fields = ('id', 'slug',)

class NewsSerializer(ModelSerializer):
    news_category = NewsArticleSerializer()

    class Meta:
        model = News
        fields = ("id", "news_slug", "news_title", "news_text", "news_image_url", "news_video_url", "news_video", "news_category", "news_created",)

    news_image_url = SerializerMethodField()

    def get_news_image_url(self, obj):
        return f"http://127.0.0.1:8000/next_api{obj.news_image.url}"

    news_video_url = SerializerMethodField()

    def get_news_video_url(self, obj):
        return f"http://127.0.0.1:8000/next_api{obj.news_video_file.url}"





class CategorySeralizers(ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ProductSeralizers(ModelSerializer):
    product_category = CategorySeralizers()

    class Meta:
        model = Product
        fields = '__all__'

