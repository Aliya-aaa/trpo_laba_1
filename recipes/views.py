from django.shortcuts import render, get_object_or_404
from .models import Recipe, Ingredient


def recipe_list(request):
    recipes = Recipe.objects.all()
    return render(request, 'recipes/recipe_list.html', {'recipes': recipes})


def recipe_detail(request, recipe_id):
    recipe = get_object_or_404(Recipe, id=recipe_id)
    return render(request, 'recipes/recipe_detail.html', {'recipe': recipe})


def about(request):
    return render(request, 'recipes/about.html')


def search_by_ingredient(request):
    query = request.GET.get('q', '').strip()
    recipes = []
    if query:
        # Находим ингредиенты, содержащие запрос (регистронезависимо)
        ingredients = Ingredient.objects.filter(name__icontains=query)
        # Находим рецепты, связанные с этими ингредиентами
        recipe_ids = set()
        for ingredient in ingredients:
            for ri in ingredient.recipeingredient_set.all():
                recipe_ids.add(ri.recipe.id)
        recipes = Recipe.objects.filter(id__in=recipe_ids)
    return render(request, 'recipes/recipe_list.html', {'recipes': recipes, 'search_query': query})
