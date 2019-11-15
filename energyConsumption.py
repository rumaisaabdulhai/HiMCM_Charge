import numpy as np
import phoneUsage

# CONSTANTS:
num_elements = 100
batteryLifeMin = 3.58 # min hours for a smartphone battery life, defined from REFERENCE
batteryLifeMax = 4.51 # max hours for a smartphone battery life, defined from REFERENCE
rechargeMin = 0.8 #REFERENCE
rechargeMax = 1
KWH = 0.00545 # energy consumed by 1 hour of charging a phone REFERENCE

def batteryLife(numel=num_elements):
  # Generates phones with various battery lifes
  batteryInstance = np.asarray([np.random.uniform(batteryLifeMin,batteryLifeMax) for i in range(numel)])

  return batteryInstance

def recharge(numel=num_elements):
   # Generates phones with various recharging states
  recharge = np.asarray([np.random.uniform(rechargeMin,rechargeMax) for i in range(numel)])
 
  return recharge

def usageDay(phoneUsage, battery, recharge):

  # Calculates # of hours it takes to deplete battery
  denom = np.multiply(battery,recharge)

  # gives the number of times someone will have to charge their phone
  return np.divide(phoneUsage, denom)

def energyConsumption(weekdayUsageDay, weekendUsageDay, battery, kwh = KWH):
  k = KWH*battery

  e_weekday = k*5*weekdayUsageDay
  e_weekend = k*2*weekendUsageDay

  totalConsumption = e_weekday+e_weekend
  
  return totalConsumption


def energyConsumptionPlaces(weekendUsageDay, battery, kwh = KWH):
  k = KWH*battery

  e_weekend = k*2*weekendUsageDay
  
  return e_weekend