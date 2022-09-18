from django.urls import path
from .views import UserLoginViews, UserRegisterViews, UserRestaurantViews

urlpatterns = [
    path('users', UserLoginViews.as_view()),
    path('register', UserRegisterViews.as_view()),
    path('restaurant', UserRestaurantViews.as_view()),
    path('user/<int:id>', UserLoginViews.as_view())
]
