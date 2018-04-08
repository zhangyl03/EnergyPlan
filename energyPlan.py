__author__ = 'zhangyl03'
#main file of EnergyPlan, optimization is done here

from scipy import optimize
import numpy as np

#price of electricity (RMB/kWh),
#from left to right is from: grid, solar, wind and heat
price = np.array([0.5, 1.0, 0.3, 1.0])

# initial guess
x0 = np.array([1,1,1,1])

# x denotes the amount of energy/resources needed; price is the unit price of the energy/resources
def economy(x):
    return x.dot(price)

def fun1(x):
    return 2 - x[2]

def fun2(x):
    return 7 - x[1]

def fun3(x):
    return sum(x) - 10

cons = ({'type': 'ineq', 'fun': fun1},\
        {'type': 'ineq', 'fun': fun2},\
        {'type': 'eq', 'fun': fun3})

# bds means the boundary of energy/natural resources amount
bds = ([0, None],[0, None],[0, None])

if __name__ == "__main__":
    res = optimize.minimize(economy, x0, method='SLSQP', constraints=cons, bounds=bds)
    print res