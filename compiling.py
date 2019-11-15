import pandas as pd
import numpy as np
import cost
import energyConsumption
import phoneUsage

#numpy arrays (current day): recharge point, battery life, weekend usage per day, weeday usage per day, total energy consumption (per person), total cost (per person).

adultPhones = int(39.56*1000000*0.55*0.81)

# def statistics(DataFrame):
#   stats = np.zeros(1,67)
#   for i in range(67):

def compileData(elements, hoursout=10):
  if hoursout == 10:
    hoursout = np.asarray([random.uniform(0,10) for i in range(elements)])
    #People typically spend 0-10 hours outside of home on the weekends.

  for i in range(adultPhones):
    weekday = phoneUsage.weekday(numel=elements)
    weekend = phoneUsage.weekend(hoursspent=hoursout, numel=elements)

    recharge = energyConsumption.recharge(elements)
    battery = energyConsumption.batteryLife(elements)

    weekendUsageDay = energyConsumption.usageDay(weekend, battery, recharge)
    weekdayUsageDay = energyConsumption.usageDay(weekday, battery, recharge)

    totalConsumption = energyConsumption.energyConsumption(weekdayUsageDay, weekendUsageDay, battery)
    
    weeklyCost = cost.cost(totalConsumption)
    yearlyCost = weeklyCost*52

    data = {"Recharging Point": recharge, "Battery Life": battery, "Weekend Usage (per day)": weekendUsageDay,
              "Weekday Usage (per day)": weekdayUsageDay, "Total Energy Consumption (per person)": totalConsumption,
              "Total Yearly Cost (per person)": yearlyCost}

    header = {"Recharging Point", "Battery Liefe", "Weekend Usage (per day)", "Weekday Usage (per day)",
                "Total Energy Consumption (per person)", "Total Cost (per person)"}

    df = pd.DataFrame(data)
    print("Done!")
    pd.DataFrame.to_csv(df, "SmartphoneCostPerPerson.csv")

    # stats = statistics(df)
    # pd.DataFrame.to_csv(stats, "SmartphoneCostPerPersonStats.csv")
    return df

def compileDataPlaces(elements, hoursout=10):
  if (hoursout.all() == 10):
    hoursout = np.asarray([random.uniform(0,10) for i in range(elements)])
    #People typically spend 0-10 hours outside of home on the weekends.

  for i in range(adultPhones):

    weekend = phoneUsage.weekend(hoursspent=hoursout, numel=elements)

    recharge = energyConsumption.recharge(elements)
    battery = energyConsumption.batteryLife(elements)

    weekendUsageDay = energyConsumption.usageDay(weekend,battery, recharge)
  
    totalConsumption = energyConsumption.energyConsumptionPlaces(weekendUsageDay, battery=battery)
    
    weeklyCost = cost.cost(totalConsumption)
    yearlyCost = weeklyCost*52

    data = {"Recharging Point": recharge, "Battery Life": battery, "Weekend Usage (per day)": weekendUsageDay, "Total Energy Consumption (per person)": totalConsumption, "Total Yearly Cost (per person)": yearlyCost}

    header = {"Recharging Point", "Battery Liefe", "Weekend Usage (per day)", "Weekday Usage (per day)",
                "Total Energy Consumption (per person)", "Total Cost (per person)"}

    df = pd.DataFrame(data)
    print("Done!")
    pd.DataFrame.to_csv(df, "SmartphoneCostPerPersonTest.csv")

    # stats = statistics(df)
    # pd.DataFrame.to_csv(stats, "SmartphoneCostPerPersonStats.csv")

    return df.iloc[:,-1]