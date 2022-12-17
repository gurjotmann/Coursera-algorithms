# Uses python3
def evalt(a, b, op):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        assert False

def get_maximum_value(dataset):
    dataset_list=list(dataset)
    digits=dataset_list[0:len(dataset_list)+1:2]
    operators=dataset_list[1:len(dataset_list)+1:2]
    NO_of_digits=len(digits)
    MAX_VALUE=[[0 for i in range(NO_of_digits+1)] for i in range(NO_of_digits+1)]
    MIN_VALUE=[[0 for i in range(NO_of_digits+1)] for i in range(NO_of_digits+1)]
    for i in range(1,NO_of_digits+1):
        MAX_VALUE[i][i],MIN_VALUE[i][i]=int(digits[i-1]),int(digits[i-1])
    for s in range(1,NO_of_digits+1):
        for i in range (1,NO_of_digits-s+1):
            j=i+s
            MIN_VALUE[i][j],MAX_VALUE[i][j]=min_and_max(operators,MIN_VALUE,MAX_VALUE,i,j)
    return MAX_VALUE[1][NO_of_digits]   
def min_and_max(operators,MIN_VALUE,MAX_VALUE,i,j):
    min_=float('+inf')
    max_=float('-inf')
    for k in range(i,j):
        a=evalt(MAX_VALUE[i][k],MAX_VALUE[k+1][j],operators[k-1])
        b=evalt(MAX_VALUE[i][k],MIN_VALUE[k+1][j],operators[k-1])
        c=evalt(MIN_VALUE[i][k],MAX_VALUE[k+1][j],operators[k-1])
        d=evalt(MIN_VALUE[i][k],MIN_VALUE[k+1][j],operators[k-1])
        min_=min(min_,a,b,c,d)
        max_=max(max_,a,b,c,d)
    return min_,max_
if __name__ == "__main__":
    print(get_maximum_value(input()))
