"""This module provides defination for IngredientType."""
from graphene_django.types import DjangoObjectType
from app.models import Ingredient


class IngredientType(DjangoObjectType):
    """IngredientType class."""
    class Meta:
        """Meta Configuration."""
        model = Ingredient
