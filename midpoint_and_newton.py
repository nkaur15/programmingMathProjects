#Implement formulas for the midpoint rule and newton's method

import math 

#Implement midpoint rule into integration of a function
def integration(f,a,b,N=10):
    interval = b - a
    length_of_subinterval = interval/N

    sum = 0
    count = 0

    while count <  N:
        c = a + length_of_subinterval
        area = f((a + c)/2) * (c - a)
        sum += area

        a = c
        count += 1

    return sum

f1 = lambda x: x ** 2

print(integration(f1,0,4,N=2))

#Modify newton method to check if f_deriv is actually a derivative of f
def newton(f,f_deriv,x0,tol=0.00001,N=10):
    x = x0
    count = 0

    while abs(f(x)) < tol and count <= N:
        x = x - f(x)/f_deriv(x)
        count += 1

    if count == N + 1:
        print ("Maximum number of iterations occurred.")
        return

    if f_deriv 

    return x

f2 = lambda x: x ** 2 - 8 * x + 7
f2_deriv = lambda x: 2 * x - 8

print(newton(f2,f2_deriv,8)
