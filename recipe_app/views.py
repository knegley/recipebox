from django.shortcuts import render, HttpResponseRedirect, reverse
from recipe_app.models import Recipe, Author
from recipe_app.forms import AddAuthorForm, AddRecipeForm, LoginForm, SignUpForm
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.admin.views.decorators import staff_member_required
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


def signup_view(request):
    if request.method == "POST":
        form = SignUpForm(request.POST)
        data = form.cleaned_data
        new_user = User.objects.create_user(username=data.get(
            "username"), password=data.get("password"))
        login(request, new_user)
        return HttpResponseRedirect(reverse("recipe_home"))
    form = SignUpForm()
    return render(request, "generic_form.html", {"form": form})


@staff_member_required
def add_author(request):
    form = AddAuthorForm()
    if request.method == "POST":
        form = AddAuthorForm(request.POST)

    if form.is_valid():
        data = form.cleaned_data
        Author.objects.create(
            name=data.get("name"),
            bio=data.get("bio")
        )
        return HttpResponseRedirect(reverse("recipe_home"))

    return render(request, "generic_form.html", {"form": form})


@login_required
def add_recipe(request):
    form = AddRecipeForm()
    # print(dir(request))
    if request.method == "POST":
        form = AddRecipeForm(request.POST)
    if form.is_valid():
        data = form.cleaned_data
        Recipe.objects.create(
            title=data.get("title"),
            author=request.user.author,
            description=data.get("description"),
            time_required=data.get("time_required"),
            instructions=data.get("instructions")
        )
        return HttpResponseRedirect(reverse("recipe_home"))

    return render(request, "generic_form.html", {"form": form})


def login_view(request):
    if request.method == "POST":
        form = LoginForm(request.POST)

        if form.is_valid:

            data = request.POST
            # print(data)
            user = authenticate(request, username=data.get(
                "username"), password=data.get("password"))

            if user:
                login(request, user)

                return HttpResponseRedirect(redirect_to=request.GET.get("next", reverse("recipe_home")))
    form = LoginForm()
    return render(request, "generic_form.html", {"form": form})


def logout_view(request):
    logout(request)
    return HttpResponseRedirect(reverse("recipe_home"))
