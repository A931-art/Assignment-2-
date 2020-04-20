import numpy as np
import matplotlib.pyplot as plt

#dz/dx=-10=f(x,y)
def f(x,y):
    return (-10)

#dy/dx=z=g(x,z)
def g(x,z):
    return (z)


h=0.001
a=0
b=10
A=40
B=60

z0=np.linspace(A,B,B-A+1)
y0=0
n=int((b-a)/h)
x=np.linspace(a,b,n+1)
z=np.zeros((z0.size,x.size))  

for i in range(len(z0)):
        z1=[]
        z1.append(z0[i])
        for j in range(n):
            ze=z1[j]+f(x[j],z1[j])*h
            z1.append(ze)
        z[i]=z1
Y=np.zeros((z0.size,x.size))   

for i in range(z0.size):
    y=[]
    y.append(y0)
    for j in range(n):
        ye=y[j]+g(x[j],z[i][j])*h
        y.append(ye)
    Y[i]=y
    c=0

######### Use of numpy.argmin #########

s=[]
for i in range(z0.size):
    s.append(abs(Y[i][n]))
c=np.argmin(s,axis=0)

#######################################
'''
for i in range(z0.size):
    if(abs(Y[i][n]))<0.06:
        break
    c+=1
'''
print(c) 
print("z(0) =",z[c][0])

plt.xlabel('x')
plt.ylabel('y')
for k in [x for x in range(7,14) if x != 10]:
    plt.plot(x,Y[k],'--')
plt.plot(x,Y[10],color = 'k',label = 'y vs x_true')
plt.legend()
plt.show()

