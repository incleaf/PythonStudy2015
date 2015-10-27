#package

###패키지 구조

```
game/
    __init__.py
    sound/
        __init__.py
        echo.py
        wav.py
    graphic/
        __init__.py
        screen.py
        render.py
    play/
        __init__.py
        run.py
        test.py
```
기본적으로 패키지 구조의 예는 이렇다.  
또 위에 보면 `__init__.py`파일은 해당 디렉토리가 패키지의 일부임을 알려주는 역할을 한다. 만약 디렉토리에 이 파일이 없으면 패키지로 인식되지 않는다.  
`[참고] python3.3 버전부터는 __init__.py 파일 없이도 패키지로 인식이 가능하게 변경되었다.(PEP 420) 하지만 하위 버전 호환을 위해 __init__.py 파일을 생성하는 것이 안전한 방법이다.`

```
# echo.py
def echo_test():
    print ("echo")
    
# render.py
def render_test():
    print ("render")

```
두 파일 안에 각각 하나씩 함수를 정의해두고, 패키지 추가하는 법을 알아보자.

### 패키지 추가

##### 첫번째 방법

```
>>> import game.sound.echo
>>> game.sound.echo.echo_test()
echo
```

##### 두번째 방법
```
>>> from game.sound import echo
>>> echo.echo_test()
echo
```

##### 세번째 방법
```
>>> from game.sound.echo import echo_test
>>> echo_test()
echo
```

###__all__ 의 용도

```
>>> from game.sound import *
>>> echo.echo_test()
Traceback (most recent call last):
  File "<stdin>", line 1, in <module>
NameError: name 'echo' is not defined
```
`*`을 이용하여 모듈을 import 할 경우, 해당 디렉토리의 `__init__.py`파일에 `__all__`변수를 선언해야 한다.  

```
__all__ = ['echo']
```
이런식으로 선언한 후 `*`을 이용하여 import하게 되면 해당 디렉토리에 `echo`모듈만 imoprt 된다.

### 상대적 패키지 (relative)

```
// 절대경로로 패키지 import
from game.sound.echo import echo_test

def render_test():
    print ("render")
    echo_test()
```

```
// 상대경로로 패키지 import 
from ..sound.echo import echo_test

def render_test():
    print ("render")
    echo_test()
```