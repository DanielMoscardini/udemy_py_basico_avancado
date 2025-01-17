print(type('Daniel'))
print(type('''Daniel'''))
print(type("Daniel"))
print(type("""Daniel"""))

nome = 'Daniel Moscardini'
print(nome.upper())
print(nome.lower())
print(nome.capitalize())

print(nome.split())
print(nome.split('a'))

# [ 0    1    2    3    4    5   6    7    8    9   10   11   12   13   14   15   16]
# ['D', 'a', 'n', 'i', 'e', 'l' ' ', 'M', 'o', 's', 'c', 'a', 'r', 'd', 'i', 'n', 'i']

print(nome[0:6])
print(nome.split()[0])
print(nome.split()[0][0:3] + '1')

print(nome[::-1])

print(nome.replace('i', '1', 2))


