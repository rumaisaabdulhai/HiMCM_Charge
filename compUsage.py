import random
import numpy as np
import pandas as pd

#############
# CONSTANTS #
#############

days_in_year = 365.25
adults_w_laptops = 0.73 # [1]
num_elements = int(1000000 * adults_w_laptops)

day_screen_time = 2.21 # [2]

w_per_hour = np.asarray([random.uniform(50,100) for i in range(num_elements)])
cost_per_kwh = 0.12 # [3]

kw_per_hour = w_per_hour / 1000 # Metric conversion
cost_per_day = kw_per_hour * day_screen_time * cost_per_kwh
cost_per_year = cost_per_day * days_in_year

###################
# COMPUTE METHODS #
###################

'''
This method calculates...
'''
def getData(numel = num_elements):

  numel = int(numel)
  
  day_screen_time = 2.21 # hours
  w_per_hour = np.asarray([random.uniform(50,100) for i in range(numel)])

  cost_per_kwh = 0.12

  cost_per_day = w_per_hour * (day_screen_time * cost_per_kwh / 1000)
  cost_per_year = cost_per_day * 365.25

  data = {"WH Per Hour": w_per_hour,"Total Yearly Cost (per person)": cost_per_year}

  df = pd.DataFrame(data)
  pd.DataFrame.to_csv(df, "CompUsage.csv")
  
  return df

'''
This method calculates...
'''
def data():
  data = {"WH Per Hour": w_per_hour,"Cost Per Year": cost_per_year}
  df = pd.DataFrame(data)
  pd.DataFrame.to_csv(df, "CompUsage.csv")

  return df

##############
# REFERENCES #
##############

'''
[1]: 73% of adults own laptops as of February 2019 https://www.statista.com/statistics/756054/united-states-adults-desktop-laptop-ownership/

[2]:

[3]: Average Cost per KWh
https://www.npr.org/sections/money/2011/10/27/141766341/the-price-of-electricity-in-your-state

'''
