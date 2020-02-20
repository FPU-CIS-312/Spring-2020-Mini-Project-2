#Variables go here
num_cookies = int(input('How many cookies are you making?'))

#Ingredients Prices Dictionary for 1 cookie
ingredient_prices = {
    'Butter' : 0.03,
    'Sugar' : 0.03,
    'Brown Sugar' : 0.03,
    'Vanilla Extract' : 0.37,
    'Large Eggs' : 0.10,
    'Flour' : 0.09,
    'Baking Soda' : 0.01,
    'Salt' : 0.04,
    'Semisweet Chocolate Chips' : 0.07
    }

#Discounted Prices Dictionary for 1 cookie for Else (-30% on quantities greater than or equal to 100 cookies)
discounted_prices = {
    'Butter' : 0.02,
    'Sugar' : 0.02,
    'Brown Sugar' : 0.02,
    'Vanilla Extract' : 0.26,
    'Large Eggs' : 0.07,
    'Flour' : 0.06,
    'Baking Soda' : 0.01,
    'Salt' : 0.03,
    'Semisweet Chocolate Chips' : 0.05
    }

#Ingredients Quantity Dictionary for 1 cookie
ingredient_quantity = {
    'Butter' : 0.02, #cups
    'Sugar' : 0.02, #cups
    'Brown Sugar' : 0.01, #cups
    'Vanilla Extract' : 0.08, #cups
    'Large Eggs' : 0.04, #number of eggs
    'Flour' : 0.07, #cups
    'Baking Soda' : 0.02, #teaspoons
    'Salt' : 0.02, #teaspoons
    'Semisweet Chocolate Chips' : 0.04 #cups
    }
#If-else statement
if num_cookies <= 99:
    print('To make' + ' ' + str(num_cookies) + ' ' + 'chocolate chip cookies, you will need:')
    print('Butter -', round(ingredient_quantity['Butter'] * num_cookies, 2), 'cups, which will cost approximately $', round(ingredient_prices['Butter'] * num_cookies, 2))
    print('Sugar -', round(ingredient_quantity['Sugar'] * num_cookies, 2), 'cups, which will cost approximately $', round(ingredient_prices['Sugar'] * num_cookies, 2))
    print('Brown Sugar -', round(ingredient_quantity['Brown Sugar'] * num_cookies, 2), 'cups, which will cost approximately $', round(ingredient_prices['Brown Sugar'] * num_cookies, 2))
    print('Vanilla Extract -', round(ingredient_quantity['Vanilla Extract'] * num_cookies, 2), 'teaspoons, which will cost approximately $', round(ingredient_prices['Vanilla Extract'] * num_cookies, 2))
    print('Large Eggs -', round(ingredient_quantity['Large Eggs'] * num_cookies, 2), 'eggs, which will cost approximately $', round(ingredient_prices['Large Eggs'] * num_cookies, 2))
    print('Flour -', round(ingredient_quantity['Flour'] * num_cookies, 2), 'cups, which will cost approximately $', round(ingredient_prices['Flour'] * num_cookies, 2))
    print('Baking Soda -', round(ingredient_quantity['Baking Soda'] * num_cookies, 2), 'teaspoons, which will cost approximately $', round(ingredient_prices['Baking Soda'] * num_cookies, 2))
    print('Salt -', round(ingredient_quantity['Salt'] * num_cookies, 2), 'teaspoons, which will cost approximately $', round(ingredient_prices['Salt'] * num_cookies, 2))
    print('Semisweet Chocolate Chips -', round(ingredient_quantity['Semisweet Chocolate Chips'] * num_cookies, 2), 'cups, which will cost approximately $', round(ingredient_prices['Semisweet Chocolate Chips'] * num_cookies, 2))
    print('The total expected cost for all ingredients is: $', sum(ingredient_prices.values()) * num_cookies)

else:
    print('To make' + ' ' + str(num_cookies) + ' ' + 'chocolate chip cookies, you will need:')
    print('Butter -', round(ingredient_quantity['Butter'] * num_cookies, 2), 'cups, which will cost approximately $', round(discounted_prices['Butter'] * num_cookies, 2))
    print('Sugar -', round(ingredient_quantity['Sugar'] * num_cookies, 2), 'cups, which will cost approximately $', round(discounted_prices['Sugar'] * num_cookies, 2))
    print('Brown Sugar -', round(ingredient_quantity['Brown Sugar'] * num_cookies, 2), 'cups, which will cost approximately $', round(discounted_prices['Brown Sugar'] * num_cookies, 2))
    print('Vanilla Extract -', round(ingredient_quantity['Vanilla Extract'] * num_cookies, 2), 'teaspoons, which will cost approximately $', round(discounted_prices['Vanilla Extract'] * num_cookies, 2))
    print('Large Eggs -', round(ingredient_quantity['Large Eggs'] * num_cookies, 2), 'eggs, which will cost approximately $', round(discounted_prices['Large Eggs'] * num_cookies, 2))
    print('Flour -', round(ingredient_quantity['Flour'] * num_cookies, 2), 'cups, which will cost approximately $', round(discounted_prices['Flour'] * num_cookies, 2))
    print('Baking Soda -', round(ingredient_quantity['Baking Soda'] * num_cookies, 2), 'teaspoons, which will cost approximately $', round(discounted_prices['Baking Soda'] * num_cookies, 2))
    print('Salt -', round(ingredient_quantity['Salt'] * num_cookies, 2), 'teaspoons, which will cost approximately $', round(discounted_prices['Salt'] * num_cookies, 2))
    print('Semisweet Chocolate Chips -', round(ingredient_quantity['Semisweet Chocolate Chips'] * num_cookies, 2), 'cups, which will cost approximately $', round(discounted_prices['Semisweet Chocolate Chips'] * num_cookies, 2))
    print('The total expected cost for all ingredients is: $', round(sum(discounted_prices.values()) * num_cookies, 2), 'after a 30% discount from bulk ordering')
#Link to recipe
print('To see the recipe visit https://www.ihearteating.com/easiest-chocolate-chip-cookie-recipe/')
input('Press ENTER to exit')
