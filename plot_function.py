## Sample of plotting a function
## Author: Zander 
## Usage:  python plot_function.py
## Notes: requires numpy and matplotlib
## Tested with Python Python 2.7.9 --  64-bit

##----------------------------------------------------##
## These are the import statements
## "as" just allows you to make a short hand for numpy
## "numpy as np" is just a common comvention you can use 
##  anything you like
import numpy as np
import matplotlib.pyplot as plt

## Easy way to plot a function is to first generate an 
## list of numbers, which can be done as follows
x = np.linspace(0,1,1000)
## this will create a list(array) of 1000 numbers between 
## 0 and 100

## you can then feed that x into a function you are interested in plotting
#y = np.cos(x)
y = np.exp(x)


## TO plot just put x and y as such
plt.plot(x,y)


## --- DON't forget the plt.show() ----##
plt.show()
