def product_of_polinomial_naive(A,B):
    RES = [0]*(len(A)+len(B)-1)
    for i in range(len(A)):
        for j in range(len(B)):
            RES[i+j]+=A[i]*B[j]
    return RES
A=[1,2,3,4]
B=[5,6,7,8]
print(product_of_polinomial_naive(A,B))

