def sort_dq_rec(A):
    if len(A)==1:
        return A
    m=int(len(A)/2)
    B=sort_dq_rec(A[0:m])
    C=sort_dq_rec(A[m:len(A)])
    D= merge(B,C)
    return D
def merge(B,C):
    A=[0]*(len(B)+len(C))
    w=0
    while len(B)!=0 and len(C)!=0:
        if B[0]>=C[0]:
            A[w]=C[0]
            C.pop(0)
        else:
            A[w]=B[0]
            B.pop(0)
        w+=1
    if len(B)!=0:
        while len(B)!=0:
            A[w]=B[0]
            B.pop(0)
            w+=1
    else:
        while len(C)!=0:
            A[w]=C[0]
            C.pop(0)
            w+=1   
    return A
print(sort_dq_rec([2,3,7,1,22]))



    
