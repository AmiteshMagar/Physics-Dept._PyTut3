import math
import numpy as np
import matplotlib.pyplot as plt

kb = 1.38e-23
eT=[]

Tc = int(input("Enter the value of Tc\n"))
T = np.arange(0,Tc+1,1)

def EnergyGap(t,tc):
    inn = 1 -(t/tc)
    r = 3.52*kb*tc * (math.sqrt(inn))
    return r

for t in T:
    eT.append(EnergyGap(t,Tc))

plt.plot(T,eT)
plt.show()

