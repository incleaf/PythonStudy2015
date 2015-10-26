#while문

##while문의 기본 구조

```
while <조건문>:
    <수행할 문장1>
    <수행할 문장2>
    <수행할 문장3>
    ...
```

###1. 무한루프

```
while True:    	// 조건문이 True이기 때문에 수행할 문장을 무한반복 함.
    <수행할 문장1>     
    <수행할 문장2>
    ...
```


```
>>> prompt= """		// """를 사용하면 개행 포함한 문자열 생성 가능
...   1. Add
...   2. Del
...   3. Quit
... 
... Enter number: """

>>> number=0
>>> while number != 3:
...   print(prompt)
...   number = int(input())
... 

  1. Add
  2. Del
  3. Quit

Enter number: 

```

input함수

```
>>> a=input()
hi
>>> a
'hi'
```