import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import linregress
import numpy as np
import seaborn as sns

def draw_plot():
    # Read data from file
    df = pd.read_csv('epa-sea-level.csv')
    df.rename(columns = {'CSIRO Adjusted Sea Level':'CSIRO_Adjusted_Sea_Level'}, inplace = True)
    # Create scatter plot
    g = plt.figure(figsize = (15,15))
    years = np.arange(1880, 2051)
    plt.scatter(df['Year'], df['CSIRO_Adjusted_Sea_Level'])
    # Create first line of best fit
    slope, intercept, r, p, stand = linregress(df['Year'], df['CSIRO_Adjusted_Sea_Level'])
    line = [slope*x + intercept for x in years]   
    plt.plot(years, line)
    plt.xticks(np.arange(1850.0, 2076.0, step = 25))

  
    # Create second line of best fit
    df = df.loc[df['Year']>=2000]
    newyears = np.arange(2000, 2051)
    slope, intercept, r, p, stand = linregress(df['Year'], df['CSIRO_Adjusted_Sea_Level'])
    line = [slope*xi + intercept for xi in newyears]
    plt.plot(newyears,line)
    plt.xticks(np.arange(1850.0, 2076.0, step = 25))
  
    # Add labels and title
    plt.title('Rise in Sea Level')
    plt.xlabel('Year')
    plt.ylabel('Sea Level (inches)')
    
    # Save plot and return data for testing (DO NOT MODIFY)
    g.figure.savefig('sea_level_plot.png')
    return g.gca()
