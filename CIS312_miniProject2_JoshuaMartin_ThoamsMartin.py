pricePerDoughPackage = 2.00
pricePerBagOfPepperoni = 11.00
pricePerBagOfCheese = 5.00
pricePerJarOfSauce = 2.00

costPerPizzaForDough = pricePerDoughPackage / 2.0
costPerPizzaForPepperoni = pricePerBagOfPepperoni / 4.0
costPerPizzaForCheese = pricePerBagOfCheese / 2.0
costPerPizzaForSauce = pricePerJarOfSauce / 2.0

amountOfPizzaDoughNeeded = 1
amountOfPepperonisNeededPerPizza = 5
amountOfCheeseNeededPerPizza = 1
amountOfSauceNeededPerPizza = 12

costPerPizza = costPerPizzaForSauce + costPerPizzaForCheese + costPerPizzaForPepperoni + costPerPizzaForDough

numberOfPizzasRequested = float(input('Enter the number of Pizzas you want: '))

totalCost = costPerPizza * numberOfPizzasRequested
if numberOfPizzasRequested >= 5:
    totalCost = numberOfPizzasRequested * costPerPizza - (totalCost * .15)

tax = totalCost * .0725
totalCost = totalCost + tax
    
amountOfDoughNeededInTotal = amountOfPizzaDoughNeeded * numberOfPizzasRequested
amountOfPepperonisNeededInTotal = amountOfPepperonisNeededPerPizza * numberOfPizzasRequested
amountOfCheeseNeededInTotal = amountOfCheeseNeededPerPizza * numberOfPizzasRequested
amountOfSauceNeededInTotal = amountOfSauceNeededPerPizza * numberOfPizzasRequested

print('You will need',amountOfDoughNeededInTotal,'premade pizza crusts.')
print('You will need',amountOfPepperonisNeededInTotal,' ounzes of pepperonis.')
print('You will need',amountOfCheeseNeededInTotal,' pounds of cheese.')
print('You will need',amountOfSauceNeededInTotal,'ounzes of sauce.')

costPerItem = totalCost / numberOfPizzasRequested

print('It will be',"%.2f" % costPerItem,'per pizza.')
print('Your total will be:',"%.2f" % totalCost)
print('Use the following steps to make your pizza: ')
print('1. Preheat oven to 400 degrees.')
print('2. Put pizza dough on a round pizza tray.')
print('3. Spread sauce on top of the pizza dough.')
print('4. Spread cheese on top of the sauce.')
print('5. Place pepperonis on top of cheese.')
print('6. Cook pizza for 10-15 minutes at 400 degrees.')
print('7. Let pizza cool for 2-3 minutes after cokking before cutting.')
print('8. Enjoy.')
#>>> print("%.2f" % a)
  #13.95