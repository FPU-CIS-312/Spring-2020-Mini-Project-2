# -*- coding: utf-8 -*-
"""

created by the dynamic coding team of:
Lisa Lenhart
Melissa Regalado
Mark Munoz

Mini Project 2

"""
'''
Base Recipe for 4 people
  ***  Hot Chicken Salad Caaserole  ***
  1.5    cup       cubed cooked cdhicken meat
  0.5  12oz can   mushroom soup
  0.25   cup      mayo
  0.5    cup      chopped celery
  1      Tbsp     minced shallot
  1      Tbsp     lemon juice
  1       tsp     minced garlic
  0.5    cup      grated cheese - any kind
  0.25   cup      sliced or slivered water chestnuts
  2      each     chopped hard boiled eggs
  1.5   slices    chopped bread slices - any kind
  0.25   cup      sliced black olives
  0.5   sleeve    Ritz crackers crumbled
  0.25   cup      grated Paresan cheese
'''
  
'''
    ingrediants as list for each item with the following structure
    
    item = [name-in-recipe, measure-amount, type-measure, reducer, cost]
'''
    
ckn = ['diced cooked chicken meat',1.5, 'cup', 0.9, .70]
soup = ['cream of mushroom soup', 0.5, '12oz can', 1, 1.50]
mayo = ['mayonnaise', 0.25, 'cup', 0.8, 0.20]
clry = ['1/2 inch sliced celery', 0.5, 'cup', 0.75, 0.25]
on = ['minced shallot', 1, 'Tbsp', 0.8, 0.09]
lmn = ['lemon juice', 1, 'Tbsp', 0.65, 0.02]
grlk = ['minced garlic', 1, 'tsp', 0.75, 0.03]
chz = ['grated cheese - any kind', 0.25, 'cup', 0.75, 0.65]
wc = ['water chestnut - sliced or slivered', 0.25, 'cup', 0.7, 0.3]
egg = ['chopped hard boiled eggs', 2, 'each', 1, .15]
brd = ['torn bread slices - any kind', 1.5, 'slices', 0.85, 0.03]
oliv = ['sliced black olives', 0.25, 'cup', 0.75, 0.45]
ritz = ['Ritz crackers crumbled' ,0.5, 'sleeve', 0.8, 0.80]
parm = ['grated parmesan cheese', 0.25, 'cup', 0.75, 0.8]

'''

 -- Find out how many people recipe will be feeding.
 -- use round(num_people / 4) as base recipe is for 4 people.
 
'''
num_people = int(input('How many people will you be feeding with this recipe: '))

'''
multipler = #formula with round
'''
mltplr = round(num_people / 4)
# print('mltplr = ', mltplr) commented out test point
'''
 dictionary holding pan sizes available. Key is the increase in recipe from the base amount 
'''
pan = {1: '8x8', 2 : '9x11', 3 : '9x13', 4 : '11x15', 5 : 'full aluminum steam pan'}

'''
Use if and elif structure to calculate pans to use.
'''
m = mltplr
if mltplr == 1:
    pan_size = pan[m]
elif mltplr == 2:
    pan_size = pan[m]
elif mltplr == 3:
    pan_size = pan[m]
elif mltplr == 4:
    pan_size = pan[m]
elif mltplr == 5:
    pan_size = pan[m]
elif mltplr == 6:
    pan_size = pan[(m-4)] + ' and ' + pan[4]
elif mltplr == 7:
    pan_size = pan[(m-4)] + 'and ' + pan[4]
elif mltplr == 8: 
    pan_size = pan[(m-4)] + ' and ' + pan[4]
elif mltplr == 9: 
    pan_size = pan[(m-5)] + ' and ' + pan[5]
elif mltplr == 10: 
    pan_size = pan[(m-5)] + ' and ' + pan[5]
elif mltplr == 11: 
    pan_size = 'Two ' + pan[5] + ' and ' + pan[1]
elif mltplr == 12: 
    pan_size = 'Two ' + pan[5] + ' and ' + pan[2]
elif mltplr == 13: 
    pan_size = 'Two ' + pan[5] + ' and ' + pan[3]
elif mltplr == 14: 
    pan_size = 'Two ' + pan[5] + ' and ' + pan[4]
elif mltplr == 15: 
    pan_size = 'Three ' + pan[5]
