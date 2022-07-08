from django.db.models import Prefetch

from apps.core.models import FoodCategory, Food


def get_food_category_list():
    """
    Функция, которая вернет список категорий по заданным правилам:
    - Категории без товаров не выводятся
    - В списке товаров каждой категории присутствуют только товары, у которых is_published True
    """
    foods = Prefetch('food', queryset=Food.objects.filter(is_publish=True).prefetch_related('additional'))
    categories_list = FoodCategory.objects.filter(food__isnull=False).distinct().prefetch_related(foods)

    return categories_list
