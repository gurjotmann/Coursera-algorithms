def mult2(A,B,n,a1,b1,R):
    
    if n==1:
        R[0]=A[a1]*B[b1]
        return R
    R[0:int(n-1)] = mult2(A,B,int(n/2),a1,b1,R)
    R[n:2*int(n-1)]=mult2(A,B,int(n/2),a1+int(n/2),b1+int(n/2),R)
    D1E2 = mult2(A,B,int(n/2),a1,b1+int(n/2),R)
    D2E1 = mult2(A,B,int(n/2),a1+int(n/2),b1,R)
    R[int(n/2):(n+int(n/2))-2]+= D1E2+D2E1
    return R
R=[0]*int(((2*4)-1))
A=[1,2,3,4]
B=[5,6,7,8]
print(mult2(A,B,4,0,0,R))