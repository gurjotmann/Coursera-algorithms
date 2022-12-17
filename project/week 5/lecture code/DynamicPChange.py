import sys
def DynamicPChange(money):
    coins=[1,3,4]
    save_value_array=[0]*(money+1)
    for i in range(1,money+1):
        num_sum=float('inf')
        for j in coins:
            if j<=i:
               num_coins=save_value_array[i-j]+1
               if num_coins<=num_sum:
                   num_sum=num_coins
        save_value_array[i]=num_sum
    return save_value_array[money]


if __name__ == '__main__':
    m = int(sys.stdin.read())
    print(DynamicPChange(m))