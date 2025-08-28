
def calculate_discount(price, discount_percent):
    if discount_percent >= 20:
        final_price = price * (1 - discount_percent / 100)
        return final_price
    else:
        return price


price = float(input("Enter the original price of the item: "))
discount_percent = float(input("Enter the discount percentage: "))


final_price = calculate_discount(price, discount_percent)


if final_price != price:
    print(f"Discount applied! Final price: {final_price:.2f}")
else:
    print(f"No discount applied. Original price: {price:.2f}")
