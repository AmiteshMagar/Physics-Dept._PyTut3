import math
import numpy as np
import matplotlib.pyplot as plt

xRange=np.arange(-5,5,0.5)

def fact(x):
    pro =1
    if x==1 or x==0:
        return 1
    while (x>1):
        pro = pro*x
        x = x-1
    return pro
    
def Hermite(x,n):
    su =0
    if n%2==1:
        n=n+1
    else:
        n=n+2
    n1 = int(n/2)
    for s in range(n1):
        mult = math.pow(-1,s)
        mult = mult * math.pow((2*x),(n-2*s)) * fact(n)
        mult = mult / (fact(n-2*s) * fact(s))
        su =su + mult
    return su

values=[]
#enter the value for n here
n=1
for i in xRange:
    values.append(Hermite(i,n))

plt.plot(xRange,values,'r')
plt.show()
    
