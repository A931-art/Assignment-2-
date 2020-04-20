from scipy.integrate import solve_bvp
import numpy as np
import matplotlib.pyplot as plt


def f1(x, y):
	return np.vstack((y[1], -np.exp(-2*y[0])))
def bc1(ya, yb):
	return np.array([ya[0], yb[0]-np.log(2)])

def f2(x, y):
	return np.vstack((y[1], y[1]*np.cos(x)-y[0]*np.log(y[0]) ))
def bc2(ya, yb):
	return np.array([ya[0]-1, yb[0]-np.exp(1)])

def f3(x, y):
	return np.vstack((y[1], -(2*y[1]**3+y[0]**2*y[1])*np.cos(x)**(-1) ))
def bc3(ya, yb):
	return np.array([ya[0]-2**(-1/4), yb[0]-np.sqrt(np.sqrt(3)/2)])

def f4(x, y):
	return np.vstack((y[1], 0.5*(1-y[1]**2-y[0]*np.sin(x))  ))
def bc4(ya, yb):
	return np.array([ya[0]-2, yb[0]-2 ])

########################################################

a=1;b=2;f=f1;y0=0;bc=bc1
x = np.linspace(a, b)
yd = np.zeros((2, x.size))
yd[0]=y0
sol =solve_bvp(f, bc, x, yd)
y = np.log(x) #Analytical solution
plt.subplots()
plt.plot(x,sol.sol(x)[0],'tab:orange',x,y,'g')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(['solve_bvp','Analytical'])
plt.grid()
plt.text(1.6, 0.2, r"$y''=-e^{-2x}$")

########################################################

a=0;b=np.pi/2;f=f2;y0=1;bc=bc2
x = np.linspace(a, b)
yd = np.zeros((2, x.size))
yd[0]=y0
sol =solve_bvp(f, bc, x, yd)
y = np.exp(np.sin(x)) #Analytical solution
plt.subplots()
plt.plot(x,sol.sol(x)[0],'tab:orange',x,y,'r')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(['solve_bvp','Analytical'])
plt.grid()
plt.text(0.5, 1.5, r"$y''=y'\cos x-y\ln y$")

##############################################################

a=np.pi/4;b=np.pi/3;f=f3;y0=2**(-1/4);bc=bc3
x = np.linspace(a, b)
yd = np.zeros((2, x.size))
yd[0]=y0
sol =solve_bvp(f, bc, x, yd)
y = np.sqrt(np.sin(x)) #Analytical solution
plt.subplots()
plt.plot(x,sol.sol(x)[0],'tab:orange',x,y,'y')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(['solve_bvp','Analytical'])
plt.grid()
plt.text(0.85, 0.86, r"$y''=-(2y'^3+y^2y')\sec(x)$")

#################################################################

a=0;b=np.pi;f=f4;y0=2;bc=bc4
x = np.linspace(a, b)
yd = np.zeros((2, x.size))
yd[0]=y0
sol =solve_bvp(f, bc, x, yd)
y = np.sin(x)+2 #Analytical solution
plt.subplots()
plt.plot(x,sol.sol(x)[0],'tab:orange',x,y,'b')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(['solve_bvp','Analytical'])
plt.grid()
plt.text(1.5, 2.1, r"$y''=\frac{1}{2}-\frac{y'^2}{2}-y \ \frac{\sin(x)}{2}$")
plt.show()
