import numpy as np
import phoneUsage
import energyConsumption

#############
# CONSTANTS #
#############

avg_KWH_cost = 0.12

def kwh_cost(elements, min = 0.08, max = 0.16):
  avg_cost = np.asarray([random.uniform(min,max) for i in range(numel)])

  return avg_cost

def cost(totalConsumption, kwh_cost=avg_KWH_cost):

  cost = totalConsumption*kwh_cost
  return cost
