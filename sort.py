# excersize, merge sort 

A = [1,3,5,7,9,11,13,15,17,19]
B = [10,20,30,40,50,60,70,80,90,100]

def merg(A, B):
    C = []
    i = 0
    j = 0
    while i < len(A) and j < len(B):
        if A[i] < B[j]:
           C.append(A[i])
           i += 1
        else:
            C.append(B[j])
            j += 1
    while i < len(A):
        C.append(A[i])
        i +=1 
    while j < len(B):
        C.append(B[j])
        j += 1
    return C

print (merg(A, B))