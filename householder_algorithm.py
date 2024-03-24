#Householder transofrmation to compute reflection in hyperplane
import math
import copy

def dot_product(v,w):
    total = 0
    if (len(v) == len(w)):
        for a,b in zip(v,w):
            total += a*b
        return total
    else:
        return None

def reflection(u,a):
    #The return vector will be q
    q = [0 for i in range(len(a))]

    for i in range(len(a)):
        c = dot_product(u,a)
        print(c)

        q[i] = a[i] - 2 * c * u[i]

    return q

#print(reflection([-1/2,-1/2,-1/2,1/2],[4,3,-2,1]))

#Task 2 - Householder algorithm
def householder_algorithm(A):
    #Loop through values 0 to n-1
    u_list = []
    for i in range(len(A)-1):
        print("Step: " + str(i))
        #alpha is equal to the column of A we are referring to at each step
        #drop first i entries
        alpha = A[i][i:]
        print(alpha)

        #find the magnitude of alpha
        len_alpha = math.sqrt(dot_product(alpha,alpha))
        print(len_alpha)

        #b
        b = [0 for i in range(len(alpha))]
        b = copy.copy(alpha)

        b[0] -= len_alpha

        print(b)

        #u = normalizing b
        len_b = math.sqrt(dot_product(b,b))
        u = [0 for i in range(len(b))]
        for j in range(len(b)):
            u[j] = b[j]/len_b

        u_list.append(u)
        print(len_b)
        print(u_list)

        #For the remaining vectors in A, do Task 1
        V = copy.copy(A)
        print(V)

        for j in range(len(A)):
            print(V[j+1][j:])
            V[j+1][j:] = reflection(u_list[i],V[j+1][j:])

            A[j+1][j:] = V[j+1][j:]
        #print(A)

        #Compute the R
        R = [[0 for i in range(len(A[0]))] for j in range(len(A))]
        R[i][i] = len_alpha

        for j in range(len(A[0])):
                R[i+1][j] = A[i+1][j]

    return u,R

print(householder_algorithm([[1,1,1,1],[-1,4,4,-1],[4,-2,2,0]]))
