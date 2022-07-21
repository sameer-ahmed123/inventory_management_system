from django.contrib.auth import get_user_model
from django.contrib import admin
from recipes.models import Recipe,RecipeIngredient

User =get_user_model()

# Register your models here.
# admin.site.register(RecipeIngredient)


class RecipeIngredientInline(admin.StackedInline):
    model = RecipeIngredient
    extra = 0
    #fields = ['name', 'quantity', 'unit', 'directions', 'active']


class RecipeAdmin(admin.ModelAdmin):
    inlines = [RecipeIngredientInline]
    list_display = ['name', 'user', 'active', 'directions', 'timestamp']
    readonly_fields = ['timestamp']
    raw_id_fields = ["user"]
admin.site.register(Recipe, RecipeAdmin)


