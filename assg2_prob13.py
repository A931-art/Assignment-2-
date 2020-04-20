import numpy as np
import matplotlib.pyplot as plt

def f(t,y,yp):
	return 2*yp/t-2*y/t**2+t*np.log(t)
def g(t,y,yp):
	return yp

tlist=[]
ylist=[]

t=1
y=1
yp=0
h=0.001

while(t<=2+h):
	tlist.append(t)
	ylist.append(y)
	y+=g(t,y,yp)*h
	yp+=f(t,y,yp)*h
	t+=h

T=np.array(tlist)
y_exact=7*T/4+0.5*T**3*np.log(T)-3/4*(T)**3

plt.scatter(tlist,ylist,s=70,facecolors='none',edgecolors='y',label="Numerical sol")
plt.plot(tlist,y_exact,label="Exact sol",color='k')
plt.xlabel('t')
plt.ylabel('y')
plt.grid()
plt.legend()
plt.show()
