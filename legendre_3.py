
#legendre polynomial
#(3) (2*n+1)*P(n,x) = P'(n+1)-P'(n-1)

import numpy as np
from scipy.special import legendre
from scipy.misc import derivative

x=float(input("Enter the x: "))
n=int(input("enter the n: "))

def f(x):
    return legendre(n-1)(x)
def g(x):
    return legendre(n+1)(x)

LHS=(2*n+1)*legendre(n)(x)
RHS=derivative(g,x,order=15)-derivative(f,x,order=15)
print("LHS: ",LHS)
print("RHS: ",RHS)
