#Creating definition of linear combinations

#Input a single list of 3 values to see if w1 and w2 can form a linear combination
def linearCombination(v):

    w1 = [6., 1., 2.]
    w2 = [0., 2., 3.]

    #Step 1: match first components of w1, w2 to v
    a1 = v[0] / w1[0]

    for i in range(len(w1)):
        w1[i] *= a1

    newList = [i-j for i,j in zip(v,w1)]

    #Step 2 : match second components
    a2 = newList[1] / w2[1]

    for i in range(len(w2)):
        w2[i] *= a2

    checkList = [i-j for i,j in zip(newList,w2)]

    #Step 3: match third components and check if it is a linear combination
    if (checkList[2] == 0):
        return [a1,a2]
    else:
        return None

print(linearCombination([-1,1,4]))
print(linearCombination([12,0,1]))

#Do the same but for 3 coefficients now
def linearCombination3(v):

    w1 = [6., 1., 2., 7.]
    w2 = [0., 2., 3., -1.]
    w3 = [0., 0., 4., -2.]

    #Step 1: match first components of w1, w2, w3 to v
    a1 = v[0] / w1[0]

    w1 = [i * a1 for i in w1]

    newList = [i-j for i,j in zip(v,w1)]

    #Step 2: match second components
    a2 = newList[1] / w2[1]

    w2 = [i * a2 for i in w2]

    secondNewList = [i - j for i,j in zip(newList,w2)]

    #Step 3: match third components
    a3 = secondNewList[2] / w3[2]

    w3 = [i * a3 for i in w3]
    
    finalList = [i - j for i,j in zip(secondNewList,w3)]

    # Step 4: match fourth components and check if it is a linear combination
    if (finalList[3] == 0):
        return [a1,a2,a3]
    else:
        return None

print(linearCombination3([6,3,13,2]))
print(linearCombination3([0,1,2,3]))

def loopLinearCombination(v):

   w1 = [6., 1., 2.]
   w2 = [0., 2., 3.]
   listOfVectors = [w1, w2]

   listCoeff = []

   count = 0
   for i in listOfVectors:
        coeff = v[count] / i[count]

        i = [j * coeff for j in i]

        v = [m - n for m,n in zip(v,i)]
        
        count += 1
        
        listCoeff.append(coeff)

   if (v[2] == 0):
        return listCoeff
   else:
        return None

print (loopLinearCombination([-1,1,4]))
print (loopLinearCombination([12,0,1]))
