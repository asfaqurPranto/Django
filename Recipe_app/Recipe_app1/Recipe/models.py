from django.db import models

# Create your models here.
class Recipe(models.Model):
    title = models.CharField(max_length=255, unique=True)  # Unique constraint
    ingredients = models.TextField()
    instructions = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)  # Automatically set on creation

    def __str__(self):
        return self.title  # Ensures readable representation