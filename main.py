import phoneUsage
import energyConsumption
import cost
import compiling
import carUsage
import otherPlace
import compUsage
import solarPower
import random
import numpy as np

num_elements = int(1000000 * 0.55 * 0.81) # Number of adults with phones from sample
hours_spent = np.asarray([random.uniform(0,10) for i in range(num_elements)])

def main():
  compiling.compileData(num_elements, hours_spent)
  print("\n Analysis for Smartphone Yearly Energy Consumption and Cost Saved to File. \n")

  carUsage.getStationData()
  print("\n Analysis for Car Yearly Energy Consumption and Cost Saved to File. \n")

  compUsage.getData(num_elements)
  print("\n Analysis for Computer Yearly Energy Consumption and Cost Saved to File. \n")

  otherPlace.getComputerSmartphoneData()
  print("\n Analysis for Smartphone and Computer Yearly Energy Consumption and Cost in Airports, Libraries, Coffee Shops, and Malls Saved to File. \n")

  solarPower.variables()
  solarPower.data()
  print("\n Analysis for Solar Power Solution Saved to File. \n")

if __name__ == '__main__':
  main()
