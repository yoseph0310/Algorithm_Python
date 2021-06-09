word = input()
croatian_list = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']

for i in croatian_list:
    word = word.replace(i, '*')

print(len(word))