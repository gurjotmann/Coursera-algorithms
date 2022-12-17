def EditDistance(A,B):
    DA=[[0 for x in range(len(B)+1)] for x in range(len(A)+1)]
    for i in range(len(A)+1):
        for j in range(len(B)+1):
            if i==0:
                DA[i][j]=j
                continue
            if j==0:
                DA[i][j]=i
                continue
            insertion=DA[i][j-1]+1
            deletion=DA[i-1][j]+1
            match=DA[i-1][j-1]
            mismatch=DA[i-1][j-1]+1
            if A[i-1]!=B[j-1]:
                DA[i][j]=min(insertion,deletion,mismatch)
            else:
                DA[i][j]=min(insertion,deletion,match)
    return DA[len(A)][len(B)]

if __name__ == "__main__":
    print(EditDistance(input(), input()))
            

