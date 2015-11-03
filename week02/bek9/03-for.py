# for
li = ['one', 'two', 'three']
for i in li:
	print(i)

# continue
marks = [90, 25, 67, 45, 80]
num = 0
for mark in marks:
	num+=1
	if mark < 60: continue
	print("%d번 학생 합격" % num)

# range
print(range(10)) # range(0, 10)

sum = 0
for i in range(1, 11):
	sum += i
print(sum) # 55

for num in range(len(marks)):
	if marks[num] < 60: continue
	print("%d번 학생 합격" % (num+1))

# variation
a = [(1,2), (3,4), (5,6)]
for (first, last) in a:
	print(first+last)

# 구구단
for i in range(2, 10):
	for j in range(1, 10):
		print(i*j, end=", ")
	print('')

# List comprehension
a = [1,2,3,4]
print([num * 3 for num in a]) # [3, 6, 9, 12]

print([num * 3 for num in a if num % 2 == 0]) # [6, 12]

print([x*y for x in range(2,10) for y in range(1,10)]) # 구구단 값 배열