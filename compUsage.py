import random
import numpy as np
import pandas as pd
# need references for computers

num_elements = int(1000000 *0.73) # 73% of adults own laptops as of February 2019 https://www.statista.com/statistics/756054/united-states-adults-desktop-laptop-ownership/

day_screen_time = 2.21
# wh_per_hour = random.uniform(50,100)
wh_per_hour = np.asarray([random.uniform(50,100) for i in range(num_elements)])

wh_per_hour = wh_per_hour*24*365.25
cost_per_kwh= 0.12

cost_per_day = wh_per_hour * (day_screen_time * cost_per_kwh / 1000)
cost_per_year = cost_per_day * 365.25

def data():
  df = pd.DataFrame({"WH Per Hour": wh_per_hour,"Cost Per Year": cost_per_year})

  pd.DataFrame(df, "CompUsage.csv")
  return df