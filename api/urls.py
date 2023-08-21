from django.urls import path
from .views import *
from django.urls import path
from .views import NewsList, NewsDetail

urlpatterns = [
    path('', router, name="pur api"),
    path('all-navigation/', navigation, name="get_navigation"),
    path('all-category-news/', news_category, name="news_category"),
    path('all-news/', news, name="news_name"),
    path('all-product-category/', product_category, name="product_category"),
    path('all-product/', product, name="product_name"),
    path('get-news-id/<str:news_slug>/', get_news_id, name="get-news-id/"),
    path('news/', NewsList.as_view(), name='news-list'),
    path('news/<slug:news_slug>/', NewsDetail.as_view(), name='news-detail')
]
