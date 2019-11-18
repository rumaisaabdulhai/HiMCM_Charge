import pandas as pd
import numpy as np
import cost
import energyConsumption
import phoneUsage
import random

#############
# CONSTANTS #
#############

num_elements = 100.0
per_of_adults = 0.55 # [1] Percentage of population that are adults
adult_phones = 0.81 # [2] Percentage of adult population that owns phones
weeks_in_year = 365.25/7 # Number of weeks in a year ~= 52

hours_spent = np.full((int(num_elements),), 10)

###################
# COMPUTE METHODS #
###################

def compileData(elements=num_elements, hoursout=hours_spent):
  """
  This method calculates energy consumption in KWH and yearly cost in dollars for each PERSON.
  :param elements: int
  :param hoursout: numpy array
  :return: pandas dataframe
  """

  global weeks_in_year
  elements = int(elements)

  for i in range(elements):
    weekday = phoneUsage.a_weekday(num_elements=elements)
    weekend = phoneUsage.a_weekend(hoursspent=hoursout, num_elements=elements)

    recharge = energyConsumption.rechargeInstances(elements)
    battery = energyConsumption.batteryInstances(elements)

    weekendUsageDay = energyConsumption.usageDay(weekend, battery, recharge)
    weekdayUsageDay = energyConsumption.usageDay(weekday, battery, recharge)

    totalConsumption = energyConsumption.energyConsumption(weekdayUsageDay, weekendUsageDay, battery)

    yearlyCost = cost.cost(totalConsumption)

    data = { "Recharging Point": recharge,
             "Battery Life": battery,
             "Weekend Usage (per day)": weekendUsageDay,
             "Weekday Usage (per day)": weekdayUsageDay,
             "Total Energy Consumption (per person)": totalConsumption,
             "Total Yearly Cost (per person)": yearlyCost }

    df = pd.DataFrame(data)
    pd.DataFrame.to_csv(df, "SmartphoneCostPerPerson.csv")
    return df

def compileDataPlaces(elements, hoursout):
    """
    This method calculates energy consumption in KWH and yearly cost in dollars for each PLACE. Remember that hoursout
    must have the same length as the interger value of elements.
    :param elements: int
    :param hoursout: numpy array
    :return: pandas dataframe
    """

    global weeks_in_year
    elements = int(elements)

    for i in range(elements):
        all_days = phoneUsage.a_weekend(hoursspent = hoursout, num_elements=elements)

        recharge = energyConsumption.rechargeInstances(elements)
        battery = energyConsumption.batteryInstances(elements)

        usageDays = energyConsumption.usageDay(all_days, battery, recharge)

        totalConsumption = energyConsumption.energyConsumption(usageDays, usageDays, battery)

        weeklyCost = cost.cost(totalConsumption)
        yearlyCost = weeklyCost * weeks_in_year

        data = {"Recharging Point": recharge,
                "Battery Life": battery,
                "Phone Usage (per day))": usageDays,
                "Total Energy Consumption (per person)": totalConsumption,
                "Total Yearly Cost (per person)": yearlyCost}

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
