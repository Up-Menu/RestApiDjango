from django.contrib import admin
from .models import UserLogin, UserRegister, UserRestaurant

admin.site.register(UserLogin)
admin.site.register(UserRegister)
admin.site.register(UserRestaurant)
