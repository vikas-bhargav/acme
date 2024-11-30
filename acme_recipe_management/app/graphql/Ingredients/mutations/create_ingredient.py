"""This module provides mutation for create Ingredient."""
import graphene
from app.serializers import IngredientSerializer
from ..types import IngredientType


class CreateIngredient(graphene.Mutation):
    """Mutation for create Ingredient."""
    class Arguments:
        name = graphene.String(description="Name of the Ingredient.", required=True)
        quantity = graphene.String(description="Quantity of the Ingredient.", required=True)

    ingredient = graphene.Field(IngredientType, description="Ingredient type.")

    @classmethod
    def mutate(cls, root: graphene.ObjectType, info: graphene.ResolveInfo, **data: dict) -> "CreateIngredient":
        """Create Ingredient."""
        serializer = IngredientSerializer(data=data)
        if serializer.is_valid():
            ingredient = serializer.save()
            return CreateIngredient(ingredient=ingredient)
        else:
            raise Exception(f"Validation Error: {serializer.errors}")

