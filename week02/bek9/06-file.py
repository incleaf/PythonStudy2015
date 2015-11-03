# create file
f = open("testfile.txt", 'w')
f.close()

# write file
f = open("testfile.txt", 'w') # erased whole content

for i in range(1, 11):
	data = "%d 번쨰 줄입니다.\n" % i
	f.write(data)

f.close()

# read file 1
f = open("testfile.txt", 'r')

while True:
	line = f.readline()
	if not line: break
	print(line)

f.close()

# read file 2
f = open("testfile.txt", 'r')
lines = f.readlines()

for line in lines:
	print(line)

f.close()

# read file 3
f = open("testfile.txt", 'r')
data = f.read()

print(data)

f.close()

# add contents
f = open("testfile.txt", 'a')

for i in range(11, 16):
	data = "%d번쨰 줄입니다.\n" % i
	f.write(data)

f.close()

# with (auto close)
with open("testfile.txt", "r") as ff:
	print(ff.readline())