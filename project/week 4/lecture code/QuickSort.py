import sys
sys.setrecursionlimit(1500)
def quicksort(A,l,r):
    if l>=r:
        return A
    m=partion(A,l,r)
    quicksort(A,l,m-1)
    quicksort(A,m+1,r)
    return A
def partion(A,l,r):
    x=A[l]
    j=l+1
    for i in range(l+1,r+1):
        if A[i]<=x:
            A[j],A[i]=A[i],A[j]
            j+=1
    A[j-1],A[l]=A[l],A[j-1]
    return j-1
A=[6,3,7,8,5,4,7,8,6,4,3,6,6,7,4,41,6,46,3456,34574,567,246,345673,46674564674,2345,3,3,34523,234523452345234523452334252]
print(quicksort(A,0,len(A)-1))