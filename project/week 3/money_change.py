def change(money):
    no_coins=0
    while money>0:
        if money>=10:
            money-=10
        elif money>=5:
            money-=5
        else:
            money-=1
        no_coins+=1
    return no_coins
print(change(int(input())))
