from django.db import models


class UserLogin(models.Model):
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=20)


class UserRegister(models.Model):
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    confirmPassword = models.CharField(max_length=50)
    address = models.TextField(max_length=256)


class UserRestaurant(models.Model):
    cellPhone = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    profile = models.ImageField(null=True, blank=True, default="default.jpg")
    restaurantName = models.CharField(max_length=50)
    social = models.CharField(max_length=50)
    website = models.CharField(max_length=256)
    address = models.TextField(max_length=256)
