# mod2.py
PI = 3.14

class Math:
	def solv(self, r):
		return PI * (r ** 2)

def sum(a, b):
	return a+b

if __name__ == "__main__":
	print(PI) # 3.14
	a = Math()
	print(a.solv(2)) # 12.56
	print(sum(PI, 4.4)) # 7.540000000000001