"""This module provides mutation for create Recipe."""
import graphene
from app.serializers import RecipeSerializer
from ..types import RecipeType
from app.models import Ingredient


class CreateRecipe(graphene.Mutation):
    """Mutation for create Recipe."""
    class Arguments:
        name = graphene.String(description="Name of the Recipe.", required=True)
        ingredient_ids = graphene.List(graphene.Int, description="List of Ingredient ids.", required=True)

    recipe = graphene.Field(RecipeType, description="Recipe type.")

    @classmethod
    def mutate(cls, root: graphene.ObjectType, info: graphene.ResolveInfo, **data: dict) -> "CreateRecipe":
        """Create Recipe."""
        recipe_data = {'name': data.get("name", None), 'ingredients': data.get("ingredient_ids", None)}
        serializer = RecipeSerializer(data=recipe_data)
        if serializer.is_valid():
            recipe = serializer.save()
            # Add the ingredients in recipe
            if recipe_data.get("ingredients"):
                ingredients = Ingredient.objects.filter(id__in=data.get("ingredient_ids"))
                recipe.ingredients.set(ingredients)
                recipe.save()
            return CreateRecipe(recipe=recipe)
        else:
            raise Exception(f"Validation Error: {serializer.errors}")
