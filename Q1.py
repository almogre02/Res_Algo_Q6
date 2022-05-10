import pandas as pd
import numpy as np
import pylab
import matplotlib.pyplot as plt
from scipy.optimize import fsolve

# I got help from the site "pythonpool.com" and at the hint of the lecturer

''' Helper function which checks if fsolve returned the intersection dots '''
def helperFunction(max_dot, min_dot, temp_sol)->bool:
    if(temp_sol[0]<=max_dot and temp_sol[0]>=min_dot):
        if(temp_sol[-1] == 'The solution converged.'):
            return True
    return False

def plotIntersection(x_linspace, f, g):
    '''
    :param x_linspace: Range of X values
    :param f: First function
    :param g: Second function
    :return: Displays the points of intersection between the two functions
    '''
    plt.plot(x_linspace, f(x_linspace), x_linspace, g(x_linspace))
    intersection_function = lambda x : f(x) - g(x)

    for x0 in x_linspace:
        intersection_dots = fsolve(intersection_function, x0, full_output=True)
        max_dot = max(x_linspace)
        min_dot = min(x_linspace)
        if(helperFunction(max_dot, min_dot, intersection_dots)):
            plt.plot(intersection_dots[0], g(intersection_dots[0]), 'ro', zorder=3)

    ''' Plots the Intersection - the red dots'''
    plt.title("Plot Intersection")
    plt.xlabel("X Axis")
    plt.ylabel("Y Axis")
    plt.grid()
    plt.show()



if __name__ == "__main__":
    ''' Running examples '''
    f = lambda x: x**2
    g = lambda x: x+10
    plotIntersection(np.linspace(-10, 10, 1000), f, g)

    f = lambda x : np.sin(x)
    g = lambda x : 0.2*x
    plotIntersection(np.linspace(-10, 10, 1000), f, g)

    f = lambda x : np.tan(x)
    g = lambda x : x-13
    plotIntersection(np.linspace(-10, 10, 1000), f, g)

    f = lambda x: np.cos(x)
    g = lambda x: x**3
    plotIntersection(np.linspace(-10, 10, 1000), f, g)

    f = lambda x: x/3
    g = lambda x: np.sin(x)
    plotIntersection(np.linspace(-10, 10, 1000), f, g)

