def recursiveChange(money,coins):
    if money==0:
        return 0
    n_coins=float('inf')
    for i in coins:
        if money-i>=0:
            no_coins= recursiveChange(money-i,coins)
            if no_coins<n_coins:
                n_coins=no_coins+1
    return n_coins
money=50
coins=[10,25,30]
print(recursiveChange(money,coins))
