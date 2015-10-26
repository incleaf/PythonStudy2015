##len()함수

```{.python}
marks = [90, 25, 67, 45, 80]

for number in range(len(marks)):  // =range(5) = range(0,5)  
  if marks[number] < 60: continue  
  print("%d번 학생 축하합니다. 합격입니다." % (number+1))
```
len()함수를 이런식으로 사용 가능하다.


##리스트 내포


```
//a 리스트의 각 항목에 3을 곱한 값을 result 리스트에 담는 코드이다.  

>>> a = [1,2,3,4]
>>> result = []
>>> for num in a:
...     result.append(num*3)
...
>>> print(result)
[3, 6, 9, 12]
```


```
//위 코드를 이런 식으로 리스트 내포를 사용하면 더 간단히 구현된다.
>>> result = [num * 3 for num in a]
>>> print(result)
[3, 6, 9, 12]
``` 

```
//if조건까지 추가하여 짝수인 값만 담을 수도 있다.

>>> result = [num * 3 for num in a if num % 2 == 0]
>>> print(result)
[6, 12]
```

`[표현식 for 항목 in 반복가능객체 if 조건]`		// 리스트 내포 문법


```
// 다중 for문도 가능하다
[표현식 for 항목1 in 반복가능객체1 if 조건1  
        for 항목2 in 반복가능객체2 if 조건2    
        ...  
        for 항목n in 반복가능객체n if 조건n]
        
// 다중 for문을 사용하여 손쉽게 구구단 값을 리스트에 담을 수 있다.
>>> result = [x*y for x in range(2,10)
...               for y in range(1,10)]
```


