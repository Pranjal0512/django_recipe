from django.db import models


# Create your models here.
class Recipe(models.Model):
    
    recipe_name = models.CharField(max_length=255)
    recipe_image =models.ImageField(upload_to="recipe")
    recipe_description = models.TextField()

    def __str__(self):
        return self.recipe_name
    