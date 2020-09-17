from django import forms
from recipe_app.models import Recipe


class AddAuthorForm(forms.Form):
    name = forms.CharField(max_length=50)
    bio = forms.CharField(widget=forms.Textarea())
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)


class AddRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ["title", "description",
                  "time_required", "instructions"]


class LoginForm(forms.Form):
    username = forms.CharField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput)


class UpdateRecipeForm(forms.ModelForm):
    class Meta:
        model = Recipe
        fields = ["title", "description", "time_required", "instructions"]


# class SignUpForm(forms.Form):
#     username = forms.CharField(max_length=150)
#     password = forms.CharField(widget=forms.PasswordInput)
