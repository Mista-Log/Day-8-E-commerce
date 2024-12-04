from django.db import models
import uuid

# Create your models here.

class Banner(models.Model):
    title = models.CharField(max_length=255, blank=True, help_text="Optional banner title")
    image = models.ImageField(upload_to='banners/')
    description = models.TextField(blank=True, null=True, help_text="Optional description")

    def __str__(self):
        return self.title
    
class Color(models.Model):
    name = models.CharField(max_length=100, unique=True)


    def __str__(self):
        return self.name
    
    
class Product(models.Model):
    
    CATEGORY = (
        ("Phone & Tablets", "Phone & Tablets"),
        ("Cases & Covers", "Cases & Covers"),
        ("Screen Guards", "Screen Guards"),
        ("Cables & Chargers", "Cables & Chargers"),
        ("Power Banks", "Power Banks"),
        ("Others", "Others"),
    )

    BRAND = (
        ("Apple", "Apple"),
        ("Samsung", "Samsung"),
        ("Google", "Google"),
        ("HTC", "HTC"),
        ("Others", "Others"),
    )

    MANUFACTURER = (
        ("HOCO", "HOCO"),
        ("Nillkin", "Nillkin"),
        ("Remax", "Remax"),
        ("Baseus", "Baseus"),
        ("Others", "Others"),
    )
    STATUS = (
        ("In Stock", "In Stock"),
        ("Out of Stock", "Out of Stock"),
    )



    name = models.CharField(max_length=255, blank=True, help_text="Optional title for the body image")
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    code = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False, unique=True)
    category = models.CharField(max_length=200, null=True, choices=CATEGORY)
    brand = models.CharField(max_length=200, null=True, choices=BRAND)
    manufacturer = models.CharField(max_length=200, null=True, choices=MANUFACTURER)
    color = models.ManyToManyField(Color)
    status = models.CharField(max_length=200, null=True, choices=STATUS)
    image = models.ImageField(upload_to='products/')
    description = models.TextField(max_length=100000, blank=True, help_text="Optional title for the body image")

    def __str__(self):
        return self.name