else:
    pan_size = 'past 15 times base recipe.  Time to call a Caterer'
print()
print()                    
print()
print('                      ***  Hot Chicken Salad Casserole  *** ')
print('                                  For ', num_people, 'people')
print('                             Oven Bake Temp:  350 deg')
print()
print('Pans you will need:', pan_size)
print()
print(format(ckn[1] * m * ckn[3], '7,.2f'), format(ckn[2].center(20,' ')),  format(ckn[0].ljust(40,' ')), '$', format(ckn[4] * m * ckn[3], '8,.2f'))
print(format(soup[1] * m * soup[3], '7,.2f'), format(soup[2].center(20,' ')), format(soup[0].ljust(40,' ')), '$', format(soup[4] * m * soup[3], '8.2f'))
print(format(mayo[1] * m * mayo[3], '7,.2f'), format(mayo[2].center(20,' ')), format(mayo[0].ljust(40,' ')), '$', format(mayo[4] * m * mayo[3], '8.2f'))
print(format(clry[1] * m * clry[3], '7,.2f'), format(clry[2].center(20,' ')), format(clry[0].ljust(40,' ')), '$', format(clry[4] * m * clry[3], '8.2f'))
print(format(on[1] * m * on[3], '7,.2f'), format(on[2].center(20,' ')), format(on[0].ljust(40,' ')), '$', format(on[4] * m * on[3], '8.2f'))
print(format(lmn[1] * m * lmn[3], '7,.2f'), format(lmn[2].center(20,' ')), format(lmn[0].ljust(40,' ')), '$', format(lmn[4] * m * lmn[3], '8.2f'))
print(format(grlk[1] * m * grlk[3], '7,.2f'), format(grlk[2].center(20,' ')), format(grlk[0].ljust(40,' ')), '$', format(grlk[4] * m * grlk[3], '8.2f'))
print(format(chz[1] * m * chz[3], '7,.2f'), format(chz[2].center(20,' ')), format(chz[0].ljust(40,' ')), '$', format(chz[4] * m * chz[3], '8.2f'))
print(format(wc[1] * m * wc[3], '7,.2f'), format(wc[2].center(20,' ')), format(wc[0].ljust(40,' ')), '$', format(wc[4] * m * wc[3], '8.2f'))
print(format(egg[1] * m * egg[3], '7,.2f'), format(egg[2].center(20,' ')), format(egg[0].ljust(40,' ')), '$', format(egg[4] * m * egg[3], '8.2f'))
print(format(brd[1] * m * brd[3], '7,.2f'), format(brd[2].center(20,' ')), format(brd[0].ljust(40,' ')), '$', format(brd[4] * m * brd[3], '8.2f'))
print(format(oliv[1] * m * oliv[3], '7,.2f'), format(oliv[2].center(20,' ')), format(oliv[0].ljust(40,' ')), '$', format(oliv[4] * m * oliv[3], '8.2f'))
print(format(ritz[1] * m * ritz[3], '7,.2f'), format(ritz[2].center(20,' ')), format(ritz[0].ljust(40,' ')), '$', format(ritz[4] * m * ritz[3], '8.2f'))
print(format(parm[1] * m * parm[3], '7,.2f'), format(parm[2].center(20,' ')), format(parm[0].ljust(40,' ')), '$', format(parm[4] * m * parm[3], '8.2f'))
total_cost = (ckn[4] + soup[4] + mayo[4] + clry[4] + on[4] + lmn[4] + grlk[4] + chz[4] + wc[4] +\
    egg[4] + brd[4] + oliv[4] + ritz[4] + parm[4]) * m  
print('=================================================================================')
print(f'      Total cost for this recipe will be: $ {total_cost:5.2f}')
print()
print()
print('*******************************************************************************')
print('"***   Follow these instructions to make the best Hot Chicken Casserole !  ***"')
print('**********************************************************"********************')
print("Step 1: Preheat oven to 350 degrees")
print("Step 2: Combine all ingrediants, except for Ritz and parmesan cheese, in a bowl")
print("Step 3: Mix together till well blended, then pour into pan(s)")
print("Step 4: Mix together crumbled Ritz and Parmesan")
print("Step 5: Distribute evenly over top of filled pans")
print("Step 6: Bake in the heated oven for approx. 30 min. ; until warm and bubbly.")
print("Step 7: Serve Hot.")
