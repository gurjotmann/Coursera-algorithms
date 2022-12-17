def max_rep_knapsack(W,V,w):
    max_value_arr=[0]*(W+1)
    for i in range(1,W+1):
        for j in range(len(w)):
            if w[j]<=i:
               value=max_value_arr[i-w[j]]+V[j]
               if value>max_value_arr[i]:
                   max_value_arr[i]=value
    return max_value_arr
print(max_rep_knapsack(10,[15,5,15],[1,2,3]))
                

