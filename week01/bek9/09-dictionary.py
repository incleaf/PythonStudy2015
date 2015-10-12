# define
me = {
	'name': 'Bek9',
	8: 'My Favorite',
	'like': ['Hiphop', 'Movie']
}

# get val
print(me['name']) # Bek9

# add key
me['age'] = 27
print(me)

# del key
del me['age']
print(me)

# diffrence from arr
dic = {
	0: 'foo',
	1: 'bar',
	2: 'quz'
}

print(dic[1]) # bar

dic['a'] = 'qux' # 인덱싱이 아니다. key는 해시
# print(dic[0:]) # 인덱싱이 아니므로 슬라이싱 불가

dic[0] = 'new'
print(dic) # 중복 키 불가. 리터럴 선언 시 키가 중복되면 어떤 값이 유지될지 알 수 없음

# dic[[1,2]] = "It's a list" # list는 키로 불가, 변할 수 있기 때문
dic[(1,2)] = "It's a tuple"
print(dic[(1,2)]) # tuple은 키로 가능, 변하지 않기 때문

# functions

# get keys
print(list(me.keys())) # [8, 'like', 'name'] (2.7 style)

print(me.keys()) # dict_keys([8, 'name', 'like']) (python3 부터는 메모리 낭비를 줄이기 위해 객체 리턴)

for k in me.keys(): 
	print(k) # 굳이 리스트화하지 않아도 루프 가능

# get values
print(me.values()) # dict_values(['Bek9', 'My Favorite', ['Hiphop', 'Movie']])

# get key val pairs
print(me.items()) # dict_items([(8, 'My Favorite'), ('name', 'Bek9'), ('like', ['Hiphop', 'Movie'])])

# contains key
print('name' in me, 'unknown' in me) # True False

# get val 2
print(me.get('name')) # Bek9
print(me.get('unknown')) # None (me['unknown']은 에러)
print(me.get('unknown', 'Bek9')) # Bek9 (value 없을 경우 기본값 설정)