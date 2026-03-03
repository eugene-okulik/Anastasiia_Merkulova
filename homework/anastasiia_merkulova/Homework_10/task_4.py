PRICE_LIST = '''тетрадь 50 p
книга 200 p
ручка 100 p
карандаш 70 p
альбом 120 p
пенал 300 p
рюкзак 500 p '''

new_price_list = PRICE_LIST.split( )
new_price_list = filter(lambda x: x != 'p', new_price_list)
new_price_list = list(new_price_list)
items = new_price_list[::2]
prices = new_price_list[1::2]
prices_numbers = list(map(int,prices))
new_dict = dict(zip(items,prices_numbers))

print(new_dict)
