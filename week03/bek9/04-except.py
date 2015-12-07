# 04-except.py

# way 1
try:
	4 / 0
except:
	print("way 1 error")

# way 2
try:
	4 / 0
except ZeroDivisionError:
	print("way 2: zero division error")

# way 3
try:
	4 / 0
except ZeroDivisionError as e: # if less than 2.7: ZeroDivisionError, e
	print(e)

# else
try:
	f = open('foo.txt', 'r')
except FileNotFoundError as e:
	print(str(e))
else:
	data = f.read()
	f.close()

# finally
f = open('README.md', 'r')

try:
	lines = f.readlines()
finally:
	f.close()
	print("anyway f is closed")

# pass
try:
	f = open('foo.txt', 'r')
except FileNotFoundError:
	pass

# raise
class Bird:
	def fly(self):
		raise NotImplementedError
