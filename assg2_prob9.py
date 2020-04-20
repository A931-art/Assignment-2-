import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import odeint

def f(t,x):
    return ((x**2+x)/t)
def g(x,t):
    return ((x**2+x)/t)
    
#initial condition
t = 1
x = -2
#initial step size
dt = 1e-1
#minimal step size
dt_min = 1e-3
#relative change tolerances
dx_max = 0.01  
dx_min = 0.008 
x_tol = 1e-3
X=[x]
T=[t]
while (t <= 3):
    k1 = f(t,x)
    k2=f(t+dt/2,x+dt*(k1/2))
    k3 = f(t+dt/2, x+dt*k2/2)
    k4 = f(t+dt,   x+dt*k3)
    step_x = x + dt/6*(k1+2*k2+2*k3+k4)

    k2 = f(t+dt/4, x+dt*k1/4)
    k3 = f(t+dt/4, x+dt*k2/4)
    k4 = f(t+dt/2, x+dt*k3/2)
    half_step_x = x + dt/12*(k1+2*k2+2*k3+k4)

    k2 = f(t+dt,   x+dt*k1)
    k3 = f(t+dt,   x+dt*k2)
    k4 = f(t+2*dt, x+2*dt*k3)
    dble_step_x = x + dt/3*(k1+2*k2+2*k3+k4)

    if (abs(step_x) < x_tol):
        if (dt != dt_min):
            print("New step size",dt_min)
            dt = dt_min
        new_x = step_x
    else:
        if (abs(step_x) > x_tol and abs(step_x-half_step_x)/abs(step_x) > dx_max):
            dt = dt/2
            print("New step size",dt)
            new_x = half_step_x
        elif (abs(step_x) > x_tol and abs(step_x-dble_step_x)/abs(step_x) < dx_min):
            dt = dt*2 
            print("New step size",dt)
            new_x = dble_step_x
        else:
            new_x = step_x # This is just right.

    x = new_x
    t = t + dt
    X.append(x)
    T.append(t)

X_true=odeint(g,X[0],T) 
E=np.zeros(len(X))

for i in range(len(X)):
    E[i]=(abs(X_true[i]-X[i])/X_true[i])

print('The absolute accuracy of the solution :',abs(sum(E)))
plt.plot(T,X,'g-o',label = 'Adaptive Step Size')
#plt.plot(T,X_true,'r-o',label = 'Actual')
plt.legend()
plt.show()
