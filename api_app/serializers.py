from rest_framework import serializers
from .models import UserLogin, UserRegister, UserRestaurant


class UserLoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(max_length=20)
    password = serializers.CharField(max_length=20)

    class Meta:
        model = UserLogin
        fields = ('__all__')


class UserRegisterSerializer(serializers.ModelSerializer):
    firstName = serializers.CharField(max_length=50)
    lastName = serializers.CharField(max_length=50)
    email = serializers.EmailField(max_length=50)
    password = serializers.CharField(max_length=50)
    confirmPassword = serializers.CharField(max_length=50)
    address = serializers.CharField(max_length=256)

    class Meta:
        model = UserRegister
        fields = ('__all__')


class UserRestaurantSerializer(serializers.ModelSerializer):
    address = serializers.CharField(max_length=256)
    cellPhone = serializers.CharField(max_length=50)
    email = serializers.EmailField(max_length=50)
    profile = serializers.ImageField()
    restaurantName = serializers.CharField(max_length=50)
    social = serializers.CharField(max_length=50)
    website = serializers.CharField(max_length=256)

    class Meta:
        model = UserRestaurant
        fields = ('__all__')
