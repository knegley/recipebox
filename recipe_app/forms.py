from django import forms
from recipe_app.models import Recipe, Author


class AddAuthorForm(forms.ModelForm):
    class Meta:
        model = Author
        fields = ["name", "bio"]


class AddRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ["title", "author", "description",
                  "time_required", "instructions"]
