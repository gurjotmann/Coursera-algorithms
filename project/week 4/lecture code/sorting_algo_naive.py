def sort(A):
    for i in range(len(A)):
        shortest_no_index=i
        for j in range(i+1,len(A)):
            if A[j]<A[shortest_no_index]:
                shortest_no_index=j
        A[i],A[shortest_no_index]=A[shortest_no_index],A[i]
    return A
print(sort([5,3,7,1,5,3,8,2,3]))