"""This module provides mutation for update Ingredient."""
import graphene
from app.models import Ingredient
from app.serializers import IngredientSerializer
from ..types import IngredientType


class UpdateIngredient(graphene.Mutation):
    """Mutation for update Ingredient."""
    class Arguments:
        ingredient_id = graphene.Int(description="Id of the Ingredient.", required=True)
        name = graphene.String(description="Name of the Ingredient.")
        quantity = graphene.String(description="Quantity of the Ingredient.")

    ingredient = graphene.Field(IngredientType, description="Ingredient type.")

    @classmethod
    def mutate(cls, root: graphene.ObjectType, info: graphene.ResolveInfo, **data: dict) -> "UpdateIngredient":
        """Create Ingredient."""
        ingredient = Ingredient.objects.get(id=data.get("ingredient_id"))
        serializer = IngredientSerializer(ingredient, data=data, partial=True)
        if serializer.is_valid():
            updated_ingredient = serializer.save()
            return UpdateIngredient(ingredient=updated_ingredient)
        else:
            raise Exception(f"Validation Error: {serializer.errors}")

