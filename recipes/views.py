from django.shortcuts import render, get_object_or_404
from django.db.models import Q
from .models import Recipe, Category

def recipe_list(request):
    recipes = Recipe.objects.all()
    categories = Category.objects.all()
    
    # Get filter parameters
    category_filter = request.GET.get('category')
    difficulty_filter = request.GET.get('difficulty')
    search_query = request.GET.get('search')
    sort_by = request.GET.get('sort', 'newest')
    
    # Apply filters
    if category_filter:
        recipes = recipes.filter(category__slug=category_filter)
    
    if difficulty_filter:
        recipes = recipes.filter(difficulty=difficulty_filter)
    
    if search_query:
        recipes = recipes.filter(
            Q(title__icontains=search_query) |
            Q(description__icontains=search_query) |
            Q(ingredients__icontains=search_query)
        )
    
    # Apply sorting
    if sort_by == 'prep_time':
        recipes = recipes.order_by('prep_time')
    elif sort_by == 'total_time':
        recipes = recipes.order_by('prep_time', 'cook_time')
    elif sort_by == 'difficulty':
        recipes = recipes.order_by('difficulty', 'prep_time')
    elif sort_by == 'title':
        recipes = recipes.order_by('title')
    else:  # newest (default)
        recipes = recipes.order_by('-created_at')
    
    context = {
        'recipes': recipes,
        'categories': categories,
        'current_category': category_filter,
        'current_difficulty': difficulty_filter,
        'search_query': search_query,
        'current_sort': sort_by,
        'difficulty_choices': Recipe.DIFFICULTY_CHOICES,
    }
    
    return render(request, 'recipes/recipe_list.html', context)

def recipe_detail(request, slug):
    recipe = get_object_or_404(Recipe, slug=slug)
    related_recipes = Recipe.objects.filter(category=recipe.category).exclude(id=recipe.id)[:3]
    
    context = {
        'recipe': recipe,
        'related_recipes': related_recipes,
    }
    
    return render(request, 'recipes/recipe_detail.html', context)