# Monte Carlo Pi estimator: 
# how it works :
#   randomly throwing points into a square and checking how many land inside a circle.

import random


points_in_circle = 0

amount_random_points = range(100_000, 10_000_000, 100_000)
increment = 0.01
index = 0
pi_approximation = 0
x_points = [] ## total points 
y_points = [] ## approxiamte pis
for n in amount_random_points:
    while index < n:
        x = random.uniform(-1.0, 1.00)
        y = random.uniform(-1.0, 1.00)
        if (x*x) +(y*y) <=1: 
            points_in_circle += 1

        index += 1
    
        pi_approximation = 4 * (points_in_circle / n)
    x_points.append(n)
    y_points.append(pi_approximation)




## visuallising what is going on 
import matplotlib.pyplot as plt

plt.plot(x_points, y_points)

plt.axhline(y=3.14159 , color='r', linestyle='-') # line shows where pi is
plt.show()