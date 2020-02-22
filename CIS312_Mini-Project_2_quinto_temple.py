#input prompt
print("How many Big Macs* would you like?")
amount = int(input("-> "))

#prices
patty = 2.94
sauce = 0.25
lettuce = 1.38
cheese = 0.27
pickles = 0.40
onions = 0.62
buns = 0.24

single = (patty + sauce + lettuce + cheese + pickles + onions + buns)

#calculations
total = (single * amount)

patty_amt = int(2 * amount)
sauce_amt = int(1 * amount)
lettuce_amt = int(1 * amount)
cheese_amt = int(1 * amount)
pickles_amt = int(5 * amount)
onions_amt = int(1 * amount)
buns_amt = int(3 * amount)

#output
print("To make ", amount, " Big Macs, you will need: \n")
print(patty_amt, "patties ($2.94 for 2)\n", sauce_amt, "sauce ($0.25)\n", lettuce_amt, "lettuce ($1.38)\n", cheese_amt,
"cheese ($0.27)\n", pickles_amt, "pickles ($0.40 for 5)\n", onions_amt, "onions ($0.62)\n", buns_amt, "buns ($0.24 for 3)\n")
print("The total cost for all ingredients is: $", "%.2f" % total)
single_cost = input("\nWould you like to see the cost of a single (y/n)?: ")

#conditional for cost of a single Big Mac, consider this part of output
if single_cost == "y" or single_cost == "Y":
    print("The cost of a single Big Mac* is $", "%.2f" % single)
elif single_cost == "n" or single_cost == "N":
    print("Ok")
else:
    print("Invalid option")
print("\n(*costs may differ from cost of actual McDonalds Big Mac)")
print("https://www.mcdonalds.com/us/en-us/product/big-mac.html")
