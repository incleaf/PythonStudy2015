# function
def sum(a, b):
	return a+b

print(sum(3, 4))

# no arg
def say():
	return 'Hi'

print(say())

# no return
def saySum(a, b):
	print("%d, %d의 합은 %d입니다." % (a, b, a+b))

total = saySum(3, 4)

print(total) # None

# how many args
def sum_many(*args): # don't need to named 'args'
	sum = 0
	for i in args:
		sum += i
	return sum

print(sum_many(2, 3, 4)) # 9

def sum_mul(choice, *args):
	if choice == "sum":
		result = 0
		for i in args:
			result+=i
	elif choice == "mul":
		result = 1
		for i in args:
			result*=i
	return result

print(sum_mul('sum', 2, 3, 4), sum_mul('mul', 2, 3, 4)) # 9 24

# return is always one
def sum_and_mul(a, b):
	return a+b, a*b

print(sum_and_mul(3, 4)) # (7, 12) (it's tuple)

# return sometimes use escape
def say_nick(nick):
	if not nick:
		return
	print(nick)

print(say_nick("")) # None

# default arg
def say_myself(name, old=27, man=True): # must be last arg
	if man: gender = "남자"
	else: gender = "여자"
	print("Name: %s, Age: %s, Gender: %s" % (name, old, gender))

say_myself("bek9") # bek9 27 남자
say_myself("girl", 20, False) # girl 20 여자

# scope
a = 1
def scope_test(a):
	a = a + 1

scope_test(a)
print(a) # 1

def global_scope():
	global a
	a = a+1

global_scope()
print(a) # 2
