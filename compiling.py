import pandas as pd
import numpy as np
import cost
import energyConsumption
import phoneUsage
import random

#############
# CONSTANTS #
#############

num_elements = 1000000
per_of_adults = 0.55 # [1] Percentage of population that are adults
adult_phones = 0.81 # [2] Percentage of adult population that owns phones
weeks_in_year = 365.25/7 # Number of weeks in a year ~= 52

'''
This method calculates energy consumption in KWH and yearly cost in dollars for each person.
'''
def compileData(elements, hoursout):
  elements = int(elements * per_of_adults * adult_phones)
  global weeks_in_year

  # weekend
  if hoursout.all() == None:
    hoursout = np.asarray([random.uniform(0,10) for i in range(elements)])
    # People typically spend 0-10 hours outside of home on the weekends.

  for i in range(elements):
    weekday = phoneUsage.a_weekday(elements)
    weekend = phoneUsage.a_weekend(hours_spent=hoursout, num_elements=elements)

    recharge = energyConsumption.rechargeInstances(elements)
    battery = energyConsumption.batteryInstances(elements)

    weekendUsageDay = energyConsumption.usageDay(weekend, battery, recharge)
    weekdayUsageDay = energyConsumption.usageDay(weekday, battery, recharge)

    totalConsumption = energyConsumption.energyConsumption(weekdayUsageDay, weekendUsageDay, battery)
    
    weeklyCost = cost.cost(totalConsumption)
    yearlyCost = weeklyCost * weeks_in_year

    data = { "Recharging Point": recharge,
             "Battery Life": battery, 
             "Weekend Usage (per day)": weekendUsageDay,
             "Weekday Usage (per day)": weekdayUsageDay,
             "Total Energy Consumption (per person)": totalConsumption,
             "Total Yearly Cost (per person)": yearlyCost }

    df = pd.DataFrame(data)
    pd.DataFrame.to_csv(df, "SmartphoneCostPerPerson.csv")
    return df

##############
# REFERENCES #
##############

"""
[1]:https://www.census.gov/quickfacts/fact/table/US/PST045218
[2]:https://www.pewresearch.org/internet/fact-sheet/mobile/

"""
