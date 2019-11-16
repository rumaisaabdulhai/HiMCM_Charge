import numpy as np
import pandas as pd

#############
# CONSTANTS #
#############

chargingStations = 20021 # Number of electric car charging stations in US from survey as of August 2019 (see References)
num_elements = 1000000 #Estimated number of electric vehicles in US, REFERENCE: https://www.eei.org/resourcesandmedia/newsroom/Pages/Press%20Releases/EEI%20Celebrates%201%20Million%20Electric%20Vehicles%20on%20U-S-%20Roads.aspx

mu_1 = 13476/365
sigma_1 = 5
miles_per_day = np.random.normal(mu_1, sigma_1, num_elements) # REFERENCE: https://www.autogravity.com/autogravitas/money/whats-average-miles-driven-per-year-car-lease-guide

cost_per_kwh = 0.12 # REFERENCE
mu2 = 0.34
sigma2 = 0.05
kwh_per_mile = np.random.normal(mu2, sigma2, num_elements)

# Energy Consumption Per Week
kwh_per_week = np.multiply(miles_per_day, kwh_per_mile) * 7

kwh_per_year = kwh_per_week * (365.25/7)

cost_per_year = kwh_per_year * cost_per_kwh
 
#Calculates yearly cost for ONE gas station with public charging facilities.
totalCostperGasStation = np.sum(cost_per_year) / chargingStations

def variables():
  return {"kwh_per_year":np.sum(kwh_per_year), "totalCostperGasStation":totalCostperGasStation}
  
def data():
  df = pd.DataFrame({"KWH per Year": kwh_per_year, "Cost per Year": cost_per_year})

  pd.DataFrame.to_csv(df, "CarCostPerPerson.csv")
  print("Done!")
  return df

"""
References:
#electric car charging: https://www.statista.com/statistics/416750/number-of-electric-vehicle-charging-stations-outlets-united-states/
"""
