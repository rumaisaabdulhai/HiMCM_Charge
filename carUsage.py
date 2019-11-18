import numpy as np
import pandas as pd

#############
# CONSTANTS #
#############

days_in_year = 365.25
weeks_in_year = 365.25/7 # Number of weeks in a year ~= 52

global num_elements

num_stations = 20021 # [1]
num_elements = 1000000 # [2]
cost_per_kwh = 0.12 # [3]

miles_per_year = 13476 # [4]
miles_per_day = miles_per_year / days_in_year
mu_1 = miles_per_day
sigma_1 = 5

kwh_per_mile = 0.34 # [5]
mu_2 = kwh_per_mile
sigma_2 = 0.05

###################
# COMPUTE METHODS #
###################

'''
This method generates a random sample of energy consumption per year for a number of num_elements people
'''
def get_kwh_per_year():
  kwh_per_mile = np.random.normal(mu_2, sigma_2, num_elements)
  miles_per_day = np.random.normal(mu_1, sigma_1, num_elements)

  miles_per_week = miles_per_day * 7
  kwh_per_week = np.multiply(miles_per_week, kwh_per_mile) # Energy Consumed per week

  kwh_per_year = kwh_per_week * weeks_in_year
  return kwh_per_year

'''
This method generates a random sample of cost per year for a number of num_elements people
'''
def get_cost_per_year():
  cost_per_year = get_kwh_per_year() * cost_per_kwh
  return cost_per_year

'''
This method calculates the total energy consumption per gas station
'''
def get_kwh_per_station():
  sum_kwh_per_year = np.sum(get_kwh_per_year()) / num_stations
  return sum_kwh_per_year

'''
This method calculates the total cost per gas station
'''
def get_cost_per_station():
  totalCostperGasStation = np.sum(get_cost_per_year()) / num_stations
  return totalCostperGasStation

def getStationData():
  df = pd.DataFrame({"KWH per Year": get_kwh_per_year(), "Cost per Year": get_cost_per_year()})
  pd.DataFrame.to_csv(df, "CarCostPerPerson.csv")

  print("Done!")
  return df

##############
# REFERENCES #
##############

"""
 [1]: Number of electric car charging stations in US from survey as of August 2019
 https://www.statista.com/statistics/416750/number-of-electric-vehicle-charging-stations-outlets-united-states/

 [2]: Estimated number of electric vehicles in US https://www.eei.org/resourcesandmedia/newsroom/Pages/Press%20Releases/EEI%20Celebrates%201%20Million%20Electric%20Vehicles%20on%20U-S-%20Roads.aspx

 [3]: Average cost per KWh
 https://www.npr.org/sections/money/2011/10/27/141766341/the-price-of-electricity-in-your-state

 [4]: Average miles per year
 https://www.autogravity.com/autogravitas/money/whats-average-miles-driven-per-year-car-lease-guide

 [5]: Average KWh per mile
 https://www.fueleconomy.gov/feg/PowerSearch.do?action=PowerSearch&year1=2010&year2=2020&minmsrpsel=0&maxmsrpsel=0&city=0&highway=0&combined=0&cbvtelectric=Electric&YearSel=2010-2020&MakeSel=&MarClassSel=&FuelTypeSel=&VehTypeSel=Electric&TranySel=&DriveTypeSel=&CylindersSel=&MpgSel=000&sortBy=Comb&Units=&url=SearchServlet&opt=new&minmsrp=0&maxmsrp=0&minmpg=&maxmpg=&rowLimit=10
"""
