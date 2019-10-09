#!/usr/bin/python

import math

def recipe_batches(recipe, ingredients):
  how_many = []

  # If ingredients are missing then return 0
  if recipe.keys() != ingredients.keys():
    return 0
  
  # Loop through list to get the floor ratio
  for key in recipe:
    how_many.append(ingredients[key] // recipe[key])

  # Get the min amount of recipe
  return min(how_many)


if __name__ == '__main__':
  # Change the entries of these dictionaries to test 
  # your implementation with different inputs
  recipe = { 'milk': 100, 'butter': 50, 'flour': 5 }
  ingredients = { 'milk': 132, 'butter': 48, 'flour': 51 }
  print("{batches} batches can be made from the available ingredients: {ingredients}.".format(batches=recipe_batches(recipe, ingredients), ingredients=ingredients))