my_dict = {
    'tuple': (1, 2, 3, 4, 5),
    'list': ['apple', 'potato', 'strawberry', 'blackberry', 'watermelon'],
    'dict': {
        'swimming': True,
        'reading': True,
        'dancing': True,
        'running': True,
        'singing': True
    },
    'set': { 1, 2, 10, 'eight', 'zero'}
}
my_dict['list'].append('tomato')
my_dict['list'].pop(1)

my_dict['dict'] ['i am a tuple'] = False
del my_dict['dict'] ['swimming']

my_dict['set'].add(1000)
my_dict['set'].remove('zero')

print(my_dict['tuple'][-1])
print(my_dict)
