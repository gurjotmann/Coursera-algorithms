def lastDigit(n) :
    return (n % 10)
def eff_fib_no_last(n):
    if n<=1:
        return n
    else:
      arr =[0]*(n+1)
      arr[0]=0
      arr[1]=1
      for i in range(2,n+1):
          arr[i]=arr[i-1]+arr[i-2]
          arr[i]=lastDigit(arr[i])
      return arr
def sum_last_digit_array(n):
    arr=eff_fib_no_last(n)
    sum = 0
    for i in range(len(arr)):
        sum = sum+arr[i]
    return lastDigit(sum)
n = int(input())
print(sum_last_digit_array(n))