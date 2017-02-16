from math import sqrt, log, exp, erf
import random
from numpy import arange
from scipy.stats import norm
import matplotlib.pyplot as plt



S0 = 100.0 # S0 = Stock price
strikes = arange(50,150,1) # Exercise pricesrange
T = 1.0 # T = Time to expiration
r = 0.01 # r = risk-free interest rate
q = 0.02 # q = dividend yield
vol = 0.2 # vol = volatility
Nsteps = 100 # Number or steps in MC


def bs_solver( S, K, T, r, q, sig):

    #Compute D1
    D1 = (log( S / K ) + (r - q + (sig) / 2.0) * T) / ( sig * sqrt(T))

    #Compute D2
    D2 = D1 - sig * sqrt(T)

    return S * norm.cdf(D1) - K * exp(- r * T) * norm.cdf(D2)


#---------------------


C = bs_solver(S0, strikes, T, r, q, vol)

print('The option price = ' + C )