import trapezium
import simpsons
import gauss

def func(x):
    y = 3*(x**2) + 2*x
    return y

val1 = trapezium.integration(-1,1,20,func)
val2 = simpsons.simpson(-1,1,20,func)
val3 = gauss.gaussian(-1,1,func)
print(val1,val2,val3)
