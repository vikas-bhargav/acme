"""This module provides serializers for the app."""

from rest_framework import serializers
from .models import Recipe, Ingredient


class RecipeSerializer(serializers.ModelSerializer):
    """Serializer for the Recipe model."""
    class Meta:
        model = Recipe
        fields = ['id', 'name', 'ingredients']


class IngredientSerializer(serializers.ModelSerializer):
    """Serializer for the Ingredient model."""
    class Meta:
        model = Ingredient
        fields = ['id', 'name', 'quantity']


