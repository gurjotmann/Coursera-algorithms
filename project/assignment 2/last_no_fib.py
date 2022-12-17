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
      return arr[n]
n= int(input())
print(eff_fib_no_last(n))