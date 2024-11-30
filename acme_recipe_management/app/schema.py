"""This module define the graphql schema for the app."""
import graphene
from app.graphql.Ingredients import CreateIngredient, UpdateIngredient, DeleteIngredient
from app.graphql.Ingredients.resolvers import Resolvers as IngredientResolvers
from app.graphql.recipies.resolvers import Resolvers as RecipeResolvers
from app.graphql.Ingredients.types import IngredientType
from app.graphql.recipies.types import RecipeType
from app.graphql.recipies.mutations import CreateRecipe, AddIngredientsToRecipe, RemoveIngredientsFromRecipe


# Define the mutations for GraphQL
class Mutation(graphene.ObjectType):
    """Mutation schema."""
    create_ingredient = CreateIngredient.Field()
    update_ingredient = UpdateIngredient.Field()
    delete_ingredient = DeleteIngredient.Field()
    create_recipe = CreateRecipe.Field()
    add_ingredients_to_recipe = AddIngredientsToRecipe.Field()
    remove_ingredients_from_recipe = RemoveIngredientsFromRecipe.Field()


# Define the query for GraphQL
class Query(graphene.ObjectType):
    """Query schema."""
    ingredients = graphene.Field(
        graphene.List(IngredientType),
        description=("List of ingredients"),
        name=graphene.String(),
        quantity=graphene.String(),
        resolver=IngredientResolvers.resolve_all_ingredients,
    )

    recipe = graphene.Field(
        RecipeType,
        id=graphene.Int(),
        resolver=RecipeResolvers.resolve_recipe,
    )


schema = graphene.Schema(query=Query, mutation=Mutation)
