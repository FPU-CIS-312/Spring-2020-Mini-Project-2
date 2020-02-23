#here is the price list. This is per ounce. (or per 1 for eggs)
price_list = {
  "eggs": 0.08,
  "flour": 0.02,
  "butter": 0.299,
  "baking_powder": 0.15,
  "baking_soda": 0.46,
  "brown_sugar": 0.05,
  "buttermilk": 0.03,
  "oil": 0.07,
  "chocolate_chips": 0.31,
  "chocolate_frosting": 0.10,
  "light_brown_sugar": 0.07,
  "vanilla": 2.62,
  "salt": 0.10,
  "cocoa_powder": 0.37,
  "sugar": 0.29
}

#This is the conversion rate to turn the ingredients back from ounces to a normal measurement for a recipe. I also listed the measurement I was converting to so I can easily print it out with the recipe. 
conversions = {
  "eggs": [1,"egg(s)"],
  "flour": [.2353, "cups"],
  "butter": [.125, "cups"],
  "baking_powder": [0.1689, "teaspoons"],
  "baking_soda": [5.882,"teaspoons"],
  "brown_sugar": [0.1418, "cups"],
  "buttermilk": [0.124,"cups"],
  "oil": [0.48, "tablespoons"],
  "chocolate_chips": [0.161, "cups"],
  "chocolate_frosting": [1, "ounces"],
  "light_brown_sugar":  [0.141, "cups"],
  "vanilla": [6.667, "teaspoons"],
  "salt": [5, "teaspoons"],
  "cocoa_powder": [0.286, "cups"],
  "sugar": [0.141, "cups"]
}


#This is the cookie recipe. All the units were converted to ounces. And I scaled it down so this recipe is for 1 cookie. 
cookie_recipe = {
  "butter": 0.3333,
  "sugar": 0.29,
  "brown_sugar": 0.29,
  "vanilla": 0.00625,
  "eggs": 0.083,
  "flour": 0.53125,
  "baking_powder": 0.1233,
  "baking_soda": 0.00708,
  "salt": 0.00833,
  "chocolate_chips": 0.516667
}

recipe_instructions = "\n\n\nPreheat your oven to 375 degrees and line a baking sheet with parchment paper.\n\nMix together the flour, baking soda, salt, and baking powder. Set aside. \n\nIn a seperate bowl, cream together butter and both sugars.\n\nOnce butter and sugars are well mixed, add in eggs and vanilla. Mix until fluffy.\n\nMix the dry ingredients into the wet ingrednents and mix just until they seem evenly combined.\n\nAdd the chocolate chips and mix until they seem evenly distributed.\n\nRoll 3 tablespoons or so at a time into balls. Place evenly on the baking sheet leaving 1-2 inches in between.\n\nBake for 8-10 minutes or until the edges are barely starting to turn brown.\n\nLet cookies cool on baking sheet for a minute or two before attempting to transfer to a cooling rack.\n\nEnjoy!"