## Generic Plotting Outline for rhovsenergy.out data
## 
## Author:  Zander Mausolff
## Usage:  python name_of_file.py
import os
import numpy as np
import matplotlib.pyplot as plt
import sys

##-------Change font to 'Palatino' throughout the plot---##
from matplotlib import rcParams
rcParams['font.family'] = 'serif'
rcParams['font.serif'] = ['Palatino']

##-------Check if user wants help w/cmd line options
arglist = str(sys.argv)
if "help" in arglist:
	print 'user wants help'
	print 'cmd line options are: \n r - plot reactivity \n n - normalize power \n xl - x log scale \n yl - y log scale \n fig - save figure as pdf \n s - plot figure in window'
	exit()	

##-------File names
k6file = "rho_k6-npg10k" 
file2 = "pkparm"
file3 = "power.out" 
arktranfile="arktran-td_16a3-data.csv"
##------Simplified file input--------#
current_dir = os.getcwd()
k6 = np.loadtxt(current_dir + "/" + k6file , skiprows=2)
try2 = np.loadtxt(current_dir + "/" + file2 , skiprows=2)
try3 = np.loadtxt(current_dir + "/" + file3 , skiprows=2)
##-----arktran data from csv file
arktran = np.genfromtxt(current_dir + "/" + arktranfile,skiprows=1, delimiter=',',usecols=(0,1))
time_ark=arktran[:,0]
power_ark=arktran[:,1]

reactivity1 = k6[:,5]
reactivity2 = try2[:,3]
time2= try2[:,1]

time1 = k6[:,0]
power1 = k6[:,3]

time3 = try3[:,0]
power3 = try3[:,1]
reactivity2 = try2[:,3]

powFirst = power1[0]
normPow = power1/powFirst

#--needed to save to pdf
f=plt.figure()

altcolor = 'lightgreen'
c8 = 'orange'
color4 = 'lightblue'

##------Evaluate command line
length = len(str(arglist[1]))
print 'Argument List:', arglist[length:]
##------If 'r' in cmd line arg, plt reactivity
if "r" in arglist[1:]:
	plt.plot(time1,reactivity1,label='new 16a3 npg=10k')
	plt.plot(time2,reactivity2,label='old k5')
	plt.ylabel('Reactivity [$]')
	name="reactivity"
##------Plot normalized power
if "n" in arglist[1:]:
	plt.plot(time_ark,power_ark,label='Arktran-td')
	plt.plot(time1,normPow,label='16a3')
	plt.plot(time3,power3,label='old k5')
	plt.ylabel('Relative Power')
	name="power"
#-------Have x log scale
if "xl" in arglist:
	plt.xscale('log')
#-------Have y log scale
if "yl" in arglist:
	plt.yscale('log')

## ---Configure the legend --- ##
plt.legend(loc='upper left',prop={'size':14},numpoints=1)

#plt.xlim([0,0.1])
plt.xlabel('Time [$s$]')
#plt.ylabel('Yield [$MJ$]')

if "fig" in arglist:
	f.savefig("./" + name + ".png")
if "s" in arglist:
	plt.show()
