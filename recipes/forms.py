from django import forms
from .models import Recipe

class RecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ['title', 'cooking_time', 'description', 'img']
        widgets = {
            'description': forms.Textarea(attrs={'rows': 6}),
        }

