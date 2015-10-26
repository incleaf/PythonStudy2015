#모듈

### 모듈 사용

```python
# mod1.py

def sum(a, b):
    return a + b

def safe_sum(a, b): 
    if type(a) != type(b): 
        print("더할수 있는 것이 아닙니다.")
        return 
    else: 
        result = sum(a, b) 
    return result
```
위와 같이 'mod1.py'라는 스크립트를 만들었다.  
mod1 모듈을 추가하여 사용해보자.

```
>>> import mod1
>>> print(mod1.safe_sum(1,2))	// safe_sum() 함수
3
>>> print(mod1.safe_sum(1,'a'))
더할수 있는 것이 아닙니다.
None
>>> print(mod1.sum(3,4))	// sum() 함수
7
```
위와 같이 사용하면 매번 'mod1.함수명' 이러한 형식으로 사용해야 한다.  
간단히 함수명만 사용하고 싶을 경우 `from 모듈이름 import 모듈함수` 이런 형식으로 모듈을 추가하면 된다.

```
// 모듈에서 필요한 함수만 추가
>>> from mod1 import sum, safe_sum
>>> sum(3, 4) 
7

// 모듈의 모든 함수를 추가
>>> from mod1 import *
```

### if __name__ == "__main__": 의 의미

```
# mod2.py 
PI = 3.141592

class Math: 
    def solv(self, r): 
        return PI * (r ** 2)


def sum(a, b): 
    return a+b

if __name__ == "__main__": 
    print(PI)
    a = Math() 
    print(a.solv(2)) 
    print(sum(PI , 4.4))
```

`if __name__ == "__main__":`   
이것의 의미는 파일을 직접 실행시켰을 때는 참이 되어 if문 안의 내용이 수행되고, 모듈을 import 시킬 때는 거짓이 되어 if문 안의 내용이 수행되지 않도록 한다는 뜻이다.  

```
>>> import mod2
>>> print(mod2.PI)	// 모듈 내 변수 사용
3.141592
>>> a = mod2.Math()	// 모듈 내 클래스 사용
>>> print(a.solv(2))
12.566368
```
또한 위처럼 모듈 선언 후 모듈 안의 변수, 클래스 및 함수 모두 사용 가능하다.

### 모듈 path 설정

##### python 내부에서 sys.path를 이용한 설정
```python
>>> import sys
>>> sys.path
['', '/usr/local/Cellar/python3/3.5.0/Frameworks/Python.framework/Versions/3.5/lib/python35.zip', '/usr/local/Cellar/python3/3.5.0/Frameworks/Python.framework/Versions/3.5/lib/python3.5', '/usr/local/Cellar/python3/3.5.0/Frameworks/Python.framework/Versions/3.5/lib/python3.5/plat-darwin', '/usr/local/Cellar/python3/3.5.0/Frameworks/Python.framework/Versions/3.5/lib/python3.5/lib-dynload', '/usr/local/lib/python3.5/site-packages']
```
sys.path는 파이썬 라이브러리들이 설치되어 있는 디렉토리들을 보여준다.  
또한 파이썬 모듈이 위의 디렉토리에 들어있는 경우에는 해당 디렉토리로 이동할 필요 없이 바로 불러서 쓸 수가 있다.   
원하는 디렉토리를 추가하고 싶으면 다음과 같은 문법으로 추가해주면 된다.  
`>>> sys.path.append('/Users/Jin-TaeWoo/PythonModules')`  

##### terminal에서 PYTHONPATH 설정

```
export PYTHONPATH='/Users/Jin-TaeWoo/PythonModules'
echo $PYTHONPATH
/Users/Jin-TaeWoo/PythonModules
```
원하는 디렉토리를 export 명령어를 이용하여 PYTHONPATH를 추가할 수 있다.  
윈도우의 cmd창에서는 export 대신 set을 사용하면 된다.

##### terminal 실행시 자동으로 PYTHONPATH 설정

위의 두가지 방법은 python 및 터미널 재구동 시 설정한 PATH가 리셋된다.  
터미널 구동시 자동으로 경로가 설정되도록 하려면 따로 방법이 필요하다.  
일단 SHELL에 따라 설정방법에 차이가 있는데, 아래와 같은 명령어를 사용하여 자신이 사용하는 SHELL을 알 수 있다.  
```
jin-yonghoui-MacBook-Pro:~ Jin-TaeWoo$ echo $SHELL
/bin/bash		//  bash 쉘
```
bash 쉘을 사용하면 자신의 홈 디렉토리에 `.bash_profile`이란 파일을 연다.  

```
export PATH=/usr/local/bin:$PATH
export PYTHONPATH=~/PythonModules	// 자신의 모듈디렉토리 경로추가
```
그 후, 위의 2줄을 추가해주면 된다.