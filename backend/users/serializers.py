# from django.contrib.auth.models import User
# from rest_framework import serializers
# from django.contrib.auth.hashers import make_password
# from django.contrib.auth import get_user_model



# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model= User
#         fields = ["id", "username", "password"]
#         extra_kwargs = {"password": {"write_only": True}}

#         def create(self, validated_data):
#             user = User.objects.create_user(**validated_data)
#             user.is_active = True
#             user.save()
#             return user