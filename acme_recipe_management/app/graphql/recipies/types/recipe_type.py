"""This module provides defination for RecipeType."""
import graphene
from graphene_django.types import DjangoObjectType
from app.models import Recipe


class RecipeType(DjangoObjectType):
    """RecipeType class."""
    ingredient_count = graphene.Int()

    class Meta:
        """Meta Configuration."""
        model = Recipe

    def resolve_ingredient_count(self, info):
        return self.ingredient_count