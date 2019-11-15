import random
#need references for computers
day_screen_time = 2.21
# wh_per_hour = random.uniform(50,100)

wh_per_hour = np.asarray([random.uniform(50,100) for i in range(num_elements)])

cost_per_kwh= 0.12

cost_per_day = wh_per_hour * day_screen_time * cost_per_kwh / 1000
cost_per_year = cost_per_day * 365.25