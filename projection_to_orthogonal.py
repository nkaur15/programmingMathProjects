import math

def dot_product(v,w):
    total = 0
    if (len(v) == len(w)):
        for a,b in zip(v,w):
            total+= a*b
        return total
    else:
        return None

def projection_to_orthogonal(a,Q):

    r_values = []
    num_vectors = range(len(Q))
    num_values = range(len(Q[0]))
    #r values are calculated by taking the previous q's and multiplying it by a
    for i in num_vectors:
        r = dot_product(Q[i],a)
        r_values.append(r)
    #print(r_values)

    a_perp = [0 for i in range(len(a))]
    for i in num_values:
        a_perp[i] = a[i]
    #print(a_perp)


    for i in num_vectors:
        multp_var = r_values[i]
        for j in num_values:
            Q[i][j] *= multp_var
            a_perp[j] -= Q[i][j]

    return a_perp

print(projection_to_orthogonal([3.0,4.0,-2.0,1.0],[[0.5,0.5,0.5,-0.5],[-0.5,0.5,0.5,-0.5]]))

def normalize(a):
    r_value = math.sqrt(dot_product(a,a))

    q = [0 for i in range(len(a))]
    for i in range(len(a)):
        q[i] = a[i] / r_value

    return q

print(normalize([3,4,-2,1]))
