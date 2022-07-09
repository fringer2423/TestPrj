from django.contrib import admin
from .models import Food, FoodCategory

admin.site.register(Food)


class Foods(admin.StackedInline):
    model = Food
    fields = ['name_ru', 'is_publish']
    extra = 1


@admin.register(FoodCategory)
class FoodCategoryAdmin(admin.ModelAdmin):
    list_display = ['name_ru']
    fields = ['name_ru', 'name_en', 'name_ch', 'order_id']
    inlines = [Foods]
