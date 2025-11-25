from django.db import models


class Ingredient(models.Model):
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Recipe(models.Model):
    title = models.CharField(max_length=200)
    cooking_time = models.PositiveIntegerField(help_text="В минутах")
    description = models.TextField()
    img = models.ImageField(upload_to='recipes/', blank=True, null=True)

    def __str__(self):
        return self.title


class RecipeIngredient(models.Model):
    recipe = models.ForeignKey(Recipe, on_delete=models.CASCADE, related_name='recipe_ingredients')
    ingredient = models.ForeignKey(Ingredient, on_delete=models.CASCADE)
    unit = models.CharField(max_length=50)
    quantity = models.FloatField()

    def __str__(self):
        return f"{self.quantity} {self.unit} {self.ingredient.name}"
