from django.shortcuts import render
from rest_framework.response import Response
from .models import Product, Banner
from .serializers import ProductSerializer, BannerSerializer
from rest_framework.views import APIView


# Create your views here.
class ProductListAPIView(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)



class BannerListAPIView(APIView):
    def get(self, request):
        banner = Banner.objects.all()
        serializer = BannerSerializer(banner, many=True)
        return Response(serializer.data)



