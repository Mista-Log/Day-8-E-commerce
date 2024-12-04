from django.db import models
from shop_page.models import Product


class Rating(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name="ratings")
    stars = models.PositiveSmallIntegerField()

