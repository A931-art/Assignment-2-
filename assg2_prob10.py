import numpy as np
import matplotlib.pyplot as plt


def f(x,t):
    return 1/(x**2*(1-t)**2+t**2)

def rk4(w,t,h,i):
    k1 = h*f(w[i],t[i])
    k2 = h*f(w[i]+k1/2.0,t[i]+h/2.0)
    k3 = h*f(w[i]+k2/2.0,t[i]+h/2.0)
    k4 = h*f(w[i]+k3,t[i]+h)
    return  w[i]+(k1+2*k2+2*k3+k4)/6

h=float(input('Enter step size: '))
n=int((1/h)+1)
t=np.array([0])
w=np.zeros(1)

s=np.linspace(0,1,n-1)
y=np.zeros(s.size)

y[0]=1
flag=0
w[0]=1
hold=0

for i in range(0,n-2):
    y[i+1]=rk4(y,s,h,i)
i=0
while(flag==0):
    tem=rk4(w,t,h,i)
    if(flag==0):
        if((t[i])>=0.99999998):
            flag=1
            hold=w[i]
    w=np.append(w,tem)
    t=np.append(t,t[i]+h)
    i=i+1

for i in range(0,n-1):
    s[i]=s[i]/(1-s[i])
plt.plot(s,y,color = 'red')
plt.grid()
plt.show()

print('x at t = 3.5x10^6', 'is approximately: ',hold)
print(t.size)
print(y)
