import numpy as np
import phoneUsage
import energyConsumption

#############
# CONSTANTS #
#############

avg_kwh_cost = 0.12

'''
This method calculates...
'''
def kwh_cost(elements, min = 0.08, max = 0.16):
  avg_cost = np.asarray([random.uniform(min,max) for i in range(numel)])

  return avg_cost

'''
This method calculates...
'''
def cost(totalConsumption, kwh_cost=avg_kwh_cost):

  cost = totalConsumption*kwh_cost
  return cost


##############
# REFERENCES #
##############
