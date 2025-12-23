"""
Project 1: System of Linear ODEs Solver

This is my first project for practicing what I've learned over the break. 
This program will take a 2x2 system of linear differetial equations and solve and graph it.

Current issues:
- Scaling of the plot at the end
- Repeated and Complex Eigenvalues



"""
import numpy as np
import matplotlib.pyplot as plt

print("x' = ax + by")
print("y' = cx + dy")
"""
a = int(input("a: "))
b = int(input("b: "))
c = int(input("c: "))
d = int(input("d: "))
"""

a = 3
b = -1
c = 0
d = 2
"""
x0 = int(input("x(0): "))
y0 = int(input("y(0): "))
"""

# First we turn the system into a matrix:
A = np.array([[a,b],[c,d]])

# Here we're getting the eigenvalues and eigenvectors out of the matrix for the system
evalues, evectors = np.linalg.eig(A)
eval1 = evalues[0]
evec1 = evectors[:,0]
eval2 = evalues[1]
evec2 = evectors[:,1]

c1 = 1
c2 = 1

t = np.linspace(-5,5,200)
x = c1*np.exp(eval1*t)*evec1[0] + c2*np.exp(eval2*t)*evec2[0]
y = c1*np.exp(eval1*t)*evec1[1] + c2*np.exp(eval2*t)*evec2[1]

plt.plot(t, x, label='x(t)')
plt.plot(t, y, label='y(t)')

plt.xlabel('t')
plt.ylabel('value')
plt.legend()
plt.grid(True)
plt.show()

print(eval1*evec1)
print(A@evec1)

print(evalues)
print(evectors)
