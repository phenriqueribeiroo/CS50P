# Ask for coin
coin = int(input("Insert Coin: "))
coke = 50
if coin == 5 or coin == 10 or coin == 25:
    amount_due = coke - coin
else:
    amount_due = coke

while amount_due >= 0:
    print(f"Amount Due: {amount_due}")
    coin = int(input("Insert Coin: "))
    if coin == 5 or coin == 10 or coin == 25:
        amount_due = amount_due - coin
    else:
        amount_due = amount_due
    if amount_due == 0:
        break


if amount_due <= 0:
    print(f"Change Owed: {-1 * amount_due}" )
