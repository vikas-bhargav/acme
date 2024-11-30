"""Resolver for Recipe."""
import graphene
from graphene import ResolveInfo
from app.models import Recipe


class Resolvers:
    """Recipe Resolver."""

    @staticmethod
    def resolve_recipe(parent: graphene.ObjectType, info: ResolveInfo, id) -> Recipe:
        """Return the detail for recipe."""
        try:
            return Recipe.objects.get(id=id)
        except Recipe.DoesNotExist:
            return None

