from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .models import *
from .serializers import *
from rest_framework import viewsets
from .models import News, NewsCategory
from .serializers import NewsSerializer, NewsCategorySerializer
from rest_framework import generics
from .models import News
from .serializers import NewsSerializer
from django.shortcuts import get_object_or_404

@api_view(['GET'])
def router(request):
    routes = [
        {
            "1": "all-navigation/",
            "2": "all-category-news/",
            "3": "all-news/",
            "4": "all-product-category/",
            "5": "all-product/",
            "6": "",
        },
    ]
    return Response(routes)


@api_view(['GET'])
def navigation(request):
    if request.method == 'GET':
        navigation_ = Navigation.objects.all()
        serializer = NavigatsionSeralizers(navigation_, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def news_category(request):
    if request.method == 'GET':
        news_category_ = NewsCategory.objects.all()
        serializer = NewsCategorySerializer(news_category_, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def news(request):
    if request.method == 'GET':
        news_ = News.objects.all()
        serializer = NewsSerializer(news_, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def product_category(request):
    if request.method == 'GET':
        category = Category.objects.all()
        serializer = CategorySeralizers(category, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def product(request):
    if request.method == 'GET':
        product_ = Product.objects.all()
        serializer = ProductSeralizers(product_, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def get_news_id(request, news_slug):
    if request.method == 'GET':
        news_ = News.objects.all().filter(news_slug=news_slug)
        serializer = NewsSerializer(news_, many=True)
    return Response(serializer.data)


class NewsList(generics.ListCreateAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer


class NewsDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

    def get_object(self):
        queryset = self.get_queryset()
        slug = self.kwargs.get('slug')
        return get_object_or_404(queryset, news_slug=slug)
