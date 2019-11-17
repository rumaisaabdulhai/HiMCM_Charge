import numpy as np
import phoneUsage

'''
This Python File calculates...

* Assumption: The phone is always charging to 100% from its low charge state.
'''

#############
# CONSTANTS #
#############

num_elements = 1000000
min_battery_life = 3.58 # min hours for a smartphone battery life, defined from REFERENCE
max_battery_life = 4.51 # max hours for a smartphone battery life, defined from REFERENCE
min_recharge = 0.8 #REFERENCE
max_recharge = 1
KWH = 0.00545 # energy consumed by 1 hour of charging a phone REFERENCE

'''
This method generates instances of phones with various battery lifes between min_battery_life and max_battery_life
(ex. a smartphone can have a battery life of 4 hours)
'''
def batteryInstances(elements):

  battery_instances = np.asarray([np.random.uniform(min_battery_life, max_battery_life) for i in range(num_elements)])
  return battery_instances

'''
This method generates instances of phones with various recharging states between min_recharge and max_recharge
(ex. a smartphone can have a recharge state of 0.8 which means the phone is currently at 20% charge)
One instance of a phone represents the percentage one must charge that phone to reach 100%
'''
def rechargeInstances(elements):
  recharge_instances = np.asarray([np.random.uniform(min_recharge, max_recharge) for i in range(num_elements)])
  return recharge_instances

'''
This method calculates the number of times someone will have to charge their phone
'''
def usageDay(phoneUsage, battery, recharge):

  # Calculates # of hours it takes to charge battery
  denom = np.multiply(battery,recharge)

  # gives the number of times someone will have to charge their phone
  return np.divide(phoneUsage, denom)

'''
This method calculates
'''
def energyConsumption(weekdayUsageDay, weekendUsageDay, battery, kwh = KWH):
  k = kwh * battery

  e_weekday = k * 5 * weekdayUsageDay
  e_weekend = k * 2 * weekendUsageDay

  totalConsumption = e_weekday + e_weekend
  
  return totalConsumption

'''
This method calculates...
'''
def energyConsumptionPlaces(weekendUsageDay, battery, kwh = KWH):
  k = KWH*battery

  e_weekend = k*2*weekendUsageDay
  
  return e_weekend


##############
# REFERENCES #
##############
