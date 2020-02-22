# coffee cake ingredients and dictionaries
coffee_cake_ingredient_list = ['flour', 'sugar', 'shortening', 'eggs', 'baking soda', 'salt', 'milk', 'vanilla extract']
coffee_cake_dict = {'flour': 2.0, 'sugar': 6.0, 'shortening': 1.0, 'eggs': 1.0, 'baking soda': 1.0, 'salt': 1.0,
                    'milk': 1.0, 'vanilla extract': 1.0}
coffee_cake_cost = {'flour': 1.66, 'sugar': 0.05, 'shortening': 0.56, 'eggs': 0.54, 'baking soda': 0.08, 'salt': 0.04,
                    'milk': 0.31, 'vanilla extract': 0.12}
# brownies ingredients and dictionaries
brownies_ingredient_list = ['butter', 'eggs', 'cocoa powder', 'salt', 'flour', 'vegetable oil', 'baking soda', 'sugar']
brownies_dict = {'butter': 1.0, 'eggs': 2.0, 'cocoa powder': 1.0, 'salt': 1.0, 'flour': 1.0, 'vegetable oil': 1.0,
                 'baking soda': 1.0, 'sugar': 1.0}
ten_brownies_cost = {'butter': 1.10, 'eggs': 1.08, 'cocoa powder': 2.69, 'salt': 0.04, 'flour': 0.83,
                     'vegetable oil': 0.50, 'baking soda': 1.0, 'sugar': 1.0}
# cookies ingredients and dictionaries
cookies_ingredient_list = ['eggs', 'flour', 'oats', 'sugar', 'baking soda', 'raisins', 'butter', 'cinnamon']
ten_cookies_cost = {'eggs': 0.54, 'flour': 0.83, 'oats': 1.50, 'sugar': 0.23, 'baking soda': 0.08, 'raisins': 3.38,
                    'butter': 1.08, 'cinnamon': 0.10}
cookies_dict = {'eggs': 1.0, 'flour': 1.0, 'oats': 2.0, 'sugar': 1.0, 'baking soda': 1.0, 'raisins': 1.0, 'butter': 2.0,
                'cinnamon': 1.0}

item_to_make = str(input('Welcome to CIS 312s online bakery!!\nWhich fine desert would you like to bake today?\nOatmeal cookies, brownies, or coffee-cake?\n'))
if 'oatmeal cookies' == item_to_make:
    print('The ingredients to make oatmeal cookies are', cookies_ingredient_list)
    how_many = int(input('How many cookies would you like to make?\n'))
    how_many_divided = how_many / 10
    print('To make', how_many, item_to_make, 'you will need', how_many_divided * cookies_dict['eggs'],
          'egg(s), which will cost you $', (ten_cookies_cost['eggs'] * how_many_divided))
    print((how_many_divided * cookies_dict['flour']), 'cup(s) of flour and it will cost you $',
          round((ten_cookies_cost['flour'] * how_many_divided), 2)),
    print(how_many_divided * cookies_dict['oats'], 'cup(s) of oats and it will cost you $',
          round((ten_cookies_cost['oats'] * how_many_divided), 2))
    print(how_many_divided * cookies_dict['sugar'], 'cup(s) of sugar and it will cost you $',
          round((ten_cookies_cost["sugar"] * how_many_divided), 2))
    print(how_many_divided * cookies_dict['baking soda'], 'tea spoon(s) of baking soda and it will cost you $',
          (ten_cookies_cost['baking soda'] * how_many_divided))
    print(how_many_divided * cookies_dict['raisins'], 'cup(s) of raisins and it will cost you $',
          (ten_cookies_cost['raisins'] * how_many_divided))
    print(how_many_divided * cookies_dict['butter'], 'stick(s) of butter and it will cost you $',
          (ten_cookies_cost['butter'] * how_many_divided))
    print(how_many_divided * cookies_dict['cinnamon'], 'tea spoon(s) of cinnamon and it will cost you $',
          (ten_cookies_cost['cinnamon'] * how_many_divided))
    recipe = str(input('Would you like a link to the recipe to make oatmeal cookies? (yes or no)\n'))
    if recipe == 'yes':
        print('https://www.allrecipes.com/recipe/11032/oatmeal-craisin-cookies')
    else:
        print('Have a good day baking!!')
    wait = input()
