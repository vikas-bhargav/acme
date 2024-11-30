"""This module provides definition for app models."""
from django.db import models


class Ingredient(models.Model):
    """Ingredient model."""
    name = models.CharField(max_length=255)
    quantity = models.CharField(max_length=255)

    def __str__(self):
        """String representation of Ingredient."""
        return f"{self.name} ({self.quantity})"


class Recipe(models.Model):
    """Recipe model."""
    name = models.CharField(max_length=255)
    ingredients = models.ManyToManyField(Ingredient, related_name='recipes')

    def __str__(self):
        """String representation of Recipe."""
        return self.name

    @property
    def ingredient_count(self):
        """Total count of ingredients."""
        return self.ingredients.count()
