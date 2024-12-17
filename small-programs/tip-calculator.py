bill = float(input("Enter total bill "))
tip_percent = int(input("Enter tip percent "))
person = int(input("Enter total number of person "))

tip_amount = (tip_percent / 100 * bill)
tip_amount = round(tip_amount, 2)
print(f"Total Tip = {tip_amount} Rs")
print(f"Total Bill After Tip = {bill+tip_amount} Rs")
print(f"Pay by per person = {(bill+tip_amount)/person} Rs")