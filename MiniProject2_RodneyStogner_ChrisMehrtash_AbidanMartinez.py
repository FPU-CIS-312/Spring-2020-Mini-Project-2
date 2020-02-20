# Rodney Stogner, Chris Mehrtash, Abidan Martinez

# Recipe

regular_batch_of_brownies = 16
cups_of_sugar_per16_brownies = 1
sticks_of_butter_per16_brownies = 1
cups_of_flour_per16_brownies = 0.5
cups_of_unsweetenedcocoa_per16_brownies = 0.5
number_of_eggs_per16_brownies = 2
teaspoons_of_vanilla_per16_brownies = 1
teaspoons_of_salt_per16_brownies = 0.25

recipe = [ "cups of sugar = 1", "sticks of butter = 1", "cups of flour = 0.5", \
          "cups of unsweetenedcocoa = 0.5", "number of eggs = 2", \
          "teaspoons of vanilla = 1", "teaspoons of salt = 0.25"]


# Input Statement

usernumber_of_brownies = int(input("How many brownies do you want to make(16 miniumum):"))

# If-else statement


if usernumber_of_brownies >= 16:
    print("")

else:
    print ("Invalid amount.")
    raise SystemExit  

 

# How many of each item we will need

expected_cups_of_sugar = ( usernumber_of_brownies / regular_batch_of_brownies) * \
                      cups_of_sugar_per16_brownies

expected_sticks_of_butter = ( usernumber_of_brownies / regular_batch_of_brownies) * \
                       sticks_of_butter_per16_brownies

expected_cups_of_flour = ( usernumber_of_brownies / regular_batch_of_brownies) * \
                      cups_of_flour_per16_brownies

expected_cups_of_unsweetenedcocoa = ( usernumber_of_brownies  / regular_batch_of_brownies) * \
                      cups_of_unsweetenedcocoa_per16_brownies

expected_number_of_eggs = ( usernumber_of_brownies / regular_batch_of_brownies) * \
                      number_of_eggs_per16_brownies

expected_teaspoons_of_vanilla = ( usernumber_of_brownies / regular_batch_of_brownies) * \
                      teaspoons_of_vanilla_per16_brownies

expected_teaspoons_of_salt = ( usernumber_of_brownies / regular_batch_of_brownies) * \
                      teaspoons_of_salt_per16_brownies

# Cost of items

price_for_sugar = expected_cups_of_sugar * 0.38

price_for_butter = expected_sticks_of_butter * 3.75

price_for_flour = expected_cups_of_flour * 0.03

price_for_unsweetenedcocoa = expected_cups_of_unsweetenedcocoa * 1.24

price_for_eggs = expected_number_of_eggs * 0.20

price_for_vanilla = expected_teaspoons_of_vanilla * 0.83

price_for_salt = expected_teaspoons_of_salt * 0.01

# Total

total = price_for_sugar + price_for_butter + price_for_flour + price_for_unsweetenedcocoa + price_for_eggs + \
        price_for_vanilla + price_for_salt

# Solution

print( "\nFor",usernumber_of_brownies,"brownies you will need:") 

print("\nWill use",format(expected_cups_of_sugar, ".1f") , "cups of sugar, which will cost $", format(price_for_sugar,".2f"))
        
print("Will use",format(expected_sticks_of_butter, ".1f") , "sticks of butter, which will cost $", format(price_for_butter,".2f"))

print("Will use",format(expected_cups_of_flour, ".1f") , "cups of flour, which will cost $", format(price_for_flour,".2f"))

print("Will use",format(expected_cups_of_unsweetenedcocoa, ".1f") , "cups of unsweetened cocoa, which will cost $", format(price_for_unsweetenedcocoa,".2f"))

print("Will use",format(expected_number_of_eggs, ".1f") , "eggs, which will cost $", format(price_for_eggs,".2f"))

print("Will use",format(expected_teaspoons_of_vanilla, ".1f") , "teaspoons of vanilla, which will cost $", format(price_for_vanilla,".2f"))

print("Will use",format(expected_teaspoons_of_salt, ".1f") , "teaspoons of salt, which will cost $", format(price_for_salt,".2f"))

print("\nThe total estimated cost for all ingredients is $" , format(total,".2f"))

print("\nRecipe for 16 brownies:\n", *recipe, sep = "\n")


    
