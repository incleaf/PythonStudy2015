# 클래스

### class 기본 구조

```
class 클래스이름[(상속 클래스명)]:
    <클래스 변수 1>
    <클래스 변수 2>
    ...
    def 클래스함수1(self[, 인수1, 인수2,,,]):
        <수행할 문장 1>
        <수행할 문장 2>
        ...
    def 클래스함수2(self[, 인수1, 인수2,,,]):
        <수행할 문장1>
        <수행할 문장2>
        ...
    ...
```

### self, __init__ 알기

```python
>>> class HousePark:
...     lastname = "박"
...     def __init__(self, name):	// 생성자
...         self.fullname = self.lastname + name
...     def travel(self, where):
...         print("%s, %s여행을 가다." % (self.fullname, where))
...
>>> me = HousePark('태우')
>>> me.travel('유럽')
>>> 박태우, 유럽여행을 가다.
```
me = HousePark('태우') 이렇게 Service를 생성하면 자동으로 __init__ 함수가 생성되고, self는 me가 된다.  
즉 self에는 인스턴스 이름이 들어가게 되는 것이다.  
`me.sum(1,2)는 self.sum(me, 1, 2)와 같은 의미이다.`


### 상속(Inheritance)

```
>>> class HouseJin(HousePark):	// HousePark을 상속
...      lastname = "진"
...
>>>
```
HousePark을 상속받고 lastname만 바꿨다. HousePark을 상속받은 HouseJin은 lastname을 제외한 모든 기능이 HousePark의 기능과 동일하다.  
이렇게 같은 기능을 수행하는 class를 상속으로 손쉽게 구현 가능하다.

```
>>> class HouseJin(HousePark):
...     lastname = "진"
...     def travel(self, where, day):	// overriding
...         print("%s, %s여행 %d일 가네." % (self.fullname, where, day))
...
>>>
```
다른 class를 상속받아 원하는 메쏘드명은 그대로지만 인자값만 재구현하여 사용할 수도 있는데 이를 **오버라이딩(overriding)**이라고 한다.  

### 연산자 오버로딩(overloading)

연산자 오버로딩이란 연산자(+, -, *, /,,, )등을 객체끼리 사용할 수 있게 하는 기법을 말한다.  

```
class HousePark:
    lastname = "박"
    def __init__(self, name):
        self.fullname = self.lastname + name
    def travel(self, where):
        print("%s, %s여행을 가다." % (self.fullname, where))
    def love(self, other):
        print("%s, %s 사랑에 빠졌네" % (self.fullname, other.fullname))
    def fight(self, other):
        print("%s, %s 싸우네" % (self.fullname, other.fullname))
    def __add__(self, other):
        print("%s, %s 결혼했네" % (self.fullname, other.fullname))
    def __sub__(self, other):
        print("%s, %s 이혼했네" % (self.fullname, other.fullname))

class HouseKim(HousePark):
    lastname = "김"
    def travel(self, where, day):
        print("%s, %s여행 %d일 가네." % (self.fullname, where, day))


pey = HousePark("응용")
juliet = HouseKim("줄리엣")
pey.travel("부산")
juliet.travel("부산", 3)
pey.love(juliet)
pey + juliet		// __add__ 함수가 호출.
pey.fight(juliet)
pey - juliet		// __sub__ 함수가 호출.
```