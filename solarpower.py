import numpy as np
import random
# raw array from reference: [[4.0, 5.0, 6.0, 8.0, 10.0, 12.0, 20.0],
#         [10402.0, 12389.0, 14228.0, 17898.0, 21305.0, 24696.0, 38858.0]]

num_elements = 100

amount_of_kwh = np.asarray([np.random.uniform(4.0,20.0,num_elements)])
cost_of_install = 0
years = 100

cost_of_install = (2093*amount_of_kwh) +(2.1*(10**-12))#Calculated from line of best fit from solar cell installation cost data(https://news.energysage.com/how-much-does-the-average-solar-panel-installation-cost-in-the-u-s/)


kwhs = amount_of_kwh * years*365*24
solar_cost_per_kwh = np.divide(total_solar_cost, kwhs)
total_regular_cost = 0.12 * kwhs
regular_cost_per_kwh = 0.12

difference_in_total_cost = np.subtract(total_regular_cost,total_solar_cost)
difference_in_cost_per_kwh = np.subtract(regular_cost_per_kwh,solar_cost_per_kwh)

def getValue():
  return "difference in total cost: "+str(difference_in_total_cost)+" | difference in cost per kwh: "+str(difference_in_cost_per_kwh)