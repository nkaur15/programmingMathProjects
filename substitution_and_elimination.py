#Implement substitution and elimination algorithms

#Write a function fo backwards substitution and forwards substitution
def BackSub(U,b):
    """Solve the upper triangular system Ux = b by backward substitution."""
    x = []

    #Define n as the number of rows in either U or b
    n = len(b)

    #Add the last coefficient to x before beginning a loop to gather the other elements
    x_last = b[n-1]/U[n-1][n-1]
    x.append(x_last)

    #Write a loop that appends the other x coefficients to the list x
    #Use size n - 1 since the last index is always 1 less than the size and 
    # since we already appended the last elements of x
    for i in range(n - 1):
        #Define a variable that represents the subtraction part from the appropriate
        # element in b each time the loop runs
        #Use a loop since the subtraction value has multiple values being subtracted
        sub_value = 0
        for j in range(i):
            sub_value += x[j] * U[n-1-i][n-1-j]

        #Define variables num and den to solve for the next element in x
        num = b[n-1-i] - sub_value
        den = U[n-1-i][n-1-i]

        #Define the new x to append to the list
        x_new = num/den
        x.append(x_new)

    #Reverse x, then return
    x.reverse()
    return x

#Test Case
print("Testing BackSub Function: ")
print(BackSub([[-1,0,7,3],[0,1,2,5],[0,0,4,2],[0,0,0,-7]],[9,8,6,-7]))


def ForwSub(L,b):
    """Solve the upper triangular system Lx = b by forward substitution."""
    x = []

    #Define the length of rows in L or b
    n = len(b)

    for i in range(n):
        sub_value = 0
        for j in range(i):
            sub_value += x[j] * L[i][j]

        num = b[i] - sub_value
        den = L[i][i]

        x_new = num/den
        x.append(x_new)

    return x

#Test Case
print("Testing ForwSub Function: ")
print(ForwSub([[-1,0,0,0],[0,1,0,0],[7,2,4,0],[3,5,2,-7]],[9,8,6,-7]))


#Write a function for Gaussian elimination
def GE0(A):
    """Performs Gaussian elimination on a square matrix with row exchanges. Return
    the lower triangular matrix L and upper triangular matrix U so that LU = A."""

    #Find the diagonals and for each row below the diagonal value, if the elements
    # in each rows in the same column in the diagonal is not equal to 0, find
    # the quotient for that row by dividing that value by the diagonal

    #Define L and U as a matrix of the same size as A, with values of 0
    num_rows = len(A)
    num_columns = len(A)

    L = [[0 for i in range(num_columns)] for j in range(num_rows)]
    U = [[0 for i in range(num_columns)] for j in range(num_rows)]

    #L has a diagonal of 1s
    for i in range(len(A)):
        L[i][i] = 1

    #Loop repeats for length len(A) - 1 since the last diagonal in the matrix is not used
    for row in range(len(A) - 1):
        #The second loop should refer to finding the elements for the rows below in 
        # the same position 
        #Only want to do the loop for the rows below the row of the diagonal value
        for ele in range(len(A) - 1 - row):
            #Condition that the element should not be equal to 0 already
            if (A[ele+row+1][row] != 0):
                q = A[ele+row+1][row]/A[row][row]
                #Implement the row operation to the row to get 0
                A[ele+row+1] = [m - n * q for m,n in zip(A[ele+row+1],A[row])]

                #Save the values of q into matrix L
                L[ele+row+1][row] = q

    #U is the matrix A after it undergoes row operations
    for i in range(len(A)):
        for j in range(len(A)):
            U[i][j] = A[i][j]

    return L, U

#Test Case
print("Testing GE0 Function: ")
print(GE0([[2,-1,0,0],[-1,2,-1,0],[0,-1,2,-1],[0,0,-1,2]]))


