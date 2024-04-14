from django.contrib import admin
from recipes.models import Recipe
from recipes.models import Category

class CategoryAdmin(admin.ModelAdmin):
    list_display = ("id","name")
    
class RecipesAdmin(admin.ModelAdmin):
    list_display = ("title","description","slug","preparation_time","preparation_time_unit","servings","servings_unit","preparation_step","preparation_step_is_html","created_at","updated_at","is_published","cover","category","author",)

admin.site.register(Recipe, RecipesAdmin)
admin.site.register(Category, CategoryAdmin)