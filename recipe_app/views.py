from django.shortcuts import render
from recipe_app.models import Recipe, Author
# Create your views here.


def home(request):
    recipes = Recipe.objects.all()

    return render(request, "home.html", context={"recipes": recipes})


def recipe_detailed(request, recipe_id):
    recipe = Recipe.objects.filter(id=recipe_id).first()
    return render(request, "recipe_details.html",
                  context={"recipe_id": recipe_id, "recipe": recipe})


def author_detailed(request, author_id):
    recipes = Recipe.objects.all()
    author_recipes = (
        recipe for recipe in recipes if recipe.author.id == author_id)
    author = Author.objects.filter(id=author_id).first()
    return render(request, "author_details.html",
                  context={"author": author, "author_recipes": author_recipes})
