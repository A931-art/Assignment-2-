import numpy as np
import matplotlib.pyplot as plt

h=0.1
A=0
B=10
n=int((B-A)/h)

a=np.zeros((n,n))
for i in range(1, n-1):
    a[i][i]=-2
    a[i][i-1]=1
    a[i][i+1]=1
a[0][0]=-2
a[0][1]=1
a[n-1][n-2]=1
a[n-1][n-1]=-2

b=-10*h**2*np.ones(n)

N = len(a)
x = np.zeros(N)
w=1.8
N = len(a)
x1_true=np.linalg.solve(a,b)
x_true=np.zeros(n+2)
for i in range(1,n+1):
    x_true[i]=x1_true[i-1]

#Relaxation Method
T=np.zeros(N)
R=np.zeros(N)
N1=1000
x_arr=np.zeros((N1,N))
c=0
for i in range(N1):             
    for j in range(0, N):         
        d = b[j]                   
        for k in range(N):      
            if(j != k): 
                d-=a[j][k]*x[k] 
        x[j] = w*(d/a[j][j])+(1-w)*x[j]
        T[j]=abs(x[j]-R[j])
        R[j]=x[j]
        x_arr[i][j]=x[j]
    if(all(m <= 0.01 for m in T)):
    	break
    c+=1

X=np.zeros((c,n+2))

print(c)
for i in range(0,c):
    for j in range(1,n+1):
        X[i][j]=x_arr[i][j-1]
t=np.linspace(0,B,n+2)
for k in [10,20,50,100,150,200,250,300]:
    plt.plot(t,X[k],'--')
plt.xlabel('x')
plt.ylabel('y')
plt.plot(t,X[c-1],color = 'r',label = 'Numerical')
plt.plot(t,x_true,color = 'g',label = 'Exact')
plt.legend()
plt.grid()
plt.show()

