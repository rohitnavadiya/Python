bills = [500, 200, 100, 50, 20, 10, 5, 2, 1]
amount = float(input("enter your amount in INR: "))
bill_count = [0] * len(bills)
for i in range (len(bills)):
    bill_count[i] = amount
    amount = amount % bills[i]
for i in range (len(bills)):
    if bill_count[i] > 0 :
        print(f"₹{bills[i]}: {bill_count[i]}")