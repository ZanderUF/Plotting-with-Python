## Generic Plotting Outline for rhovsenergy.out data
## 
## Author:  Zander Mausolff
## Usage:  python name_of_file.py
## Notes: Requires numpy and matplotlib 
## Tested with Python Python 2.7.9 --  64-bit

##----------------------------------------------------##
## These are the import statements
## "as" just allows you to make a short hand for numpy
## "numpy as np" is just a common comvention you can use 
##  anything you like
import os
import numpy as np
import matplotlib.pyplot as plt

##-------Change font to 'Times New Roman' throughout the plot---##
from matplotlib import rcParams
rcParams['font.family'] = 'serif'
rcParams['font.serif'] = ['Times New Roman']

##------Simplified file input--------#
## Usage:  just put the file name with your data in "file_name"
## 	   file must be in the directory where this script is.
 
current_dir = os.getcwd()
file_name = "the_name_of_your_file_here"
tdkeno_data = np.loadtxt(current_dir + "/" + file_name, skiprows=2)

#------- For CSV files (comma-delimited) -------#
#csv_data = np.genfromtxt('PATH TO CSV FILE',delimiter=',',usecols=(1,4,13))
## usecols(0,1,2) selects first 3 columns of your CSV, counting starts @ 0

#-------How to select the data you just imported--------#
## Rho file
time = tdkeno_data[:,0]  # corresponds to first column 
power = tdkeno_data[:,3] # fourth column
totPower=tdkeno_data[:,4] 
reactivity = tdkeno_data[:,5]

##---Normalize some parameter--##
total = np.sum(totPower)
normalize_power = totPower/total
x=0
norm_power = [x / total for x in totPower]

##----------------------------------------------------##
## Time to plot
## The data is conveniently just a list of numbers 
## So all you need to do is select which ones you want in your x,y

## GENERAL FORMAT (2D) :  plt.plot(X,Y,'color of line or dot,', label="label name",)
plt.plot(time,normalize_power,'-r',label='run 1')


## Paramters to change on the plot ##
plt.title('Pretty Cool Title')
## you can do things like change the scale ##
plt.xscale('log')  
#plt.yscale('log')

## change the limits of the plot
## Otherwise will show some default amount based on data
plt.xlim([0,8])  #-- Only changes the x 
## ---Configure the legend --- ##
plt.legend(loc='upper left',prop={'size':14},numpoints=1)

## make label for x,y axis
plt.xlabel('label (nice units kPa)')
plt.ylabel('label (nice units ergs/s)')

##---- This just shows a nice grid --#
plt.grid(True)

##-------!!!!!!!--------###
## Neeed to put the following or nothing will show up
plt.show()
