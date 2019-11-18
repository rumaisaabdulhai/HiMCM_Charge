import numpy as np
import compiling
import random
import compUsage
import pandas as pd

#############
# CONSTANTS #
#############

num_elements = 1000000
per_of_adults = 0.55 # [1] Percentage of population that are adults
adult_phones = 0.81 # [2] Percentage of adult population that owns phones
weeks_in_year = 365.25/7 # Number of weeks in a year ~= 52
hours_spent = np.full((int(num_elements),), 10)
per_of_computers=0.73

                    ################## BEG OF CLASS ##################
class otherPlace:

  #############
  # CONSTANTS #
  #############

  global weeks_in_year
  global mean_low_battery
  
  weeks_in_year = 365.25/7 # Number of weeks in a year ~= 52
  
  # Assumption: You are equally likely to have 0% battery and 100% battery at a place.
  mean_low_battery = 0.20 # Average percentage of people who have a low phone battery

  ###############
  # CONSTRUCTOR #
  ###############

  def __init__(self, weekly_foot_traffic, avg_time_spent, deviation):
    self.weekly_foot_traffic = weekly_foot_traffic
    self.avg_time_spent = avg_time_spent # In hours
    self.deviation = deviation # Deviation of average time spent

  ####################
  # ACCESSOR METHODS #
  ####################
  

  def get_yearly_foot_traffic(self):
    """
    This method converts daily to yearly foot traffic and returns it.
    :return: int
    """
    return int(weeks_in_year * self.weekly_foot_traffic)


  def get_min_spent_time(self):
    """
    This method returns the minimum time spent at a certain place in hours.
    :return: float
    """
    return self.avg_time_spent - self.deviation


  def get_max_spent_time(self):
    """
    This method returns the maximum time spent at a certain place in hours.
    :return: float
    """
    return self.avg_time_spent + self.deviation
  
  '''
  
  '''
  def get_hours_spent(self):
    """
    This method generates various numbers of hours spent on the weekend for each person who visits a certain place for a year.
    :return: numpy array
    """
    min_time = self.get_min_spent_time()
    max_time = self.get_max_spent_time()

    need_to_charge = int(mean_low_battery * self.get_yearly_foot_traffic() * adult_phones * per_of_adults)

    hours_spent = np.asarray([random.uniform(min_time, max_time) for x in range(need_to_charge)])
    return hours_spent

  ###################
  # COMPUTE METHODS #
  ###################


  def PlacesCostSmartphones(self):
    """
    This method calculates the yearly cost for all people who need to charge their smartphones at a certain place.
    :return: float, DataFrame
    """

    foot_traffic = self.get_yearly_foot_traffic() * mean_low_battery * adult_phones * per_of_adults
    #This is the number of adults with phones that need to recharge their battery in a place.
    hours_spent = self.get_hours_spent()

    df = compiling.compileData(int(foot_traffic), hours_spent) # This is the yearly cost of charging smartphones per person.

    df["Hours Spent"] = hours_spent # adding hours spent as a new column to the data frame

    yearlyCost = np.sum(df["Total Yearly Cost (per person)"]) # What shop has to pay per year: Sum of (yearly cost per person)

    return yearlyCost, df


  def PlacesCostComputers(self):
    """
    This method calculates the yearly cost for all people who need to charge their computers at a certain place.
    :return: float, DataFrame
    """

    foot_traffic = self.get_yearly_foot_traffic() * mean_low_battery * per_of_computers * per_of_adults

    df = compUsage.getData(foot_traffic)
    yearlyCost = np.sum(df["Total Yearly Cost (per person)"])

    return yearlyCost, df

                    ################## END OF CLASS ##################

######################
# OBJ INITIALIZATION #
######################

mall = otherPlace(1000000/(365.25/7), 75195, 500)
airport = otherPlace(993.91, 3.33, 0.33)
library = otherPlace(3174.06, 2.0, 0.5)
coffee_shop = otherPlace(3333.33, 0.8, 0.7)

def getComputerSmartphoneData():
  pd.DataFrame.to_csv(mall.PlacesCostComputers()[1], "mallComputers.csv")
  pd.DataFrame.to_csv(airport.PlacesCostComputers()[1], "airportComputers.csv")
  pd.DataFrame.to_csv(library.PlacesCostComputers()[1], "libraryComputers.csv")
  pd.DataFrame.to_csv(coffee_shop.PlacesCostComputers()[1], "coffeeComputers.csv")

  pd.DataFrame.to_csv(mall.PlacesCostSmartphones()[1], "mallSmartphones.csv")
  pd.DataFrame.to_csv(airport.PlacesCostSmartphones()[1], "airportSmartphones.csv")
  pd.DataFrame.to_csv(library.PlacesCostSmartphones()[1], "librarySmartphones.csv")
  pd.DataFrame.to_csv(coffee_shop.PlacesCostSmartphones()[1], "coffeeSmartphones.csv")


##############
# REFERENCES #
##############

"""
Malls:
  hours spent= 135/60: time found in ICSC survey

Airports:
  Yearly Passengers in 2018, US: 1,018,339,442 (Page 6)
  https://www.faa.gov/air_traffic/by_the_numbers/media/Air_Traffic_by_the_Numbers_2019.pdf
  https://www.bts.dot.gov/content/number-us-airportsa

  Number of Private and Public airports in 2018, US: 19636

  1,018,339,442 yearly passengers / 19636 total number of airports = 51860.8393767 passengers per year

  51860.84 / (365.25/7) = 993.910679361 passengers per week

Libraries:
  num of libraries per year: 
  hour spent=2 based on statistics for a randomly sampled library (Portland, Maine)
  (https://libguides.ala.org/numberoflibraries), number of visits: (http://www.ala.org/tools/libfactsheets/alalibraryfactsheet06)

Coffee Shops:
  min(0.1) max(1.5) from average times spent in randomly selected coffee shops (Andover, MN Dunkin Donuts, Old California Coffee House and Eatery, in San Marcos California)
  #per starbucks per year 
  (https://yourbusiness.azcentral.com/average-number-patrons-coffee-shop-26736.html)
"""
