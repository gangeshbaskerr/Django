from django.contrib import admin
from .models import FoodItem

class FoodItemAdmin(admin.ModelAdmin):
    list_display = ('name', 'food_type', 'vitamin_present')
    list_filter = ('food_type',)
    search_fields = ('name',)

    ordering = ['vitamin_present', 'name']

admin.site.register(FoodItem, FoodItemAdmin)
