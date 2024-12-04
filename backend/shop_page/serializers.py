from rest_framework import serializers
from .models import Product, Banner, Color
from details.serializers import RatingSerializer



class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = '__all__'


class ProductSerializer(serializers.ModelSerializer):
    ratings = RatingSerializer(many=True, read_only=True)
    average_rating = serializers.SerializerMethodField()
    color = ColorSerializer(many=True)


    class Meta:
        model = Product
        fields = '__all__'
    
    def get_average_rating(self, obj):
        ratings = obj.ratings.all()
        if ratings.exists():
            return sum([r.stars for r in ratings]) / ratings.count()
        return None



class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = '__all__'
