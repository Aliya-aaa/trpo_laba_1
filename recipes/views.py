from django.shortcuts import render, redirect, get_object_or_404
from .models import Recipe, Ingredient
from django.contrib.auth.decorators import login_required
from .forms import RecipeForm


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
        ingredients = Ingredient.objects.filter(name__icontains=query)
        recipe_ids = set()
        for ingredient in ingredients:
            for ri in ingredient.recipeingredient_set.all():
                recipe_ids.add(ri.recipe.id)
        recipes = Recipe.objects.filter(id__in=recipe_ids)
    return render(request, 'recipes/recipe_list.html', {'recipes': recipes, 'search_query': query})


@login_required
def recipe_create(request):
    if request.method == 'POST':
        form = RecipeForm(request.POST, request.FILES)
        if form.is_valid():
            recipe = form.save(commit=False)
            recipe.author = request.user
            recipe.save()
            return redirect('recipe_detail', recipe_id=recipe.id)
    else:
        form = RecipeForm()
    return render(request, 'recipes/recipe_form.html', {'form': form})
