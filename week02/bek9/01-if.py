# if
cond = False
cond2 = True

if cond:
	print("It's true") # Indentation is required
elif cond2:
	print("It's another true")
else:
	print("It's false")

# Comparison operators
if 8>1: True
if 1<8: True
if 8==8: True
if 8!=1: True
if 8>=1: True
if 8>=8: True
if 1<=8: True
if 1<=1: True

# Logical operators
if True or False: True
if True and True: True
if not False: True

# in
print(2 in [1,2,3]) # True
print(4 not in [1,2,3]) # True
print('b' in ('a', 'b', 'c')) # True
print('p' in 'python') # True

# pass
pocket = ['paper', 'cellphone', 'card']
if 'money' in pocket:
	pocket.remove('money')
elif 'card' in pocket:
	pass
else: 
	print("거지")
