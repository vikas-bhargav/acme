"""This module provides mutation for AddIngredientsToRecipe."""
import graphene
from app.models import Ingredient, Recipe
from ..types import RecipeType


class AddIngredientsToRecipe(graphene.Mutation):
    """Mutation for AddIngredientsToRecipe."""

    class Arguments:
        recipe_id = graphene.Int(description="Id of the Recipe.", required=True)
        ingredient_ids = graphene.List(graphene.Int, description="List of Ingredient ids to add.", required=True)

    recipe = graphene.Field(RecipeType, description="Recipe type.")

    @classmethod
    def mutate(cls, root: graphene.ObjectType, info: graphene.ResolveInfo, **data: dict) -> "AddIngredientsToRecipe":
        """Add ingredient to Recipe."""
        ingredient_ids = data.get("ingredient_ids")
        recipe = Recipe.objects.get(id=data.get("recipe_id"))
        for ingredient_id in ingredient_ids:
            ingredient = Ingredient.objects.get(id=ingredient_id)
            recipe.ingredients.add(ingredient)
        recipe.save()
        return AddIngredientsToRecipe(recipe=recipe)

