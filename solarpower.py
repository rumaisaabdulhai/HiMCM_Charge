import numpy as np
import random
import pandas as pd

# Specifies the number of elements desired for dataset
num_elements = 1000000

# Cost of electricity per kwh (unit of energy)
regular_cost_per_kwh = 0.12

# Average cost of solar panels based on system size (amount_of_kwh)
amount_of_kwh = np.asarray([np.random.uniform(4.0, 20.0, num_elements)])

# Using Mathematica, the line of best fit for the data on 
# system size vs. solar cell installation cost was found
cost_of_install = (2093 * amount_of_kwh) + (2.1 * (10 ** -12)) 
# REF: https://news.energysage.com/how-much-does-the-average-solar-panel-installation-cost-in-the-u-s/

years = 2093/(365*0.12*24) # Break even point (see doc for derivation.) REFERENCE

total_solar_cost = cost_of_install # Assumption: The total solar cost only includes the installation expenses, and does include any maintenance expenses for the solar panels

kwh = amount_of_kwh * 24 * 365 * years # the total energy, in kwh, that the solar cell will provide to the building in a year.
solar_cost_per_kwh = np.divide(total_solar_cost, kwh)
regular_cost_per_kwh = 0.12
total_regular_cost = regular_cost_per_kwh * kwh

difference_in_total_cost = np.subtract(total_regular_cost, total_solar_cost)
print(difference_in_total_cost)

difference_in_cost_per_kwh = np.subtract(regular_cost_per_kwh, solar_cost_per_kwh)

def getValue():
  return "difference in total cost: " + str(difference_in_total_cost) + " | difference in cost per kwh: " + str(difference_in_cost_per_kwh)

def getData():
  data = {"Amount of KWH in solar cell": amount_of_kwh, "Solar Cell Installation Cost": total_solar_cost, "Total Energy Provided by the Cell":kwh, "Cost of Solar Cell per KWH": solar_cost_per_kwh, "Total Regular Cost": total_regular_cost, "Profit of Solar Cells (with cost)": difference_in_total_cost, "Profit of Solar Cells per KWH (with cost)": difference_in_cost_per_kwh}
  pd.DataFrame.to_csv(pd.Series(data).to_frame(), "SolarEnergySolution.csv")