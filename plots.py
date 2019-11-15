import matplotlib.pyplot as plt
import compiling
import pandas as pd

compiling.df.[:,:-2].plot(kind='scatter',x='num_children',y='num_pets',color='red')
plt.savefig("data")