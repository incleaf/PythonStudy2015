# while
i = 3
while i:
	print(i);
	i-=1;

# infinite loop
prompt = """
1. Add
2. Delete
3. List
4. Quit

Enter number: """
num=0
while num != 4:
	print(prompt)
	num = int(input())

# break
coffee = 2
while True:
	money = int(input("Insert the coins: "))
	if money == 300:
		print("1 coffee")
		coffee-=1
	elif money > 300:
		print("1 coffee and change is %d" % (money -300))
		coffee-=1
	else:
		print("Need more money")
	print("Coffee: %d" % coffee)
	if not coffee:
		print("Sold out")
		break

# continue
a = 0
while a < 10:
	a+=1
	if a % 2 == 0: continue
	print(a)
