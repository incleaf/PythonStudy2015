#예외처리

###에러가 발생하는 경우

```
>>> f = open("나없는파일", 'r')
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
FileNotFoundError: [Errno 2] No such file or directory: '나없는파일'

>>> a = [1,2,3]
>>> a[4]
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
IndexError: list index out of range

>>> 4 / 0
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
ZeroDivisionError: division by zero
```

### 에러 처리 구조

다음은 예외처리의 기본적인 구조인 try, except문이다.  
[ ]안의 내용은 옵션이다.

```
try: 
    ...
except [발생에러[as 에러메시지변수]]:
    ...
```

### try... else

```
try:
    f = open('foo.txt', 'r')
except FileNotFoundError as e:
    print(str(e))
else:
    data = f.read()
    f.close()
```

### try... finally

```
f = open('foo.txt', 'w')
try:
    # 무언가를 수행한다.
finally:
    f.close()
```

 finally절은 try문 수행 도중 예외의 발생여부에 상관없이 항상 수행된다. 보통 finally절을 사용하는 이유는 사용한 리소스를 close 해야 할 경우에 많이 사용된다.

### 에러 패스

```
try:
    f = open("나없는파일", 'r')
except FileNotFoundError:
    pass  	// 파일이 없더라도 오류가 아니다.
```

### 에러 발생시키기(raise)

코딩 중에 에러를 일부러 발생시켜야 할 경우가 생길 수 있는데, 이 때 raise 명령어를 사용하면 된다.  
아래의 예는 부모 클래스를 상속받은 자식 클래스는 반드시 fly() 함수를 구현하도록 구현한 것이다.  

```
// Bird 클래스(부모 클래스)
class Bird:
    def fly(self):
        raise NotImplementedError	// NotImplementedError 발생
```

```
// Bird를 상속받은 Eagle 클래스
class Eagle(Bird):
    pass
    
eagle = Eagle()
eagle.fly()

Traceback (most recent call last):
  File "...", line 33, in <module>
    eagle.fly()
  File "...", line 26, in fly
    raise NotImplementedError
NotImplementedError
```

fly()함수를 재구현하지 않아 부모 클래스의 fly()함수가 실행되어 NotImplementedError 에러가 발생되었다.   

```
class Eagle(Bird):
    def fly(self):		// 함수 재구현(override)
        print("very fast")

eagle = Eagle()
eagle.fly()
```
위와 같이 fly()함수를 재구현해서 부모의 fly()함수가 실행되지 않도록 하면 된다.