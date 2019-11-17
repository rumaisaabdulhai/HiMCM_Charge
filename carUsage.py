import numpy as np
import pandas as pd

#############
# CONSTANTS #
#############

chargingStations = 20021 # [1]
num_elements = 1000000 # [2]

avg_miles_per_year = 13476 # [3]
avg_miles_per_day = avg_miles_per_year / 365
mu_1 = avg_miles_per_day
variance_1 = 5
miles_per_day = np.random.normal(mu_1, variance_1, num_elements)

cost_per_kwh = 0.12 # [4]
mu_2 = 0.34 # [5]
variance_2 = 0.05
kwh_per_mile = np.random.normal(mu_2, variance_2, num_elements)

# Energy consumed per week
kwh_per_week = np.multiply(miles_per_day, kwh_per_mile) * 7

kwh_per_year = kwh_per_week * (365.25/7)

cost_per_year = kwh_per_year * cost_per_kwh
 
#Calculates yearly cost for ONE gas station with public charging facilities.
totalCostperGasStation = np.sum(cost_per_year) / chargingStations

def variables():
  return {"kwh_per_year": np.sum(kwh_per_year), "totalCostperGasStation": totalCostperGasStation}
  
def data():
  df = pd.DataFrame({"KWH per Year": kwh_per_year, "Cost per Year": cost_per_year})

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

 [3]: Average miles per year
 https://www.autogravity.com/autogravitas/money/whats-average-miles-driven-per-year-car-lease-guide

 [4]: Cost per KWh

 [5]: Average KWh per mile
 https://www.fueleconomy.gov/feg/PowerSearch.do?action=PowerSearch&year1=2010&year2=2020&minmsrpsel=0&maxmsrpsel=0&city=0&highway=0&combined=0&cbvtelectric=Electric&YearSel=2010-2020&MakeSel=&MarClassSel=&FuelTypeSel=&VehTypeSel=Electric&TranySel=&DriveTypeSel=&CylindersSel=&MpgSel=000&sortBy=Comb&Units=&url=SearchServlet&opt=new&minmsrp=0&maxmsrp=0&minmpg=&maxmpg=&rowLimit=10

"""
