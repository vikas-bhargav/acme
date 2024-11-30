"""Resolver for Ingredient."""
import graphene
from graphene import ResolveInfo
from app.models import Ingredient


class Resolvers:
    """List Ingredient Resolver."""

    @staticmethod
    def resolve_all_ingredients(parent: graphene.ObjectType, info: ResolveInfo, name=None, quantity=None) -> [Ingredient]:
        """Return the list of Ingredient."""
        # Filter
        filter_set = {}
        if name:
            filter_set["name__icontains"] = name
        if quantity:
            filter_set["quantity__icontains"] = quantity
        ingredients = Ingredient.objects.filter(**filter_set)
        return ingredients
