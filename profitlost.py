actualcost = float(input("Please enter actual product price="))
saleamount = float(input("Please enter sale amount="))

if (saleamount>actualcost):
    amount = saleamount-actualcost
    print("Total profit = {0}".format(amount))
else:
    print("No profit")