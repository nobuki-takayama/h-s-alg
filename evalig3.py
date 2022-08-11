# On Ubutun 20.04 do pip install scipy -U --user
import numpy as np
from scipy.integrate import solve_ivp
import matplotlib.pyplot as plt
import scipy.special as ss

# df : degree of freedom 
# n  : approx degree

# evalig3.py
# Use differential equation for exp(x/2)*x^(-df/2)*gamma(x)
def igs_(x,df,n):
    s = 1
    for k in range(1,n+1):
        s = s+(x/2)**k/ss.poch(df/2+1,k)
    return s/(df/2)
def igs1_(x,df,n):
    s = 0
    for k in range(1,n+1):
        s = s+(1/2)*k*(x/2)**(k-1)/ss.poch(df/2+1,k)
    return s/(df/2)
def igsys(x,y,df,dummy1):
  return [y[1],y[0]/(2*x)+(-1/x)*(df/2+1-x/2)*y[1]]
def ig_(x1,df):
  x0=1;  n=40
  iv=[igs_(x0,df,n),igs1_(x0,df,n)]
  sol = solve_ivp(igsys,[x0,x1],iv,args=(df,0),method="RK45",dense_output="True", rtol=1e-7)
  x=np.linspace(x0,x1,100)
  z = sol.sol(x)
  #plt.gca().clear(); plt.plot(x,z[0].T); plt.show()
  return [x,z[0].T]

def ig(x,df):
   xlist,zlist=ig_(x,df)
   gamma=zlist*np.exp(-xlist/2)*(xlist**(df/2))
   return [xlist,gamma]
x,g=ig(70,50)
print([x[-1],g[-1]])




