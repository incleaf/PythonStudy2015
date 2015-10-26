#if문

## if문의 기본 구조

```
if <조건문>:  
  <수행할 문장1>  
  <수행할 문장2>  
else:  
  <수행할 문장A>  
  <수행할 문장B>  
```

##들여쓰기

if문을 사용할 때는 항상 **if<조건문>:** 다음의 문장부터 if문에 속하는 모든 문장에 **들여쓰기**를 해야 한다.

`조건문(if, while, for) 뿐만아니라 def, class에도 끝에 :(콜론)이 붙는데, 파이썬 문법이라고 생각하면 된다. 빼먹지 않도록 주의하자.`


##비교연산자

###1. and, or, not

x or y  : x와 y 둘중에 하나만 참이면 참.  
x and y : x와 y 모두 참이어야 참.  
not x : x가 거짓이면 참.

```{.python}
>>> money=1000
>>> card=0
>>> if money >= 5000 or card:
...   print("택시 고고")
... else:
...   print("뛰어")
... 
뛰어
```

###2. x in s, x not in s

x in (리스트, 튜블, 문자열 등)  
x not in (리스트, 튜블, 문자열 등)

```{.python}
>>> 1 in [1,2,3]		// 리스트
True
>>> 2 not in [1,2,3]
False
>>> 'a' in ('b', 'c')	// 튜플
False
>>> 'c' in ('c','d','e')
True
>>> 'f' in 'coffee'		// 문자열
True
```

###3. elif(다중 조건 판단)

```
If <조건문>:
    <수행할 문장1> 
    <수행할 문장2>
    ...
elif <조건문>:
    <수행할 문장1>
    <수행할 문장2>
    ...
else:
   <수행할 문장1>
   <수행할 문장2>
   ...
```

example
```
>>> pocket = ['paper', 'cellphone']
>>> card = 1
>>> if 'money' in pocket:
...      print("택시를 타고가라")
... elif card: 
...      print("택시를 타고가라")
... else:
...      print("걸어가라")
...
택시를 타고가라
```

###4. pass

조건문의 판단 여하에 따라 아무 일도 일어나지 않게 하고 싶을 때 사용한다.  
java에서 continue와 같은 기능이다.

```{.python}
>>> if 'love' in pocket:
...   pass
... else:
...   print("사랑이 식었어")
... 
```

###5. 간략한 if문

if문에서 수행할 문장이 한 줄일 때, 간편하게 사용할 수 있다.
```
>>> pocket = ['paper', 'money', 'rock', 'love']
>>> if 'love' in love: pass
... else: print("사랑이 식었어")
...
```
위에서 4줄이였던 코드를 이렇게 2줄로 간략화할 수 있다.