#More advanced gaussian elimination with partial pivoting
def GE1(A):
    """Performs Gaussian elimination on a square matrix A with row exchanges. Return 
    the lower triangular matrix L, upper triangular matrix U, and permutation matrix P
    so that LU = PA"""
    
    #Define matrices P, L, and U as matrices with values of 0 the same size of A
    num_rows = len(A)
    num_columns = len(A)

    L = [[0 for i in range(num_columns)] for j in range(num_rows)]
    U = [[0 for i in range(num_columns)] for j in range(num_rows)]
    P = [[0 for i in range(num_columns)] for j in range(num_rows)]

    #L and P are matrices with diagonals of 1s
    for i in range(len(A)):
        P[i][i] = 1

    #Create a loop that goes through each row below the row for the diagonal by 
    # finding the largest value in the column
    for i in range(len(A) - 1):
        #Starting with the element in position A[i][i] check the element in the 
        # column to see which value is the largest and switch that row with row i
        max = A[i][i]
        for j in range(len(A)):
            if (abs(A[j][i]) > max):
                max = A[j][i]
                max_index = j

        #Define 3 temporary lists to hold values when doing row switch
        temp1 = [0 for i in range(num_columns)]
        temp2 = [0 for i in range(num_columns)]
        temp3 = [0 for i in range(num_columns)]

        for val in range(len(A)):
            temp1[val] = A[i][val]
            A[i][val] = A[max_index][val]
            A[max_index][val] = temp1[val]

            temp2[val] = P[i][val]
            P[i][val] = P[max_index][val]
            P[max_index][val] = temp2[val]

            #For L the only thing the changes during row switches is the locations of 
            # the quotient values added, the diagonal of 1s stay in their location, bu 
            # since L is only defined as a matrix of 0s for now, it doesn't change the 
            # location of the 1s
            temp3[val] = L[i][val]
            L[i][val] = L[max_index][val]
            L[max_index][val] = temp3[val]

        #After row switch, we want to eliminate the values underneath the row for that
        # specific column. Making sure to store the values in matrix L and only 
        # doing operations on rows that have elements that are not 0
        
        for ele in range(len(A) - 1 - i):
            if (A[ele+i+1][i] != 0):
                q = A[ele+i+1][i]/A[i][i]
                A[ele+i+1] = [m - n * q for m,n in zip(A[ele+i+1],A[i])]
                L[ele+i+1][i] = q

    #Save manipulated values of matrix A into matrix U
    for i in range(len(A)):
        for j in range(len(A)):
            U[i][j] = A[i][j]

    #L is a matrix with diagonals of 1
    for i in range(len(A)):
        L[i][i] = 1

    return P, L, U

#Test Case
print("Testing GE1 Function: ") 
print(GE1([[0.2,-0.1,0,0],[1,-2,1,0],[0,1,-2,1],[0,0,-10,20]]))


def Solve(A,RHS):
    """Solve the linear system Ax = RHS for an invertible square matrix A"""

    #Solve function consists of 3 parts:

    #First, perform Gaussian elimination on A to derive the factorization PA = LU
    #Then, since PA = LU, if Ax = RHS, then LUx = PAx = PRHS
    #Call the function GE1 to derive the factorization of matrix A, which will
    # retrieve values P, L, and U
    P, L, U = GE1(A)

    #Since we have that LUx = PAx = PRHS, we can simplify PRHS by doing matrix multiplication
    #Define an empty vector to hold entried for PRHS
    num_rows = len(A)

    p_rhs_matrix_mult= [0 for i in range(num_rows)]

    #Do matrix multiplication by using two loops and store the values into the
    # previously defined matrix
    for i in range(num_rows):
        for j in range(num_rows):
            p_rhs_matrix_mult[i] += P[i][j] * RHS[j]

    #Second, using forward substitution solve for Ux
    Ux = ForwSub(L,p_rhs_matrix_mult)

    #Lastly, using backward substitution, solve for x
    x = BackSub(U,Ux)

    return x

#Test Case
print("Testing Solve Function: ")
print(Solve([[0.2,-0.1,0,0],[1,-2,1,0],[0,1,-2,1],[0,0,-10,20]],[0.1,0,0,10]))
