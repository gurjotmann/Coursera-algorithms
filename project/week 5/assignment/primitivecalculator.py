import sys
def optimal_sequence(n):
    if n==1:
        return [1]
    if n==2:
        return [1,2]
    if n==3:
        return [1,3]
    A=optimal_sequence1(n)
    B=[0 for i in range(A[n]+1)]
    B[0]=1
    B[A[n]]=n
    return backtracking(A,n,B)
def optimal_sequence1(n):
    A=[0 for i in range(n+1)]
    A[1]=1
    A[2]=1
    A[3]=1
    for i in range(4,n+1):
        divide_two=float('inf')
        divide_three=float('inf')
        if i%2==0:
            divide_two=1+A[int(i/2)]
        if i%3==0:
            divide_three=1+A[int(i/3)]
        minus_one=1+A[i-1]
        A[i]=min(divide_three,divide_two,minus_one)
    return A
def backtracking(A,n,B):
    if A[n]==0:
        return 
    if A[n]==A[n-1]+1:
        backtracking(A,n-1,B)
        B[A[n]-1]=n-1
        return B
    if n%2==0:
        if A[n]==A[int(n/2)]+1:
            backtracking(A,int(n/2),B)
            B[A[n]-1]=int(n/2)
            return  B
    if n%3==0:
        if A[n]==A[int(n/3)]+1:
            backtracking(A,int(n/3),B)
            B[A[n]-1]=int(n/3)
            return B
input = sys.stdin.read()
n = int(input)
sequence = list(optimal_sequence(n))
print(len(sequence) - 1)
for x in sequence:
    print(x, end=' ')