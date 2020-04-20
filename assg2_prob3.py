import numpy as np
import matplotlib.pyplot as plt

#here we define dy/dx=f(x,y,z)=z
def f(x,y,z):
    return (z)

#here we define dz/dx=g(x,y,z)
def g(x,y,z):
    return (x*np.exp(x)-x+2*z-y)

h=0.025
a=0
b=1
y0=0
z0=0
n=int((b-a)/h)

x=np.linspace(a,b,n+1)

y1=[]
z1=[]
y1.append(y0)
z1.append(z0)

for i in range(n):
    k1=h*f(x[i],y1[i],z1[i])
    l1=h*g(x[i],y1[i],z1[i])
    k2=h*f(x[i]+h/2,y1[i]+k1/2,z1[i]+l1/2)
    l2=h*g(x[i]+h/2,y1[i]+k1/2,z1[i]+l1/2)
    yrk2=y1[i]+k2
    zrk2=z1[i]+l2
    z1.append(zrk2)
    y1.append(yrk2)

y2=[]
z2=[]
y2.append(y0)
z2.append(z0)

for i in range(n):
    k3=h*f(x[i],y2[i],z2[i])
    l3=h*g(x[i],y2[i],z2[i])
    k4=h*f(x[i]+h/2,y2[i]+k3/2,z2[i]+l3/2)
    l4=h*g(x[i]+h/2,y2[i]+k3/2,z2[i]+l3/2)
    k5=h*f(x[i]+h/2,y2[i]+k4/2,z2[i]+l4/2)
    l5=h*g(x[i]+h/2,y2[i]+k4/2,z2[i]+l4/2)
    k6=h*f(x[i]+h,y2[i]+k5,z2[i]+l5)
    l6=h*g(x[i]+h,y2[i]+k5,z2[i]+l5)
    yrk4=y2[i]+(1/6)*(k3+2*k4+2*k5+k6)
    zrk4=z2[i]+(1/6)*(k3+2*k4+2*k5+k6)
    z2.append(zrk4)
    y2.append(yrk4)

plt.xlabel('x')
plt.ylabel('y')
plt.plot(x,y1,color = 'g',label = 'RK2')
plt.plot(x,y2,color = 'r',label = 'RK4')
plt.legend()
plt.grid()
plt.show()

