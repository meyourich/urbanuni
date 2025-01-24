my_dict = {'Nikolai': 1987, 'Mikhail': 1988, 'Julia': 1991}
print('Dict:', my_dict)
print('Existing value:', my_dict['Julia'])
print('Not existing value:', my_dict.get('Anton'))
my_dict.update({'Arkadiy': 1971, 'Syslik': 1966})
a = my_dict.pop('Mikhail')
print('Deleted value:', a)
print('Modified dictionary:', my_dict)
print()
my_set = {9, 8, 7, 'Sun', 5, 6, 7, 8, 9, 9}
print('Set:', my_set)
my_set.update({(1, 2)})
my_set.discard(9)
print('Modified set:', my_set)