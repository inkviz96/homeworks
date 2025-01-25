def calculate_discount(sale_amount):
    if sale_amount <= 5000:
        discount = 0.05
    elif sale_amount  <= 15000 :
        discount = 0.12
    elif sale_amount <= 25000 :
        discount =0.20
    else :
        discount = 0.30
        discount_amount = sale_amount * discount
        final_amount = sale_amount - discount_amount
        print("Скидка: {discount_amount:.2f} рублей")
        print(f"Сумма с учетом скидки : {final_amount :2f}  рублей  ")




