from django.urls import path
from . import views



urlpatterns = [
    path("ratings/", views.RatingViewSet.as_view())
]

