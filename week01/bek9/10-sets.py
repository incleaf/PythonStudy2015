#define
s1 = set([1, 2, 3])
print(s1) # {1, 2, 3}

s2 = set("Hello")
print(s2) # {'H', 'o', 'e', 'l'} 중복 안 됨

l1 = list(s2)
print(l1[0]) # 순서가 없음

# intersection
s3 = set([2, 3, 4])
print(s1 & s3) # {2, 3}
print(s1.intersection(s3)) # {2, 3}

# union
print(s1 | s3) # {1, 2, 3, 4}
print(s1.union(s3)) # {1, 2, 3, 4}

# difference
print(s1 - s3) # {1}
print(s1.difference(s3)) # {1}

# add
s1.add(4)
print(s1) # {1, 2, 3, 4}

s1.update([5, 6, 7])
print(s1) # {1, 2, 3, 4, 5, 6, 7}

# remove
s1.remove(6)
print(s1) # {1, 2, 3, 4, 5, 7}