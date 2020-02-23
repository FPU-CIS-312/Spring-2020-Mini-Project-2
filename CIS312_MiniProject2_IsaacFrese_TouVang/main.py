#This just loads all the stuff from data.py into the program. Its kinda the same as copy and pasting the code from the other file into the top of this one. 
from recipe_data import *

total_recipe_cost = 0.0


#we will call this method on each ingredient after we know the ammount we need. It just multiplies the ammount by the cost per ammount.  
def calculate_cost_of_ingredient(ingredient_name, ingredient_ammount):
  return price_list[ingredient_name]*ingredient_ammount

#This method will convert the ingredient to a normal measurement. It multiplies by the conversion rate, and combines the amount with the name of the unit. 
def convert_measurement(ingredient_name, ingredient_ammount):
  #conversion info will have the conversion rate, and the name of the unit it is being converted to. 
  conversion_info = conversions[ingredient_name]
  new_ammount = round(conversion_info[0]*ingredient_ammount, 2)
  new_unit = conversion_info[1]
  converted_measurement = "{} {}".format(new_ammount, new_unit)
  return converted_measurement

#This is a method that should print out the recipe nicely: 
def print_recipe(recipe):
  for ingredient in recipe:
    ingredient_ammount = convert_measurement(ingredient, recipe[ingredient])
    ingredient_price = calculate_cost_of_ingredient(ingredient, recipe[ingredient])
    print("{} of {} which will cost about ${}".format(ingredient_ammount, ingredient, round(ingredient_price, 2)))


#This takes the input from the user and asks how many cookies they want
number_of_cookies = float(input("How many chocolate chip cookies would you like to make?\n"))

#This scales up the recipe so that it is for the right amount of cookies. 
#It also adds up the cost while its scaling the recipe. 
for ingredient in cookie_recipe.keys():
  cookie_recipe[ingredient] = cookie_recipe[ingredient]*number_of_cookies
  total_recipe_cost += cookie_recipe[ingredient]*price_list[ingredient]


#here we call our print_recipe function that we made above. 
print("To make {} cookies you will need: ".format(number_of_cookies))
print_recipe(cookie_recipe)
print("Total recipe cost is aproximatly ${}".format(round(total_recipe_cost, 2)))
print(recipe_instructions)