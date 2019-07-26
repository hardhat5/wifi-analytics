import numpy as np
from scipy.optimize import minimize
import math

# coordinates of the three routers
locations = [(0,0), (4,0), (0,4)]

# distances of the mobile phone from the three routers
distances = [5.66, 4, 4]

min_index = distances.index(min(distances))
initial_point = locations[min_index]

def mse(x, locations, distances):
    mse = 0.0
    for location, distance in zip(locations, distances):
        distance_calculated = math.sqrt((x[0]-location[0])**2 + (x[1]-location[1])**2)
        mse += math.pow(distance_calculated - distance, 2.0)
    return mse/3

result = minimize(
    mse,
    initial_point,
    args = (locations, distances),
    method = 'L-BFGS-B',
    options = {
    'ftol':1e-5,
    'maxiter': 1e+7
    })

print(result.x)
