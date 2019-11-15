import random
import numpy as np

''' 
This python file calculates the number of hours someone spends on their phone on a weekend or weekday. 
'''

#############
# CONSTANTS #
#############
num_elements = 100 # Specifies the number of elements desired for dataset
min_percent = 0.70 # [1]
med_percent = 0.25 # [1]
max_percent = 0.05 # [1]

#############
# VARIABLES #
#############
avg_week_clicks = 30 # [1]
val_range = 10 # chosen range
hours_spent = np.zeros((num_elements,1))
hours_spent = hours_spent.fill(10) # number of hours someone spends outside on a weekend

'''
This method calculates the number of times someone uses their phone on a weekend day.
'''
def weekend_picks(hours_spent):
    x = 58 * np.divide(hours_spent,24)
    # dividing by 24 to get the day ratio
    return x

'''
This method calculates the number of times
that a person looks at their phone on a weekday.
'''

def week_picks(num_elements, mode = 0, h = hours_spent):
  if (mode == 0): # if weekday
    wp = np.asarray([random.uniform(avg_week_clicks-val_range, avg_week_clicks + val_range) for i in range(num_elements)])
    return wp

  # if time left over, move statement to weekend picks
  elif (mode == 1): # if weekend
    picks = weekend_picks(h)
    wp = np.asarray([random.uniform(weekend_picks(h)[i] - val_range, weekend_picks(h)[i] + val_range) for i in range(num_elements) ])
    return wp

  else:
    print("Invalid Day.")

# Calculates required variables for calculating phone usage in a day

'''
This method calculates a small amount of time a person looks at their phone.  
'''
def min_time(num_elements, minrange = 0.5, maxrange = 2):
  min_time = np.asarray([np.random.uniform(minrange,maxrange) for i in range(num_elements)])
  return min_time

'''
This method calculates a medium amount of time a person looks at their phone.
'''
def med_time(num_elements, minrange = 2, maxrange = 10):
  med_time = np.asarray([np.random.uniform(minrange,maxrange) for i in range(num_elements)])
  return med_time

'''
This method calculates the maximum amount of time a person
'''
def max_time(num_elements, mu = 17, sigma = 1):
  max_time = np.random.normal(mu, sigma, num_elements)
  return max_time

'''
This method calculates the phone usage (P) per weekday or weekend day
'''
def phoneUsage(avgclicks, valrange, day, num_elements):
  week_pick = week_picks(num_elements, mode=day)
  mint = min_time(num_elements)
  medt = med_time(num_elements)
  maxt = max_time(num_elements)

  a = np.multiply(week_pick,mint) * min_percent
  b = np.multiply(week_pick,medt) * med_percent
  c = np.multiply(week_pick,maxt) * max_percent
  
  P = a + b + c

  return P

# Main Functions of the Program:
def weekday(num_elements = 100):
  return phoneUsage( avgclicks = avg_week_clicks, valrange = val_range, day = 0, num_elements = num_elements)

def weekend(hours_spent, num_elements = 100):
  return phoneUsage(avgclicks = np.average(weekend_picks(hours_spent)), valrange=val_range, day = 1, num_elements = num_elements)