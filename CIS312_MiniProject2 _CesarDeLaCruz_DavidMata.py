import os
import sys
smores_needed = int(input("How many S'mores would you like to make? "))
print("\n")
#the if/else statement if user puts too low or high of a number
if smores_needed > 50:
    print("Whoa, does this look like a franchise? Lets start again")
    exec(open(__file__).read())
    sys.exit()
elif smores_needed > 2:
    print(" ___ _ __ ___   ___  _ __ ___")
    print("/ __| '_ ` _ \\ / _ \\| '__/ _ \\")
    print("\\__ \\ | | | | | (_) | | |  __/")
    print("|___/_| |_| |_|\\___/|_|  \\___|")
else:
    print("You obviously do not like smores..Lets start again.")
    exec(open(__file__).read())
    sys.exit()
#amount of items in each package
graham_per_box = 8
marshmallow_per_bag = 48
hershey_bar = 1
#price of each package
graham_box_price = 3.36
marshmallow_bag_price = 1.44
hershey_bar_price = 0.88
#price of each individual item
price_per_graham = graham_box_price / graham_per_box
price_per_marshmallow = marshmallow_bag_price / marshmallow_per_bag
price_per_hershey = hershey_bar_price / hershey_bar
#equations to get smores needed and cost of each item
graham_per_smore = 1
marshmallow_per_smore = 1
hershey_per_smore = 1 / 2

graham_needed = smores_needed * graham_per_smore
marshmallow_needed = smores_needed * marshmallow_per_smore
hershey_needed = smores_needed * hershey_per_smore

graham_needed_price = graham_needed * price_per_graham
marshmallow_needed_price = marshmallow_needed * price_per_marshmallow
hershey_needed_price = hershey_needed * price_per_hershey
#solution to smores needed and cost
print("\n")
print("To make" , smores_needed , "S'mores, you will need")
print(graham_needed , "graham crackers, which will cost approximately ${:.2f}" .format(graham_needed_price))
print(marshmallow_needed , "large marshmallows, which will cost approximately ${:.2f}" .format(marshmallow_needed_price))
print(hershey_needed , "Hershey's chocolate bars, which will cost approximately ${:.2f}" .format(hershey_needed_price))
print("\n")
#recipe for S'mores
print("Follow the recipe below to make perfect S'mores!")
print("\n")
print("Step 1: Preheat oven to 350 degrees")
print("Step 2: Line a large baking sheet with foil or parchment paper.")
print("Step 3: Break the whole graham crackers along the scored line and place on the prepared baking sheet.")
print("Step 4: Put 1 square of chocolate on half of the graham crackers.")
print("Step 5: Place a marshmallow on each piece of chocolate.")
print("Step 6: Put the pan in the heated oven for about 4 to 6 minutes or long enough to melt the marshmallow and soften the chocolate.")
print("Step 7: Remove the pan from the oven and place the other half of the graham cracker on top pushing down slightly so it adheres.")
print("Step 8: Serve while still warm and Enjoy.")