elif "brownies" == item_to_make:
    print('The ingredients to make brownies are', brownies_ingredient_list)
    how_many = int(input('How many brownies would you like to make?\n'))
    how_many_divided = how_many / 10
    print('To make', how_many, item_to_make, 'you will need', how_many_divided * brownies_dict['eggs'],
          'egg(s), which will cost you $', round((ten_brownies_cost['eggs'] * how_many_divided), 2))
    print((how_many_divided * brownies_dict['flour']), 'cup(s) of flour and it will cost you $',
          round((ten_brownies_cost['flour'] * how_many_divided), 2)),\
    print(how_many_divided * brownies_dict['cocoa powder'], 'cup(s) of cocoa powder and it will cost you $',
          round((ten_brownies_cost['cocoa powder'] * how_many_divided), 2))
    print(how_many_divided * brownies_dict['sugar'], 'cup(s) of sugar and it will cost you $',
          round((ten_brownies_cost["sugar"] * how_many_divided), 2))
    print(how_many_divided * brownies_dict['baking soda'], 'tea spoon(s) of baking soda and it will cost you $',
          (ten_brownies_cost['baking soda'] * how_many_divided))
    print(how_many_divided * brownies_dict['salt'], 'teaspoon(s) of salt and it will cost you $',
          (ten_brownies_cost['salt'] * how_many_divided))
    print(how_many_divided * brownies_dict['butter'], 'stick(s) of butter and it will cost you $',
          round((ten_brownies_cost['butter'] * how_many_divided), 2))
    print(how_many_divided * brownies_dict['vegetable oil'], 'cup(s) of vegetable oil and it will cost you $',
          (ten_brownies_cost['vegetable oil'] * how_many_divided))
    recipe = str(input('Would you like a link to the recipe to make brownies? (yes or no)\n'))
    if recipe == 'yes':
        print('https://www.allrecipes.com/recipe/10549/best-brownies/')
    else:
        print('Have a good day baking!!')
    wait = input()

elif 'coffee-cake' == item_to_make:
    print('The ingredients to make coffee cake are', coffee_cake_ingredient_list)
    how_many = int(input('How many pieces of coffee cake would you like to make?\n'))
    how_many_divided = how_many / 10
    print('To make', how_many, 'pieces of', item_to_make, 'you will need', how_many_divided * coffee_cake_dict['eggs'],
          'egg(s), which will cost you $', round((coffee_cake_cost['eggs'] * how_many_divided), 2))
    print(how_many_divided * coffee_cake_dict['sugar'], 'tablespoon(s) of sugar and it will cost you $',
          round((coffee_cake_cost["sugar"] * how_many_divided), 2))
    print(how_many_divided * coffee_cake_dict['shortening'], 'cup(s) of shortening and it will cost you $',
          round((coffee_cake_cost["shortening"] * how_many_divided), 2))
    print(how_many_divided * coffee_cake_dict['flour'], 'cup(s) of flour and it will cost you $',
          round((coffee_cake_cost["flour"] * how_many_divided), 2))
    print(how_many_divided * coffee_cake_dict['baking soda'], 'teaspoon(s) of baking soda and it will cost you $',
          round((coffee_cake_cost["baking soda"] * how_many_divided), 2))
    print(how_many_divided * coffee_cake_dict['salt'], 'teaspoon(s) of salt and it will cost you $',
          round((coffee_cake_cost["salt"] * how_many_divided), 2))
    print(how_many_divided * coffee_cake_dict['milk'], 'cup(s) of milk and it will cost you $',
          round((coffee_cake_cost["milk"] * how_many_divided), 2))
    print(how_many_divided * coffee_cake_dict['vanilla extract'], 'teaspoon(s) of vanilla extract and it will cost you $'
          , round((coffee_cake_cost["vanilla extract"] * how_many_divided), 2))
    recipe = str(input('Would you like a link to the recipe to make coffee cake? (yes or no)\n'))
    if recipe == 'yes':
        print('https://www.allrecipes.com/recipe/15399/cinnamon-coffee-cake-ii')
    else:
        print('Have a good day baking!!')
    wait = input()
else:
    print('I think you mistyped or selected something not in our menu. Try again please!')
    wait = input()


