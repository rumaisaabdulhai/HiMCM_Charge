import numpy as np
import phoneUsage

'''
This Python File calculates the yearly energy consumption in dollars per person.
* Assumption: The phone is always charging to 100% from its low charge state.
'''

#############
# CONSTANTS #
#############

#num_elements = 1000000
min_battery_life = 3.58 # min hours for a smartphone battery life, defined from REFERENCE
max_battery_life = 4.51 # max hours for a smartphone battery life, defined from REFERENCE
min_recharge = 0.8 #REFERENCE
max_recharge = 1
KWH = 0.00545 # energy consumed by 1 hour of charging a phone REFERENCE

###################
# COMPUTE METHODS #
###################

def batteryInstances(elements):
  """
  This method generates instances of phones with various battery lifes between min_battery_life and max_battery_life
  (ex. a smartphone can have a battery life of 4 hours).

  :param elements: int
  :return: numpy array
  """

  battery_instances = np.asarray([np.random.uniform(min_battery_life, max_battery_life) for i in range(elements)])
  return battery_instances


def rechargeInstances(elements):
  """
  This method generates instances of phones with various recharging states between min_recharge and max_recharge
  (eg. a smartphone can have a recharge state of 0.8 which means the phone is currently at 20% charge).
  One instance of a phone recharge represents the percentage one must charge that phone to reach 100%.

  :param elements: int
  :return: numpy array
  """
  recharge_instances = np.asarray([np.random.uniform(min_recharge, max_recharge) for i in range(elements)])
  return recharge_instances


def usageDay(phoneUsage, battery, recharge):

  """
  This method calculates the number of times someone will have to charge their phone.
  :param phoneUsage: numpy array
  :param battery: numpy array
  :param recharge: numpy array
  :return: numpy array
  """

  # Calculates # of minutes it takes to charge battery
  denom = np.multiply(battery,recharge) * 60

  # gives the number of times someone will have to charge their phone
  return np.divide(phoneUsage, denom)


def energyConsumption(weekdayUsageDay, weekendUsageDay, battery, kwh = KWH):
  """
  This method calculates total energy consumption for both weekdays and weekends for a YEAR.

  :param weekdayUsageDay: numpy array
  :param weekendUsageDay: numpy array
  :param battery: numpy array
  :param kwh: float
  :return: numpy array
  """
  k = kwh * battery #KW used

  e_weekday = k * 5 * weekdayUsageDay * 52
  e_weekend = k * 2 * weekendUsageDay * 52

  totalConsumption = np.add(e_weekday, e_weekend)
  
  return totalConsumption

'''
This method calculates...
'''
def energyConsumptionPlaces(weekendUsageDay, battery, kwh = KWH):
  """
  This method calculates the total energy consumption for just weekends for a YEAR.

  :param weekendUsageDay: numpy array
  :param battery: numpy array
  :param kwh: numpy array
  :return: numpy array
  """
  k = KWH*battery

  e_weekend = k * 2 * weekendUsageDay * 52
  
  return e_weekend



##############
# REFERENCES #
##############
