import numpy as np
import matplotlib.pyplot as plt

def f(t,y):
    return ((y/t)-(y/t)**2)

h=0.1
a=1
b=2
n=int((b-a)/h)
y0=1

t=np.linspace(a,b,n+1)
y_t=t/(1+np.log(t))
y=[]
y.append(y0)
for i in range(n):
    Y=y[i]+f(t[i],y[i])*h
    y.append(Y)   

abs_err=sum(y_t-y)
print('Total absolute error = ',abs_err)

rel_err=sum((y_t-y)/y_t)
print('Total Relative error = ',rel_err)

plt.xlabel('t')
plt.ylabel('y')
plt.plot(t,y,color = 'g',label = 'Euler')
plt.plot(t,y_t,color = 'b',label = 'Analytical')
plt.legend()
plt.show()
