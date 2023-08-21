from rest_framework.generics import RetrieveDestroyAPIView
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import *
from .models import News, NewsCategory


@api_view(['GET'])
def router(request):
    router_ = [
        {
            "all-navigation/",
            "all-category-news/",
            "all-news/",
            "all-product-category/",
            "all-product/",
            "get-news-name/",
            "all-category-news/news_slug",
            "get-news-id/id",
            "all-category-news/",
        }
    ]
    return Response(router_)


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
def get_news_name(request, news_slug):
    if request.method == 'GET':
        news_ = News.objects.all().filter(news_slug=news_slug)
        serializer = NewsSerializer(news_, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def get_news_id(request, pk):
    if request.method == 'GET':
        news_ = News.objects.all().filter(pk=pk)
        serializer = NewsSerializer(news_, many=True)
        return Response(serializer.data)


@api_view(['GET'])
def get_product_name(request, product_slug):
    if request.method == 'GET':
        new = Product.objects.all().filter(slug=product_slug)
        serializer = ProductSeralizers(new, many=True)
        return Response(serializer.data)


#
#
@api_view(['GET'])
def get_product_id(request, product_id):
    if request.method == 'GET':
        new = Product.objects.all().filter(pk=product_id)
        serializer = ProductSeralizers(new, many=True)
        return Response(serializer.data)

