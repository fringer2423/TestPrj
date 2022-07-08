from rest_framework.views import APIView
from rest_framework.response import Response

from .serializers import FoodListSerializer
from .services.food_service import get_food_category_list


class FoodsList(APIView):
    """Контроллер для вывода списка категорий"""
    def get(self, request):
        categories_list = get_food_category_list()
        serializer = FoodListSerializer(categories_list, many=True)
        return Response(serializer.data)
