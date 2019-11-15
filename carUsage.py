import numpy as np

#CONSTANTS
chargingStations = 20021 #Number of electric car charging stations from survey as of August 2019 (see References)

num_elements = 10000
miles_per_day = 40
# kwh_per_mile = 30/100
cost_per_kwh= 0.12

mu = .34
sigma = .10
kwh_per_mile = np.random.normal(mu, sigma, num_elements)

kwh_per_week = miles_per_day * 7 * kwh_per_mile
cost_per_year = kwh_per_week * (365.25/7) * cost_per_kwh

def yearlyCost(totalCost): #Calculates yearly cost for ONE gas station with public charging facilities.
  cost = totalCost/chargingStations
# print(kwh_per_mile)
# print(cost_per_year)

"""
References:

#electric car charging: https://www.statista.com/statistics/416750/number-of-electric-vehicle-charging-stations-outlets-united-states/
"""