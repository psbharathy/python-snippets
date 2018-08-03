import random

print(random.randrange(10,20))

x = ['1', 3, 'r', 45]

print(random.choice(x))

random.shuffle(x)

print(x)


my_list = ['a', 'e', 'i', 'o', 'u']

print(my_list[3])

print(my_list[-4])

print(my_list[2:4])

my_list.append('vovels')

my_list.extend(['a','b','c'])

print(my_list)


my_tuple = ("hello")
print(type(my_tuple))


my_string = 'Hello'
print(my_string)

my_string = "Hello"
print(my_string)

my_string = '''Hello'''
print(my_string)

# triple quotes string can extend multiple lines
my_string = """Hello, welcome to
           the world of Python"""
print(my_string)


str1 = 'Hello'
str2 = "World !"
str3 = str1 + str2
count = 0
print('str1 + str2=', str3 )
print('str*3=', str1 * 3 )

for letters in str3:
	count +=1

print(' Total Letters', count)


# Set

a = {1,3,4,6,8}
b = {41,3,4,66,8}

print(a) 
print(b)
print(a | b)
print(a & b)
b.union(a)
a.union(b)
print(b)
print(b.intersection(a))
print('Difference')
print(a - b)
print(b - a)
print(a.difference(b))
print(b.difference(a))
print('Unique')
print(a ^ b)

squares = {1:1, 2:4, 3:9, 4:16, 5:25}  

print(squares.pop(4))  
print(squares)