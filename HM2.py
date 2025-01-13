
sale_amount = float(input("Enter the sale amount: "))
if sale_amount <= 5000:
    discount = sale_amount * 0.05  # 5%
elif sale_amount <= 15000:
    discount = sale_amount * 0.12  # 12%
elif sale_amount <= 25000:
    discount = sale_amount * 0.20  # 20%
else:
    discount = sale_amount * 0.30  # 30%
total_amount = sale_amount - discount
print(f"Discount: {discount:.2f} euro.")
print(f"Amount including discount: {total_amount:.2f} euro.")
