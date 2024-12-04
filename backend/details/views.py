from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .models import Rating
from .serializers import RatingSerializer

# Create your views here.

class RatingViewSet(ModelViewSet):
    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
