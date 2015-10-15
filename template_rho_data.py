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
import numpy as np
import matplotlib.pyplot as plt

##-----------Import plain txt-------------------------##
## import files with numpy's built in loadtxt function
## on Mac must specify full path (location to the file)
## np.loadtxt works better for plain text files
tdkeno_data = np.loadtxt("/Users/macosx/Documents/Plotting-with-Python/test_rho", skiprows=2)
## skip rows just skips the first two rows of your file
## GENERAL ---> k6 = np.loadtxt("PATH TO FILE", skiprows=2)

#------- For CSV files (comma-delimited) -------#
#csv_data = np.genfromtxt('PATH TO CSV FILE',delimiter=',',usecols=(1,4,13))
## usecols(0,1,2) selects first 3 columns of your CSV, counting starts @ 0

#-------How to select the data you just imported--------#
## Rho file
time = tdkeno_data[:,0]  # corresponds to first row
power = tdkeno_data[:,3] # fourth row
totPower=tdkeno_data[:,4] 
reactivity = tdkeno_data[:,5]

##----------------------------------------------------##
## Time to plot
## The data is conveniently just a list of numbers 
## So all you need to do is select which ones you want in your x,y

## GENERAL FORMAT (2D) :  plt.plot(X,Y,'color of line or dot,', label="label name",)
plt.plot(time,power,'-r',label='run 1')


## Paramters to change on the plot ##
plt.title('Pretty Cool Title')
## you can do things like change the scale ##
plt.xscale('log')  
plt.yscale('log')

## change the limits of the plot
## Otherwise will show some default amount based on data
plt.xlim([0,8])  #-- Only changes the x 
## ---Configure the legend --- ##
plt.legend(loc='upper right',prop={'size':14},numpoints=1)

##---- This just shows a nice grid --#
plt.grid(True)

##-------!!!!!!!--------###
## Neeed to put the following or nothing will show up
plt.show()
