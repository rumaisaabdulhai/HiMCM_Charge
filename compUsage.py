import random
import numpy as np
import pandas as pd

#############
# CONSTANTS #
#############

num_elements = int(1000000 * 0.73) # 73% of adults own laptops as of February 2019 https://www.statista.com/statistics/756054/united-states-adults-desktop-laptop-ownership/

day_screen_time = 2.21 # hours
w_per_hour = np.asarray([random.uniform(50,100) for i in range(num_elements)])

cost_per_kwh = 0.12

cost_per_day = w_per_hour * (day_screen_time * cost_per_kwh / 1000)
cost_per_year = cost_per_day * 365.25

def getData(numel = num_elements):

  numel = int(numel)
  
  day_screen_time = 2.21 # hours
  w_per_hour = np.asarray([random.uniform(50,100) for i in range(num_elements)])

  cost_per_kwh = 0.12

  cost_per_day = w_per_hour * (day_screen_time * cost_per_kwh / 1000)
  cost_per_year = cost_per_day * 365.25

  data = {"WH Per Hour": w_per_hour,"Cost Per Year": cost_per_year}

  df = pd.DataFrame(data)
  pd.DataFrame.to_csv(df, "CompUsage.csv")
  
  return df

def data():
  data = {"WH Per Hour": w_per_hour,"Cost Per Year": cost_per_year}
  df = pd.DataFrame(data)
  pd.DataFrame.to_csv(df, "CompUsage.csv")

  return df
