import matplotlib.pyplot as plt
import compiling
import pandas as pd

df = compiling.compileData(1000000,10)
col1  = df["Total Energy Consumption (per person)"]
col2 = df["Total Yearly Cost (per person)"]

df.plot(kind='scatter',x="Total Energy Consumption (per person)",y="Total Yearly Cost (per person)",color='red')
# compiling.compileData(1000000,10)["Total Energy Consumption (per person)", "Total Yearly Cost (per person)"].plot(kind = 'scatter', x = "Total Energy Consumption (per person)", y = "Total Yearly Cost (per person)",color='red')
# plt.savefig("data.png")
plt.show()

##############
# REFERENCES #
##############
