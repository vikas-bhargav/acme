"""This module provides mutation for delete Ingredient."""
import graphene
from app.models import Ingredient


class DeleteIngredient(graphene.Mutation):
    """Mutation for delete Ingredient."""
    class Arguments:
        ingredient_id = graphene.Int(description="Id of the Ingredient.", required=True)

    success = graphene.Boolean()

    @classmethod
    def mutate(cls, root: graphene.ObjectType, info: graphene.ResolveInfo, **data: dict) -> "DeleteIngredient":
        """Delete Ingredient."""
        try:
            ingredient = Ingredient.objects.get(id=data.get("ingredient_id"))
            ingredient.delete()
            return DeleteIngredient(success=True)
        except Ingredient.DoesNotExist:
            return DeleteIngredient(success=False)
