import random
import numpy as np
import pandas as pd

#############
# CONSTANTS #
#############

num_elements = 1
cost_per_kwh = 0.12
kwh_per_hour = np.asarray([random.uniform(0.003,0.007) for i in range(num_elements)]) #at least for phones, from 3-7 W: https://www.bijlibachao.com/appliances/charging-a-mobile-phone-how-much-electricity-does-it-consume.html
cost_per_hour = cost_per_kwh/kwh_per_hour
price_per_hour = 0.05

annual_net_profit = (price_per_hour-cost_per_hour)*(365.25*24)

print(annual_net_profit)
