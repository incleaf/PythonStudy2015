# 05-builtin.py

# abs
print(abs(3), abs(-3), abs(1+2j)) # 3 3 2.23606797749979

# all
print(all([1,2,3]), all([1,2,0])) # True False

# any
print(any([1,2,0]), any([0, ""])) # True False

# chr
print(chr(97), chr(48)) # a, 0

# dir
print(dir([]))
print(dir({}))

# divmod
print(divmod(7,3)) # (2,1) 몫, 나머지
print(divmod(1.3, 0.2)) # (6.0, 0.09999999999999998)

# enumerate
for i, name in enumerate(['foo', 'bar', 'quz']):
	print(i, name)

# eval
print(eval('1+2'), eval("'hello'+'world'"), eval('divmod(4,3)')) # 3 helloworld (1, 1)

# filter
def positive(x):
	return x > 0

print(list(filter(positive, [1, -3, 2, 0, -5, 6]))) # 1, 2, 6

print(list(filter(lambda x: x > 0, [1, -3, 2, 0, -5, 6]))) # 1, 2, 6

# hex
print(hex(109), hex(3)) # 0x6d 0x3

# id
a = 3
b = a
print(id(3), id(a), id(b), id(4))

# input
a = input() # 2.7 = raw_input
print("You said", a)

b = input("Enter: ")
print("You said", b)

# int
print(int('3'), int(3.6)) # 3 3 
print(int('1101101', 2), int('6D', 16)) # 109 109

# isinstance
class Person: pass
a = Person()
b = 3
print(isinstance(a, Person), isinstance(b, Person)) # True False

# lambda
sum = lambda a, b: a+b
print(sum(3, 4)) # 7

# len
print(len('python'), len([1,2,3]), len((1, 'a'))) # 6 3 2

# list
print(list('python')) # ['p', 'y', 't', 'h', 'o', 'n']
print(list((1,2,3))) # [1, 2, 3]
a = [1,2,3]
b = list(a)
print(b, id(a), id(b)) # id가 다르다

# map
def two_times(x): return x*2

print(list(map(two_times, [1,2,3,4]))) # 2, 4, 6, 8

print(list(map(lambda a: a*2, [1,2,3,4]))) # 2, 4, 6, 8

# max min
print(max([1,2,3]), min('python')) # 3 h

# oct
print(oct(109)) # 0o42

# ord
print(ord('a'), ord('0')) # 97 48

# pow
print(pow(2, 4), pow(3, 2)) # 16 9

# range
print(list(range(3))) # [0, 1, 2]
print(list(range(5, 10))) # [5, 6, 7, 8, 9]
print(list(range(0, -5, -1))) # [0, -1, -2, -3, -4]

# repr str
print(repr("hi"), str("hi")) # 'hi' hi

# sorted
print(sorted([3,1,2])) # [1, 2, 3]
print(sorted(['c', 'b', 'a'])) # ['a', 'b', 'c']
print(sorted('kukeb')) # ['b', 'e', 'k', 'k', 'u']

# tuple
print(tuple('abc'), tuple([1,2,3]), tuple((1,2,3))) # ('a', 'b', 'c') (1, 2, 3) (1, 2, 3)

# type
print(type('abc'), type([])) # <class 'str'> <class 'list'>

# zip
print(list(zip('abc', 'def'))) # [('a', 'd'), ('b', 'e'), ('c', 'f')]
print(list(zip([1,2,3], [4,5,6], [7, 8, 9]))) # [(1, 4, 7), (2, 5, 8), (3, 6, 9)]
