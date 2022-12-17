def calculate_fib(n):
    if n<=1:
        return n
    else: 
        return(calculate_fib(n-1)+calculate_fib(n-2))
number=int(input())
print(calculate_fib(number))
