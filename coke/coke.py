price = 50
print("Amount Due:",price)
while price > 0:
    coin = int(input("Insert coin:"))
    if coin == 25 or coin == 10 or coin == 5:
        price = price - coin
        if price <= 0:
            break
        print("Amount Due:",price)
    else:
        print("Amount Due:",price)
if price <= 0:
    print("Change Owed:", price * (-1))

