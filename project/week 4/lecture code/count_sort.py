def count_sort(A,n):
    B=[0]*(n)
    for i in A:
        B[i-1]+=1
    D=[0]*(n+1)
    D[0]=0
    for i in range(1,n+1):
        D[i]=D[i-1]+B[i-1]
    copy_A=A.copy()
    C=D.copy()
    for i in range(len(A)):
       A[C[copy_A[i]-1]]=copy_A[i]
       C[copy_A[i]-1]+=1
    return A
print(count_sort([5,4,3,2,1,1,2,3,4,5,2,4,2,1,3,4,2,3,4,2,2,3,4,3,3,4],5))