import numpy as np
import compiling
import random

# FOOT TRAFFIC CONSTANTS (per day)
malls = 2000*52
airports = 782.85*52 
schools = 2984.92*52 
libraries = 3174.06*52 
coffee_shops = 3333.33*52 
gas_station = 2000*52;
meanLowBattery = 0.05
BatteryRange = 0.04

# totalFootTraffic = [mall, airport, school, library, coffee_shop]
# Format for each of these tuples: (foot traffic per year, minimum time spent, maximum time spent), CHECK WHETHER FOOT TRAFFIC IS PER YEAR OR WEEK OR DAY
places_info = { "mall": (malls, 75195-500,75195+500), # avg hrs were 75195
                "airport": (airports, 3.00, 3.66), # avg hrs were 3.33
                "library": (libraries, 1,5, 2.5), # avg hrs were 2
                "coffeeshop": (coffee_shops, 0.1, 1.5) }

def placesCost(foot_traffic, hoursSpentMin, hoursSpentMax):
  
  hours_spent = np.asarray([np.random.uniform(hoursSpentMin,hoursSpentMax) for x in range(foot_traffic)])
  lowBatteries = random.uniform(meanLowBattery-BatteryRange,meanLowBattery-BatteryRange)

  s = np.sum(compiling.compileDataPlaces(foot_traffic, hoursout=hours_spent))

  yearlyCost = np.asarray([lowBatteries * s for i in range(foot_traffic)])

  return yearlyCost


def getPlace(key):
  a = places_info[key][0]
  b = places_info[key][1]
  c = places_info[key][2]

  yearlyCost = placesCost(a,b,c)

  return yearlyCost

"""
References:

#Malls::
  hours spent =135/60: time found in ICSC survey
#Airports:: 
  passengers in the us (https://www.worldatlas.com/articles/countries-with-the-highest-number-of-airline-passengers.html), number of us airports (https://www.bts.gov/content/number-us-airportsa)
#Schools::
  num of students: 
  (https://nces.ed.gov/fastfacts/display.asp?id=372), number of schools: (https://www.statista.com/statistics/238307/number-of-us-elementary-and-secondary-schools/)
#Libraries::
  num of libraries per year: 
  hour spent=2 based on statistics for a randomly sampled library (Portland, Maine)
  (https://libguides.ala.org/numberoflibraries), number of visits: (http://www.ala.org/tools/libfactsheets/alalibraryfactsheet06)
#Coffee Shops::
  min(0.1) max(1.5) from average times spent in randomly selected coffee shops (Andover, MN Dunkin Donuts, Old California Coffee House and Eatery, in San Marcos California)
  #per starbucks per year 
  (https://yourbusiness.azcentral.com/average-number-patrons-coffee-shop-26736.html)
"""