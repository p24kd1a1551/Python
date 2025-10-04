#program to calculate the discount in a mall
amount = float(input("Enter the amount less than 1 lakh : "))
if amount <= 5000 and amount >= 1000:
    discount = amount * 0.05
elif amount <= 25000 and amount >= 5000 :
    discount = amount * 0.1
elif amount <= 50000 and amount >= 25000:
    discount = amount * 0.2
elif amount <= 75000 and amount >= 50000:
    discount = amount * 0.25
elif amount <= 100000 and amount >= 75000:
    discount = amount * 0.3
else :
    discount = 0
    print("Discount is not applicable")
print(f"Total Discount = {discount:.2f}")
print(f"Total amount to be paid = {(amount - discount):.2f}")
