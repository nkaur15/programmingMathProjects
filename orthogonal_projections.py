"""
Write a function to compute the orthogonal projection onto the column space
of A, using the formula A(A^TA)^-1A^T
"""
import numpy as np

def orth_projection(A):
    A = np.array(A)
    transpose = np.matrix.transpose(A)
    first_matrix_mul = np.matmul(transpose,A)
    inverse = np.linalg.inv(first_matrix_mul)

    mult_step1 = np.matmul(A,inverse)
    mult_step2 = np.matmul(mult_step1,transpose)

    return mult_step2


#Test Case
print("Orthogonal Projection Example 1:")
print(orth_projection([[1,-1,4],[1,4,-2],[1,4,2],[1,-1,0]]))
print("Orthogonal Projection Example 2:")
print(orth_projection([[1,1],[1,0],[0,1]]))

"""
Consider the list of lists of vectors ... Compute orthogonal projectsions
of the whole list onto each plane.
"""

import matplotlib.pyplot as plt
import math

def f(u,v):
    return np.array([math.cos(u) * (math.cos(v) + 4) + math.sin(v), math.sin(u) * (math.cos(v) + 4), math.cos(u) * (math.cos(v) + 4) - math.sin(v)])
grid = [list(a.flatten()) for a in np.meshgrid(np.arange(0,10,0.03), np.arange(0,10,0.03))]
points = [f(u,v) for u,v in zip(grid[0],grid[1])]

A = np.array([[1,0],[0,1],[0,0]])
B = np.array([[2,2],[2,3],[5,6]])
C = np.array([[4,8],[3,4],[6,7]])

P = orth_projection(A)
proj = [np.matmul(P,v) for v in points]

X = orth_projection(B)
proj2 = [np.matmul(X,v) for v in points]

Y = orth_projection(C)
proj3 = [np.matmul(Y,v) for v in points]

x = [p[0] for p in proj]
y = [p[1] for p in proj]

a = [p[0] for p in proj2]
b = [p[1] for p in proj2]

c = [p[0] for p in proj3]
d = [p[1] for p in proj3]

#plot the projections and check the shape
plt.plot(x,y, 'k*')
plt.plot(a,b, 'b*')
plt.plot(c,d,'r*')
plt.show()
