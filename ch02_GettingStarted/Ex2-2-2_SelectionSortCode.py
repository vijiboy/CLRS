def SelectionSort(A):
    for j in range(len(A)-1): 
        min = j
        for i in range(j+1,len(A)):
            if A[min] > A[i]: min = i
        if j == min: continue
        temp = A[j]
        A[j]=A[min]
        A[min]= temp
    return A

def isAscendingSorted(A):
    for i in range(len(A)-1):
        if A[i] > A[i+1]: return False
    return True 

print "Selection Sort"
A = [10,9,3,6,4,1]
print "before sort, A = ", A
SelectionSort(A)
print "after sort,  A = ", A
assert isAscendingSorted(A)

