from django.db import models
from django.contrib.auth.models import User
from django.shortcuts import reverse

# Create your models here.


class Author (models.Model):
    name = models.CharField(max_length=20)
    bio = models.TextField()
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class Recipe (models.Model):
    title = models.CharField(max_length=50)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    description = models.TextField()
    time_required = models.CharField(max_length=20)
    instructions = models.TextField()
    favorited_by = models.ManyToManyField(
        Author, related_name='favorited_by_author')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('recipe_details', kwargs={'recipe_id': self.id})
