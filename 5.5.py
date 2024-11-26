price = float(input('Enter price: '))
discount_percentage = float(input('Enter discount %: '))
discount_amount = price * (discount_percentage / 100)
price_with_discount = price - discount_amount
reduction = price - price_with_discount

print(f'Price with discount: {price_with_discount}')
print(f'Reduction: {reduction}')
