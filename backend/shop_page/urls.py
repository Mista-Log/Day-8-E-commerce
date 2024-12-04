from django.urls import path
from . import views



urlpatterns = [
    path('products/', views.ProductListAPIView.as_view(), name='product_list'),
    path('banners/', views.BannerListAPIView.as_view(), name='banner_list'),
]
