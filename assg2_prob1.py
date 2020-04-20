import numpy as np
import matplotlib.pyplot as plt

def f(x,y):
    return (-9*y)
def g(x,y):
    return (-20*(y-x)**2+2*x)

h=0.0001
a=0
b=1
n=int((b-a)/h)

y0_1=np.exp(1)
y0_2=1/3

x=np.linspace(a,b,n+1)

y1=[]
y1.append(y0_1)
for i in range(n):
    y=y1[i]/(1+9*h)
    y1.append(y)


y2=[]
y2.append(y0_2)
for i in range(n):
    y=(-1+40*h**2*(1+i)+np.sqrt(1-80*h**2*(1+i)+160*h**3*(1+i)+80*h*y2[i]))/(40*h)  
    y2.append(y)

fig1,ax1=plt.subplots()
plt.plot(x,y1,'r')
ax1.set_xlabel('x')
ax1.set_ylabel('y')

fig2,ax2=plt.subplots()
plt.plot(x,y2,'g')
ax2.set_xlabel('x')
ax2.set_ylabel('y')

plt.show()
