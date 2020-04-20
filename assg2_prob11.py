import numpy as np 
import matplotlib.pyplot as plt

def f(t,u1,u2,u3):
    return (u1+2*u2-2*u3+np.exp(-t))
def g(t,u1,u2,u3):
    return (u2+u3-2*np.exp(-t))
def fg(t,u1,u2,u3):
	return (u1+2*u2+np.exp(-t))

h=0.001
a=0
b=1
n=int((b-a)/h)

u1_0=3
u2_0=-1
u3_0=1

t=np.linspace(a,b,n+1)

u1=[]
u2=[]
u3=[]

u1.append(u1_0)
u2.append(u2_0)
u3.append(u3_0)

for i in range(n):
    k1=h*f(t[i],u1[i],u2[i],u3[i])
    l1=h*g(t[i],u1[i],u2[i],u3[i])
    m1=h*fg(t[i],u1[i],u2[i],u3[i])
    k2=h*f(t[i]+h/2,u1[i]+k1/2,u2[i]+l1/2,u3[i]+m1/2)
    l2=h*g(t[i]+h/2,u1[i]+k1/2,u2[i]+l1/2,u3[i]+m1/2)
    m2=h*fg(t[i]+h/2,u1[i]+k1/2,u2[i]+l1/2,u3[i]+m1/2)
    k3=h*f(t[i]+h/2,u1[i]+k2/2,u2[i]+l2/2,u3[i]+m2/2)
    l3=h*g(t[i]+h/2,u1[i]+k2/2,u2[i]+l2/2,u3[i]+m2/2)
    m3=h*fg(t[i]+h/2,u1[i]+k2/2,u2[i]+l2/2,u3[i]+m2/2)
    k4=h*f(t[i]+h,u1[i]+k3,u2[i]+l3,u3[i]+m3)
    l4=h*g(t[i]+h,u1[i]+k3,u2[i]+l3,u3[i]+m3)
    m4=h*fg(t[i]+h,u1[i]+k3,u2[i]+l3,u3[i]+m3)
    u1_rk4=u1[i]+(k1+2*k2+2*k3+k4)/6
    u2_rk4=u2[i]+(l1+2*l2+2*l3+l4)/6
    u3_rk4=u3[i]+(m1+2*m2+2*m3+m4)/6
    u1.append(u1_rk4)
    u2.append(u2_rk4)
    u3.append(u3_rk4)


fig1,ax1=plt.subplots()
plt.plot(t,u1,'b')
ax1.set_xlabel('t')
ax1.set_ylabel('u1')

fig1,ax2=plt.subplots()
plt.plot(t,u2,'r')
ax2.set_xlabel('t')
ax2.set_ylabel('u2')

fig1,ax3=plt.subplots()
plt.plot(t,u3,'g')
ax3.set_xlabel('t')
ax3.set_ylabel('u3')

plt.show()

