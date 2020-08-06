from django.urls import path
from recipe_app import views

urlpatterns = [
    path("", views.home, name="recipe_home"),
    path("author/<int:author_id>/",
         views.author_detailed, name="author_details"),
    path("recipe/<int:recipe_id>/",
         views.recipe_detailed, name="recipe_details"),

]
