prices = ['28$', '30$', '35$', '40$', '45$', '50$']
for price in prices:
    price = price.replace('$', 'ILS')
    print(f'the new price is {price}')
    price_only_nums = price.replace('ILS', '')
    price_as_integer = int(price_only_nums)
    print(price_as_integer)
    h_price = price_as_integer + 2
    h_price = f'h_price {h_price} ILS'
    print(h_price)

#