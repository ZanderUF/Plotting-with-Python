#Purpose: Plotting QUENCH TREAT MODEL Data KENOVI vs. KENOVA for neutronics calculations
import numpy as np
import matplotlib.pyplot as plt

data = np.genfromtxt('/Users/macosx/Documents/UF_Research/INL_REPORT/PythonPlotting/quench_comp.csv',delimiter=',',usecols=(1,4,13))

#get the data 
x=data[:,0]
y1=data[:,1]
y2=data[:,2]

plt.axis([0,8,0,4000])
plt.plot(x,y1, '-',label='KENOVI')
plt.plot(x,y2,'-',label='KENOVa')
     
#Define Plot parameters                       
plt.title('Transient 2855')
plt.xlabel('Time (s)')
plt.ylabel('Power (MW)')
plt.legend(loc='upper right',prop={'size':14},numpoints=1)
plt.grid(True)

plt.show()