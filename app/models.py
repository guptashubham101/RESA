from django.conf import settings
import uuid
from django.db import models
from django.utils import timezone

class  ExtractedRecipe(models.Model):
    userId = models.ForeignKey('User')
    recipe_template = models.TextField()
    recipe_url = models.TextField()
    creation_date = models.DateTimeField(default=timezone.now)
    modification_date = models.DateTimeField(default=timezone.now)
    source = models.CharField(max_length=50)
    recipe_title = models.CharField(max_length=50)
    class Meta:
        db_table = 'extracted_recipe'

    def __str__(self):
        return "%s" % (self.id)

class Ingredients(models.Model):

    recipeId = models.ForeignKey('ExtractedRecipe')
    ingredient_name = models.CharField(max_length=50)

    class Meta:
        db_table = 'ingredients'

    def __str__(self):
        return "%s" % (self.id)

class User(models.Model):
    username = models.CharField(max_length=255)
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    contact_number = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    creation_date = models.DateTimeField(default=timezone.now)
    modification_date = models.DateTimeField(default=timezone.now)
    

    class Meta:
        db_table = 'user'

    def __str__(self):
        return "%s" % (self.id)