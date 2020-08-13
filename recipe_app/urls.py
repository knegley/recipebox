from django.urls import path
from recipe_app import views

urlpatterns = [
    path("", views.home, name="recipe_home"),
    path("author/<int:author_id>/",
         views.author_detailed, name="author_details"),
    path("recipe/<int:recipe_id>/",
         views.recipe_detailed, name="recipe_details"),
    path("addauthor/", views.add_author, name="add_author"),
    path("addrecipe/", views.add_recipe, name="add_recipe"),
    path("signup/", views.signup_view, name="signup_view"),
    path("login/", views.login_view, name="login_view"),
    path("logout/", views.logout_view, name="logout_view")

]
