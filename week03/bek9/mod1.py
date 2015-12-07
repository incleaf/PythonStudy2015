# mod1.py
def sum(a, b):
	return a+b

def safe_sum(a, b):
	if type(a) != type(b):
		print("can't add")
		return
	else:
		result = sum(a, b)
	return result

# test code
if __name__ == "__main__":
	print(safe_sum('a', 1))