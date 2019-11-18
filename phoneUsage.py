import random
import numpy as np

''' 
This python file calculates the total time spent in minutes using the phone for one day.
'''

#############
# CONSTANTS #
#############

num_elements = 1000000 # Specifies the number of elements desired for dataset
min_percent = 0.70 # [1]
med_percent = 0.25 # [1]
max_percent = 0.05 # [1]

#############
# VARIABLES #
#############

avg_week_clicks = 30 # [1]
clicks_deviation = 10
hours_spent = np.full( (num_elements,1) , 10)

###################
# COMPUTE METHODS #
###################

def get_hours_spent(num_elements, mint = 0, maxt = 10):
  """
  Generates a random sample of hours spent outside of home for a person on a day on the weekend.

  :param num_elements: int (number of samples)
  :param min: int
  :param max: int
  :return: numpy array
  """

  hoursspent = np.asarray([random.uniform(mint, maxt) for i in range(num_elements)])
  return hoursspent

def week_picks(num_elements, mode=True, h=hours_spent):
  num_elements = int(num_elements)
  """
  This method calculates the number of times
  that a person looks at their phone on a weekday or weekend.

  :param num_elements: int (number of samples)
  :param mode: int (whether the number of times is calculated for weekdays or weekends (True for weekdays)
  :param h: numpy array (number of hours spent on phone for each sample)
  :return: numpy array (number of times phone was used for each sample)
  """
  if (mode == True): # if weekday
    min = avg_week_clicks - clicks_deviation
    max = avg_week_clicks + clicks_deviation

    wp = np.asarray([random.uniform(min, max) for i in range(num_elements)])
    return wp

  # if time left over, move statement to weekend picks
  else: # if weekend
    wp = 58 * np.divide(h, 24)  # dividing by 24 to get the hours to day ratio
    return wp


# Calculates required variables for calculating phone usage in a day

def min_time(num_elements, minrange = 0.5, maxrange = 2):
  """
  This method calculates a small amount of time a person looks at their phone.
  :param num_elements: int (number of samples)
  :param minrange: int
  :param maxrange: int
  :return: numpy array
  """
  min_time = np.asarray([np.random.uniform(minrange,maxrange) for i in range(num_elements)])
  return min_time

def med_time(num_elements, minrange = 2, maxrange = 10):
  """
  This method calculates a medium amount of time a person looks at their phone.
  :param num_elements: int (number of samples)
  :param minrange: int
  :param maxrange: int
  :return: numpy array
  """
  med_time = np.asarray([np.random.uniform(minrange,maxrange) for i in range(num_elements)])
  return med_time

def max_time(num_elements, mu = 17, sigma = 4):
  """
  This method calculates the maximum amount of time a person looks at their phone.
  An array with the maximum time a person spends looking at their phone per day is generated with random values
  with mean 17 minutes and a standard deviation of 4 minutes
  :param num_elements: int
  :param mu: int
  :param sigma: int
  :return: numpy array
  """
  max_time = np.random.normal(mu, sigma, num_elements)
  return max_time

'''
This method calculates the phone usage (P) per weekday or weekend day
'''
def phoneUsage(hoursspent, num_elements = 1, day = True):
  """
  This method calculates the total time a person spends using their phone in minutes per day.
  :param hoursspent:
  :param num_elements:
  :param day:
  :return:
  """

  week_pick = week_picks(num_elements=num_elements, mode=day, h=hoursspent)
  mint = min_time(num_elements)
  medt = med_time(num_elements)
  maxt = max_time(num_elements)

  a = np.multiply(week_pick,mint) * min_percent
  b = np.multiply(week_pick,medt) * med_percent
  c = np.multiply(week_pick,maxt) * max_percent

  P = np.add(np.add(a, b), c)

  return P

'''
**** Main Functions of the Program ****
'''
def a_weekday(hoursspent=hours_spent, num_elements=100):
  return phoneUsage(hoursspent=hoursspent, day = True, num_elements = num_elements)

def a_weekend(hoursspent, num_elements = 100):
  return phoneUsage(hoursspent = hoursspent, day = False, num_elements = num_elements)

##############
# REFERENCES #
##############

'''
[1]: Phone Usage data:
https://blog.rescuetime.com/screen-time-stats-2018/
'''
