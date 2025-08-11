from django.contrib import admin
from django.utils.text import slugify
from .models import Recipe, Category

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug', 'created_at']
    prepopulated_fields = {'slug': ('name',)}
    search_fields = ['name']

@admin.register(Recipe)
class RecipeAdmin(admin.ModelAdmin):
    list_display = ['title', 'category', 'difficulty', 'prep_time', 'cook_time', 'created_at']
    list_filter = ['category', 'difficulty', 'created_at']
    search_fields = ['title', 'description', 'ingredients']
    prepopulated_fields = {'slug': ('title',)}
    list_per_page = 20
    
    fieldsets = (
        ('Basic Information', {
            'fields': ('title', 'slug', 'description', 'category', 'image')
        }),
        ('Recipe Details', {
            'fields': ('ingredients', 'instructions', 'servings', 'difficulty')
        }),
        ('Timing', {
            'fields': ('prep_time', 'cook_time')
        }),
    )