from django.urls import path
from .views import FoodsList

urlpatterns = [
    path('foods', FoodsList.as_view()),
]
