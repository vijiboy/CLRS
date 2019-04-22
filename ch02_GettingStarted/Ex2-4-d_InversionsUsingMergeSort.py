#Exercise 2.4 d - nlogn algorithm to find inversions (modifying merge sort)
import sys
inversions = 0

def MergeSort(A): 
    if len(A) == 1:
        return A
    Left = []; Right = []
    Left.extend(A[0:int(len(A)/2)])
    Right.extend(A[int(len(A)/2):])
    print 'Left: ', Left
    print 'Right: ', Right
    Left = MergeSort(Left)
    Right = MergeSort(Right)
    A3 = Merge(Left,Right)
    return A3

def Merge(Left,Right):
    global inversions
    Left.append(sys.maxint)
    Right.append(sys.maxint)
    A3 = []
    i=j=0 
    while(True):
        if Left[i]==Right[j]==sys.maxint: 
            break
        if Left[i] <= Right[j] : 
            A3.append(Left[i]); 
            i+=1 
        elif Left[i] > Right[j]: 
            inversions += len(Left)-i-1
            A3.append(Right[j]); 
            j+=1
    print 'A3: ', A3        
    return A3            
            
    
A = [2,3,8,6,1]        
B = MergeSort(A)
print 'A:', A, 'B: ', B, 'Inversions: ', inversions
for i in range(len(B)-1):
    assert B[i] < B[i+1]
    
