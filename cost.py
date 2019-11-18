import numpy as np
import random
import phoneUsage
import energyConsumption

#############
# CONSTANTS #
#############

usageDay = 0.625 # Times per day you charge your phone.
e_yearly = 4.44938 # KWH
avg_kwh_cost = 0.12

###################
# COMPUTE METHODS #
###################

def cost(totalConsumption, kwh_cost=avg_kwh_cost):
  """
  This method calculates the total cost per YEAR for each smartphone.
  :param totalConsumption: numpy array
  :param kwh_cost: float
  :return: numpy array
  """

  cost = totalConsumption*kwh_cost
  return cost


##############
# REFERENCES #
##############
