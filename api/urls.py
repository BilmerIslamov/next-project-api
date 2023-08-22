from .views import *
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
urlpatterns = [
    path('all-navigation/', navigation, name="get_navigation"),
    path('all-category-news/', news_category, name="news_category"),
    path('all-news/', news, name="news_name"),
    path('all-product-category/', product_category, name="product_category"),
    path('all-product/', product, name="product_name"),
    path('get-news-name/<slug:news_slug>/', get_news_name, name="get-news-name"),
    path('get-news-id/<int:pk>/', get_news_id, name='get-news-id'),
    path('get-product-name/<slug:product_slug>/', get_product_name, name="get-news-name"),
    path('get-product-id/<int:product_id>/', get_product_id, name="get-news-name"),


    path('get-product-category-id/<int:category_id>/', product_category_id, name="get-product-category-id"),
    path('get-news-category-id/<int:category_id>/', news_category_id, name="get-product-category-id"),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
