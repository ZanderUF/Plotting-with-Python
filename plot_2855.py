## Author: Zander Mausolff
## Purpose:  Plotting 2855 Data

import numpy as np
import matplotlib.pyplot as plt

## import files with numpy's built in loadtxt function
## on Mac must specify full path (location to the file)
k6 = np.loadtxt("/Users/macosx/Documents/Plotting-with-Python", skiprows=2)
#k5 = np.loadtxt("/Users/zanderm/Documents/tdkeno_report/Results/2855/updated_2855/rho_k5", skiprows=2)

#kenovi rho file
time = k6[:,0]
power = k6[:,3] 
totPower=k6[:,4]
reactivity = k6[:,5]

#kenova rho file
#time2 = k5[:,0]
#power2 = k5[:,3] 
#totPower2=k5[:,4]
#reactivity2 = k5[:,5]


##Plot
##Power
plt.plot(time,power,'b',label='KENO-VI')
plt.plot(time2,power2,'-r', label='KENO V.a')


##Total Power
##plt.plot(time,totPower,'-b',label='kenovi')
##plt.plot(time2,totPower2,'-r', label='kenova')

##Reactivity
##plt.plot(time,reactivity,'-b',label='kenovi')
##plt.plot(time2,reactivity2,'-r', label='kenova')

#Yield
##plt.plot(time,reactivity,'-b',label='kenovi')
##plt.plot(time2,reactivity2,'-r', label='kenova')

## Plotting Parameters
plt.title('Transient 2856 Power Comparison of KENO-VI and KENO V.a')
#plt.xscale('log')  
plt.yscale('log')
plt.xlim([0,8])
plt.legend(loc='upper right',prop={'size':14},numpoints=1)
plt.grid(True)

plt.show()