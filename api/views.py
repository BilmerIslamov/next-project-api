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
        news_ = News.objects.filter(news_slug=news_slug)
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
        new = Product.objects.filter(product_slug=product_slug)
        serializer = ProductSeralizers(new, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def get_product_id(request, product_id):
    if request.method == 'GET':
        new = Product.objects.all().filter(pk=product_id)
        serializer = ProductSeralizers(new, many=True)
        return Response(serializer.data)








@api_view(['GET'])
def news_category_id(request, category_id):
    if request.method == "GET":
        try:
            category_view = NewsCategory.objects.get(pk=category_id)
            news_view = News.objects.filter(news_category=category_id)

            category_serializer = NewsCategorySerializer(category_view)
            product_serializer = NewsSerializer(news_view, many=True)

            response_data = {
                'category': category_serializer.data,
                'news': product_serializer.data
            }

            return Response(response_data)
        except Category.DoesNotExist:
            return Response({'error': 'Category not found'}, status=404)

@api_view(['GET'])
def product_category_id(request, category_id):
    if request.method == "GET":
        try:
            category_view = Category.objects.get(pk=category_id)
            product_view = Product.objects.filter(product_category_id=category_id)

            category_serializer = CategorySeralizers(category_view)
            product_serializer = ProductSeralizers(product_view, many=True)

            response_data = {
                'category': category_serializer.data,
                'products': product_serializer.data
            }

            return Response(response_data)
        except Category.DoesNotExist:
            return Response({'error': 'Category not found'}, status=404)