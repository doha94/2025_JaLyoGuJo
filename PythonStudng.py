
#3월 10일 월
print("Hello Python")


a = 100
b = 200
print("a -> ", a, " + ", "b -> ", b, " = ", a+b)
print("a = {x}, b = {y}".format(x = a, y = b))














#----------------------------------------------------------------------------------------------------------------------------------------------------------

# 3월 11일 화


print("Hello Python"); print("Hello DIT")   # 줄바뀜이 자동으로 됨.
print("Hello Python", end="!!!")    # 줄바꿈을 하지 않고 기호를 붙여서 쓸 수 있음.
print("Hello Python",end=""); print("Hello DIT")    # 줄바꿈을 하지 않고 내용을 붙여서 쓸 수 있음.
# 굳이 이렇게 하는 이유는 만약 변수가 주어지는 상황에선 붙여서 사용할 수 없기 때문.

print("Korea", "Japen", "China")    # 파이썬은 항목과 항목 사이에 빈칸이 기본적으로 들어감.
print("Korea", "Japen", "China", sep="")    # 항목과 항목 사이에 sep의 값이 들어감.
print("Korea", "Japen", "China", sep="/")   # 항목과 항목 사이엥 sep의 값(/)가 들어감.

# 응용(?)
print("Korea", "Japen", "China", sep="[DIT]", end="[DIT]")  #항목과 항목 사이에 [DIT]를 넣고 문장 마지막에도 [DIT]를 넣기.

# 사용자로부터 입력받기(input)
input("Name?")  #input값을 바로 적용시켜서 다음줄에 입력받음
# 출력 -> Name?  (값 적기)
name = input("Name")    #name이라는 값을 만들어서 이 안에 입력받은 값을 넣기
# 출력 -> Name (Jang)
print(name)
# 출력 -> Jang


#----------------------------------------------------------------------------------------------------------------------------------------------------------


# 이름을 입력받고 그 사람에게 인사하는 문장을 다음과 같이 출력하기

# 이름: 홍길동
# "안녕하세요, 홍길동씨"


# 1. 이름을 입력받기
# 2. 위에서 입력받은 이름을 활용하여 인사말을 만들어 출력한다.

name = "홍길동"



# 장진우 답변
name = input("name : ")
print("안녕하세요, ", name)  
# 안녕하세요,  홍길동


# 성진이형 답변
print("안녕하세요, ", input("이름이 뭐에요?"), "씨")                          
# 이름이 뭐에요? 홍길동
# 안녕하세요,   홍길동 씨


# 교수님 답변
name = input("이름: ")
print("안녕하세요, {}씨".format(name))


# 형식지정자를 활용하여 같은 결과값 만들기
print("안녕하세요, %s씨."%(name))
# 안녕하세요, Jang Jin woo씨.

#----------------------------------------------------------------------------------------------------------------------------------------------------------

# 타입 확인하기
# type(N)

# 타입 변환하기
# int(N)  # 변수의 속성을 int형으로 바꿈(하지만 값 자체는 바뀌지 않음)
# n = int(N)  # 변수의 값 자체를 다시 바꾸어서 입력시킴(값 자체가 int로 바뀜)

#예시
temp = input("체온:")   # 체온:37.5

print(temp)             # 37.5

type(temp)              # <class 'str'>

temp = float(temp)      # 값을 실수형으로 지정해주기(double, float)
type(temp)              # <class 'float'>

# input을 사용하면 str로 값이 저장됨. 
age = int(input("나이: "))  # 이렇게 작성하면 int값으로 저장됨.


#----------------------------------------------------------------------------------------------------------------------------------------------------------

# 시퀀스
# 여러개의 값이 순서대로 나열되어 있는 것.
# (항목들이 순서대로 나열되어 있는 것)
# 파이썬엣 sequence의 값을 가진것 -> list, tuple, set(순서는 안되지만 처리할 수는 있음), dictionary, string, • • •

# 문법 'for' item 'in' sequence
# 제일 앞 -> 뒤 의 순서로 반복적으로 가져와 처리하는 방식

# 기본 반복문 개념 익히기
# list
fruits = ["apple", "banana", "mango", "kiwi"]   # 대괄호로 담은것 -> list 라고 불림. 즉 fruits 는 시퀀스이다.

for item in fruits:
    print(item)
# 단 item은 변수명으로 뭐든 써도 됨.


# 반복 횟수 지정하여 처리하기


# 함수 range(start = 0, stop, step = 1)
n = [1, 2, 3, 4, 5, 6, 7, 8, 9]
for i in n:
    print(i)

# 0부터 4까지 5개의 시퀀스를 생성함.
list(range(5))              # 0, 1, 2, 3, 4

# 1부터 9까지의 시퀀스를 생성하려면?
list(range(1, 10))          # 1, 2, 3, 4, 5, 6, 7, 8, 9


# range(start, stop, step) --> 이 중에서 step 부분은 생략을 해도 됨
# step 부분은 증가하는 양을 설정하는 것으로 첫 시작숫자(start) 부분에서 +step의 값이 생성되게 됨.
list(range(1, 20, 2))       # 1, 3, 5, 7, 9, ... 17, 19

# 만약 변수에 이 시퀀스 값을 넣고 싶다면?
a = list(range(1, 10, 3))
print(a)                    # [1, 4, 7]

#----------------------------------------------------------------------------------------------------------------------------------------------------------

# 3월 17일은 MT를 갔다온 관계로 다른 날짜로 대체 됨














#----------------------------------------------------------------------------------------------------------------------------------------------------------

# 3월 18일도 MT를 갔다온 관계로 다른 날짜로 대체 됨















#----------------------------------------------------------------------------------------------------------------------------------------------------------

# 3월 24일


# 변수를 주어 3월 24일 출력하기
month = 3
day = 24
print("오늘은 {}월 {}일 입니다.".format(month, day))        # 오늘은 3월 24일 입니다.

# 또는

print(f"오늘은 {month}월 {day}입니다.")                     # 오늘은 3월 24일 입니다.

# 또는

print("오늘은 %d월 %d일 입니다."%(month, day))


#----------------------------------------------------------------------------------------------------------------------------------------------------------

# 객채라고 함
# 기본 자료형의 종류, 확인, 변환

# text type: str
# --> 문자형 자료형

# Numeric types: int, float, complex
# --> 숫자형 자료형

# sequence types: list, tuple, range
# --> 여러개의 값들을 항목으로 관리하는 자료형

# mapping type: dict
# --> 키를 주고 한세트로 묶어서 관리하는 자료형

# set types: set, frozenset
# -->

# boolean type: bool
# --> True, False, >, =, < 등의 참과 거짓을 확인하는 자료형

# binary types: bytes, bytearray, memoryview
# -->

# 별개로 자료형이라고 하기보단 자료형을 판별하는 함수
# type(N)
# --> 어떤 자료형인지 확인하는 것


#----------------------------------------------------------------------------------------------------------------------------------------------------------


# 간단한 자료형 구조를 바꾸는 방법
b = "12345.123"     # 자료형을 생성

type(b)             # TYPE으로 출력하면 str 자료형으로 출력됨
float(b)            # FLOAT으로 자료형을 변환해보기
type(b)             # TYPE으로 자료형을 출력해보면 str이 출력됨
                    # --> float만으로는 자료형 구조를 바꿀 수 없음

c = float(b)
c
#12345.123

type(c)
# float
# --> 이런식으로 다른 변수에 넣어서 값은 같지만 자료형 구조를 바꿀 수 있음


#----------------------------------------------------------------------------------------------------------------------------------------------------------


# String(str)
# 문자형

"DIT"       # DIT
'DIT'       # DIT
"DI'T'"     # DI'T'
'DI"T"'     # DI"T"

"""DIT:
Dongeui
Insti.
of Technology"""    #DIT: \nDongeui\nInsti.\nof Technology

a =  'DIT: \nDongeui\nInsti.\nof Technology'
print(a)
# DIT:
# Dongeui
# Insti.
# of Technology

# 텍스트를 입력하는 방법은 다음과 같음 --> #, """....."""
"""
    파이썬 블록 코멘트는
    ''' 시작("으로 표기) ''' 종료
"""
# 즉 모든 코멘트에 #을 붙이기 귀찮다면 """을 사용하면 됨
# (하지만 저는 #이 더 편한걸요?)

# 인덱스
a = "Korea"
a[0]        # K
a[1]        # o
# 인덱스로 문자열을 하나 때어 오든 모든 문자열을 쓰든 모두 문자형임.(배열로 표기되는게 아니라는 것)

st = "  Hello, Python  "
st.upper()          #   HELLO, PYTHON   --> 모두 대문자로 변환한 결과 반환(upper)
st.lower()          #   hello, python   --> 모두 소문자로 변환한 결과 반환(lower)
st.strip()          # Hello, Python     --> 문자열의 시작, 끝부분 여백 제거(strip)
st.replace("Hello,", "I Love")      # I Love python     --> 원하는 문자 변환
# 단 replace를 사용할 때 단어가 대문자, 소문자 구분을 하기 힘들 수도 있으므로
st = st.lower().replace("love", "like")  # i like python

st = st.title()          # I Like Python    --> 모든 단어의 앞자리가 대문자로 바뀜(title)

type(a[1])  # str(O), list(X)
print(len(st))  # 문자열의 길이 반환
'I' in 'DIT'    # 문자열 포함 여부 확인(in, not in 사용 가능)

a = "Korea/Japan/China"
"Japan" in a        # True 출력
"Mexico" in a       # False 출력
"Mexico" not in a   # True 출력


#----------------------------------------------------------------------------------------------------------------------------------------------------------

# +, -, *, /

34 + 34             # 68

"Korea" + "Japan"   # KoreaJapan

365 + "Days"        # TypeError --> 타입 에러라고 뜹니다.
str(365) + "Days"   # 365Days

"DIT" * 5           # DITDITDITDITDIT (DIT를 5번 반복)


# 문자열 잘라오기
#   "0123456789..."(인덱스 자리값)
a = "ABCDEFGHIJKLM"
a[0]                # A --> 기본적인 인덱스 잘라오기

# a[start:Finish]     a 인덱스의 start부터 이후까지 잘라옴
a[0:2]              # AB (index의 0번째부터 1번째까지 가져오기)
a[1:3]              # BC (index의 1번째 부터 2번째 까지 가져오기)
a[:3]               # ABC (index의 처음부터 2번째 자리까지 가져오기)
a[:]                # ABCDEFGHIJKLM (index 내의 모든 글자 출력하기 -> 이렇게 할 바에 그냥 "a" 쓰기)
a[6:]               # GHIJKLM (index 6이후의 모든 글자 출력하기)
a[len(a)]           # M (마지막 글자 출력하기 -> 이렇게 하는 이유는 len을 사용하면 a의 인덱스 값("0" ~ n)이 아닌 a 문자열의 값이 출력되어 "1" ~ n 까지 이기 때문에)
a[len(a)-2]         # L (마지막의 전 글자 출력하기)





#----------------------------------------------------------------------------------------------------------------------------------------------------------

# 3월 31일

# 이 파일 어디있는지 못찾아서 못씀













#----------------------------------------------------------------------------------------------------------------------------------------------------------

# 4월 1일

# python 함수 - function
# 호출에 의해 실행되는 일련의 코드 블록
# 호출 시 데이터를 전달 가능: 파라미터(인수, 매개변수)
# 함수 처리 결과로 값을 반환 가능


# 함수 정의 방법
# def 함수명(매개변수, ...):
    # 함수 코드 블록
    
    
#----------------------------------------------------------------------------------------------------------------------------------------------------------

# 함수 정의와 호출 예
def printHello():
    print("Hello Python!!")
# 함수 호출
printHello()        # 출력 -> Hello Python!!


#--------------------------------------------------------------


# 함수의 매개변수 1
# 함수를 호출 시 데이터를 전달 가능: 파라미터(인수, 매개변수)
def sayHello(name):
    print(f"안녕하세요. {name}씨, 반갑습니다.")
# 함수 호출
sayHello("홍길동")      # 출력 -> 안녕하세요. 홍길동씨, 반갑습니다.




# 함수의 매개변수 1.2
# 함수에 디폴트값을 지정해 놓으면 만약 함수 안에 값을 쓰지 않아도 자동으로 작성됨
def sayHello(name="홍길동"):
    print(f"안녕하세요. {name}씨, 반갑습니다.")
# 함수 호출
sayHello()      # 출력 -> 안녕하세요. 홍길동씨, 반갑습니다.

#--------------------------------------------------------------


# 함수의 매개변수 2
# 파라미터는 여러 개 가능
def intro(name, age):
    print(f"저는 {age}세, {name}입니다.")
#함수 호출
intro("홍길동", 20)     # 출력 -> 저는 20세, 홍길동입니다.




# 함수의 매개변수 2.2
# 1.2와 마찬가지로 똑같이 디폴트 값 적용 가능
def intro(name="홍길동", age=20):
    print(f"저는 {age}세, {name}입니다.")
# 함수 호출
intro()     # 출력 -> 저는 20세, 홍길동입니다.
intro(20)   # 출력 -> 저는 20세, 20입니다.
intro(age=25)   # 출력 -> 저는 25세, 홍길동입니다.




# 함수의 매개변수 2.3
# 만약 디폴트 값을 주는것과 주지않는것을 섞었다면? 디폴트 값이 없는 함수가 앞으로 와야함
def intro2(age, name="홍길동"):
    print(f"저는 {age}세, {name}입니다.")
# 함수 호출
intro2(20)  # 출력 -> 저는 20세, 홍길동입니다.


#--------------------------------------------------------------


# 함수의 매개변수 3.1
# 파라미터 개수를 미리 알 수 없는 경우

def myFruits(*fruits):      # 호출 시 전달되는 인수들은 list에 담겨 fruits에 전달된다.
    for fruit in fruits:    
        print(f"I Like {fruit}.")
# 함수 호출
myFruits("apple", "kiwi", "banana", "mango")
# 출력
# I like apple.
# I like kiwi.
# I like banana.
# I like mango.




# 함수의 매개변수 3.2
# 적은 모든 숫자들의 평균 구하기
def average(*averagee):
    avg = 0
    for some in averagee:
       avg = avg + some
        
    print(avg/len(averagee))
# 함수 호출
average(3, 4, 343, 456, 6)     # 출력 -> 162.4




# 함수의 매개변수 3.3
def average2(*val):
    print(sum(val)/len(val))

average(3, 4, 343, 456, 6)
# 함수 호출
average2(3, 4, 343, 456, 6)     # 출력 -> 162.4


#--------------------------------------------------------------


# Tuple unpacking
def calc(a, b):
    return a+b, a-b, a*b, a/b
# 함수 호출
calc(3, 5)      # 출력 -> 8, -2, 15, 0.6
# 이걸 각 변수마다 나누어 가지게 할 수 있음
a = calc        # a의 값 안에 (8, -2, 15, 0.6)의 값으로 가지게 됨
a[0]            # 출력 -> 8
a[1]            # 출력 -> -2
a[2]            # 출력 -> 15
a[3]            # 출력 -> 0.6
# 이걸 하나의 변수에 하나의 값을 넣기
a, b, c, d = calc(3, 5)
a               # 출력 -> 8
b               # 출력 -> -2
c               # 출력 -> 15
d               # 출력 -> 0.6
# 이런 식으로 변수마다 값을 자동으로 나누어 가질 수 있음


# 만약 2개를 쓴다면?
a, b = calc(3, 5)
# Calue error
# 2개를 쓰려면 값을 분열해서 넣어주어야 함
def cacl(a, b):
    return (a+b, a-b), (a*b, a/b)
a, b  = cacl(3, 5)
a               # 출력 -> 8, -2
b               # 출력 -> 15, 0.6

# 또는
# 첫번째 값 하나만 주고 나머지 값 몰아주기
a, *b = calc(3, 5)
a               # 출력 -> 8
b               # 출력 -> -2, 15, 0.6
# 이렇게 *을 붙여놓은 곳에 남은 변수를 모두 넣어줌
*a, b = calc(3, 5)
a               # 출력 -> 8, -2, 15
b               # 출력 -> 0.6

# 만약 3개를 썼다면?
a, b, c = calc(3, 5)
# Value error

# 만약 3개인데 별이 붙어있다면?
a, *b, c = calc(3, 5)
a               # 출력 -> 8
b               # 출력 -> -2, 15
c               # 출력 -> 0.6
# 무조건 순서를 지킴





#----------------------------------------------------------------------------------------------------------------------------------------------------------

# 2월 11일





# Class(클래스)


# 객체지향 프로르래밍 언어.
# 파이썬에서는 대부분을 객체로 처리.( 속성 + 메서드)
# 클래스는 객체 생성을 위한 설계도



# 정의방법
class 클래스명:
    # 속성과 매서드 정의;
    name = "홍길동"


# 예시
class Person:
    name = "HongGilDong"
    def intro(self):
        print(f"저는 {self.name}입니다.")
        
# 객체 생성하기
p = Person()            # p안에 Person() 클래스 넣기
p.intro()               # 클래스 Person() 작동시키기

#-------------------------------------------------------


# 정의 방법
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

        # 객체를 문자열로 표현하여 반환
        def __str__(self):
            return f"{self.name}({self.age})"

    def intro(self):
        print(f"안녕하세요, 저는 {self.age}세 {self.name}입니다.")
                
# 객체 생성하기
p = Person("홍길동", 20)
p.intro()



class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

        # 객체를 문자열로 표현하여 반환
        def __str__(self):
            return f"{self.name}({self.age})"

    def intro(self):
        print(f"안녕하세요, 저는 {self.age}세 {self.name}입니다.")
                

# 객체 생성하기
p = Person("홍길동", 20)
p.intro()

#-----------------------------------------------------------------------------------------------------------------------------------------------
# 자료구조(Data Structure): 일련의 동일한 타입의 데이터를 정돈하여 저장한 구성체
# 데이터를 정돈하는 목적: 데이터에 대해 접근, 탐색, 삽입, 삭제 등의 연산을 효율적으로 수행하기 위해
# 자료구조를 설계할 떄는 데이터와 데이터에 관련된 연산을 함께 고려


# 자료구조의 효율성은 자료궂에 대해 수행되는 연산의 수행시간으로 측정
# 자료구조에 대한 연산 수행 시간은 알고리즘의 효율성을 계산하는 방식과 동일


# 알고리즘의 효율정:
    # 시간 복잡도(Time Complexity): 수행 시간
    # 공간 복잡도(Space Complexity): 알고리즘이 수행되는 동안 사용되는 메모리의 크기


# 시간 복잡도: 알고리즘(연산)이 실행되는 동안 사용된 기본적인 여산 횟수를 입력 크기의 함수로 나타냄

# 기본 연산(Elementary Operation)
# 데이터 간 크기 비교
# 데이터 읽기
# 데이터 갱신
# 단순한 계산 등과 같은 단순한 연산


# 일반적으로 알고리즘의 수행 시간은 최악 경우로 표현





#------------------------------------------------------------------------------------------------------------------------------------------------

# 4월 8일


# 리스트
# 일반적인 리스트(List)는 일련의 동일한 타입의 항목(item)들이 나열된 것


# 일반적인 리스트의 구현
# 파이썬 리스트
# 단순 연결 리스트
# 이중 연결 리스트
# 원형 연결 리스트



#-------------------------------------------------------------------


# 단순 연결 리스트
# 동적 메모리 할당을 이용해 리스트를 구현하는 가장 간단한 형태의 자료구조
# 동적 메모리 할당을 받아 노드(Node)를 저장하고, 노드는 레퍼런스를 이용하여 다음 노드를 가리키어 노드들을 한 줄로 연결

# 연결 리스트에서는 삽입이나 삭제 시 노드들의 이동이 필요 없음

# 연결 리스트에서는 삽입이나 삭제 시 노드들의 이동이 필요 없음
# 연결리스트에서는 탐색하려면 항상 첫 노드부터 원하는 노드를 찾을 때까지 차례로 방문: 순차 탐색(Sequential Search)





#=======================================
# 단순 연결 리스트 (Singly Linked list)
#=======================================
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
    def __str__(self):
        return f"[{self.data}]"
#=======================================
class SList:
    def __init__(self):
        self.head = None            # SList의 첫 노드를 가리킨다.(초기 값은 빈 리스트이므로 None)
        self.count = 0              # SList에 연결된 노드의 개수(를 항상 유지한다.)
        
        
        
        
    #---------------------------
    def __len__(self):
        return self.count
    
    
    
    
    #---------------------------
    # 새로운 노드를 만들거나 노드에 값을 추가하기
    def insertFront(self, newNode):
        if self.head is None:       
            self.head = newNode
            self.count = 1
        else:
            newNode.next = self.head
            self.head = newNode
            self.count += 1
                
                
                
    #---------------------------
    # append -> 기존의 리스트 맨 뒤에 새 노드를 연결함.
    def append(self, newNode):
        if self.head is None:       # Slist가 빈 리스트인 경우
            self.head = newNode     # 추가하려는 새 노드(newNode)가 첫 노드가 된다.
            self.count = 1
        else:       # 1개 이상의 노드가 있는 경우, (마지막 노드를 찾아서 그 뒤에 newNode를 연결한다.)
            current = self.head     # 리스트의 첫 노드(self.head)부터 순서대로 확인하며 마지막 노드를 찾는다.
            while current.next is not None:     # 다음 노드가 마지막 노드가 아니라면(현재 가리키고 있는 노드의 다음이 값이 있다면)
                current = current.next          # current는 다음 노드를 가리키도록 설정.
                
            current.next = newNode
            self.count += 1
    
    
    
        
    #---------------------------------
    # 리스트의 맨 끝에 새로운 요소를 추가하기
    def appendValue(self, value):
        self.append(Node(value))
    
    
    
    
    #----------------------------     
    # 리스트 보여주기       
    def showList(self):
        print("Head->", end="")
        current = self.head
        while current is not None:
            print(f"{current}-", end="")
            current = current.next
        
        print(f"-> None")
        print(f"({self.count}개 노드가 있습니다.)")

    
    


    #---------------------------------
    # 리스트의 첫 노드를 삭제하며 반환한다. (빈 리스트이면 none 반환)
    def unshift(self):
        if self.head is None:
            return None
        else:
            header = self.head
            self.head = self.head.next  # 첫 노드 제거
            header.next = None
            self.count -= 1
            return header
        
        
        
        
    #---------------------------------
    # 리스트를 역순으로 출력하기.
    def reverse(self):
        revList = SList()   # 역순으로 재구성하는 데 활용할 빈 리스트 생성
        
        # 기존 리스트의 첫 노드를 차례대로 제거하며 revList에 insertFront() 처리한다.
        while self.head is not None:
            h = self.unshift()  # 기존 리스트의 첫 노드를 제거한다. (h에 저장.)
            revList.insertFront(h)  # 새 리스트(recList)의 insertFront()로 제거한 노드를 추가한다.
        
        self.head = revList.head
        self.count = revList.count
        
    
    
    
    #----------------------------------
    def reverse2(self):
        revHead = None
        while self.head is not None:
            next = self.head.next
            self.head.next = revHead
            revHead = self.head
            self.head = next
            
        self.head = revHead
    
    
    
    
    #---------------------------------
    # 정렬되지 않은 현재의 리스트를 정렬상태로 재구성한다.
    def sort(self, order="UP"):
        sorted = SList()            # 빈 리스트를 하나 만들어준다.          -> 리스트를 별도로 만들어서 옮긴 후 사용하기 위해
        # 현재 리스트의 노드를 하나씩 차례대로 꺼내서 sorted 리스트에 insertSorted로 추가한다.
        while self.count:           # while self.head is not None와 같은 말입니다. 같은데 왜 저렇게 쓰냐구요? 저도 몰라요
            sorted.insertSorted(self.unshift(), order)      # 새로 만든 빈 리스트 sorted에 원래있던 노드들 insertSorted로 넣음 (order은 UP과 DOWN으로 어떤 방식으로 정렬할것인지 정의하는것)
        
        self.head = sorted.head
        self.count = sorted.count
    
    
    
    
    #---------------------------------
    # 현재 리스트의 복사본 리스트를 생성하여 반환하기
    def copy(self):
        newList = SList()
        current = self.head
        while current:
            newList.appendValue(current.data)
            current = current.next
        return newList
    
    
    
    
    
    #---------------------------------
    # 현재 단순 연결 리스트의 파이썬 리스트 버전을 생성하여 반환한다.
    def list(self):
        newList = list()
        current = self.head
        while current:
            newList.append(current.data)
            current = current.next
        return newList    
    
    
        
    #---------------------------------
        # 리스트의 정렬 상태를 유지하면서 새 노드를 추가한다.
    def insertSorted(self, newNode, order="UP"):
        if self.head is None:
            self.head = newNode
            self.count = 1
        else:
            # 새 노드(newNode)가 삽입될 위치를 찾기 위한 준비를 한다.
            current = self.head # 새 노드보다 큰 값을 가진 노드를 차례대로 찾아가기 위한 변수 (첫 노드부터 비교 시작)
            previous = None     # current가 다음 노드로 이동할 때, 현재의 current값을 백업하며 따라간다.

            while current is not None:  # 리스트의 마지막 노드까지 비교할 예정.
                if order == "UP":
                    check = newNode.data > current.data
                else:
                    check = newNode.data < current.data

                if check:
                    previous = current
                    current = current.next
                else:
                    if previous is None:    # 첫 노드 앞에 추가되어야 하는 경우
                        newNode.next = current
                        self.head = newNode
                    else:
                        previous.next = newNode
                        newNode.next = current
                    self.count += 1
                    return
            # 리스트의 마지막에 새 노드를 연결해야 하는 경우
            previous.next = newNode
            self.count += 1



    # def insertSorted(self, newNode):
    #     if self.head is None:   
    #         self.head = newNode
    #         self.count = 1
    #     else:
    #         # 새 노드(newNode)가 삽입될 위치를 찾기위한 준비를 한다.
    #         current = self.head     # current -> 새 노드보다 큰 값을 가진 노드를 차례대로 찾아가기 위한 변수        -> 그냥 self.head를 놔두고 다른 노드를 사용하기 위해서 저장하는 역할임
    #         previous = None         # current가 다음 노드로 이동할 때, 현재의 current값을 백업하며 따라간다.
            
    #         while current is not None:  #current에 하나씩 순서대로 값을 변경하여 넣을 것이기 때문에 current에 값이 있는지 없는지로 while로 계속 반복
    #             if newNode.data > current.data:     # 만약 새로운 노드가 current에 넣었던 값(self.head)보다 크다면? 
    #                 previous = current              # previous에 current 값을 넣어주기(previous에 current(기존 값)을 백업시키기)        -> self.head가 current에 들어가 있기 때문에
    #                 current = current.next          # current에 있던 값에 current의 다음 값을 넣어주고 다시 while문 반복시키기          -> 새로운 노드의 데이터가(값이) current안에 들어간 새로운 값보다 작을 때까지

    #             else:                               # 만약 새로운 노드가 current의 값보다 작다면?
    #                 if previous is None:            # 첫 노드 앞에 추가되어야 하는 경우         -> 즉 "previous의 값이 비어있다" = "위 if문이 실행되지 않았다" 이기때문에 self.head의 값 첫번째에 들어간다는 뜻이다.
    #                                                 # -> previous의 값이 비어있는지 아닌지 확인하는 이유: 위에있던 if newNode.data > current.data의 반복이 끝나고 previous에 값이 남아있을 수 있기 때문에
    #                     newNode.next = current      # 새로운 노드에 current(self.head)를 추가시킨다.
    #                     self.head = newNode         # self.head에 새로운 노드, 연결되어있는 노드(current)들을 저장시킨다.
    #                 else:
    #                     previous.next = newNode     # 위 if문에서 끝난 previous의 다음 값에 새로운 노드를 연결시킨다.                         # 첫 노드 앞에 추가되는 경우가 아니라면?    -> "previous의 값이 비어있지 않다" = "위 if문이 실행되었다" 이기 때문에 첫 노드가 아닌 두번째 이후의 노드에 연결된다 임.
    #                     newNode.next = current      # 이후 previous -> newNode 로 연결되어있는 상태의 newNode 뒤에 current(위 if문에서 사용하지 않은 current.next들이 남아있음)를 연결시
    #                 self.count += 1                 # 새로운거 들어왔으니까 카운트 증가
    #                 return
            
        
        
    #---------------------------------
    # 특정 값을 가진 노드를 연결 리스트에서 제거한다.
    def remove(self, value):
        targetNode = self.find(value)# 아래에 만들었던 find를 이용하여 리스트들의 값을 미리 확인 하고, targetNode에 넣어 둠
        if targetNode is None:  # 만약 targetNode에 값이 들어가지 않는다면 이는 리스트 안에 값이 없다는것을 가리킴. 즉 더 이상 확인할 필요가 없다는 것
            return None         # 고로 None값을 반환하여 끝냄
        else:
            previous = None
            current = self.head
            while current is not targetNode:
                previous = current
                current = current.next
            
                # targetNode가 첫 번째 노드일 때 처리
            if previous is None:
                self.head = current.next  # head를 다음 노드로 설정
            else:
                previous.next = current.next  # current 노드를 제거
                # 연결 끊었으므로 targetNode를 리턴할 수 있으면 리턴
            return targetNode
        
        
        
    #---------------------------------
    # 특정값이 리스트에 포함되어 있는지 결과를 알려주기
    # 반환값: 없을 경우 None, 있으면 해당 노드 반환
    def find(self, value):
        current = self.head
        while current is not None:
            if value == current.data:
                return current
            else:
                current = current.next
        # vlaue를 찾지 못하면 while 종료
        return None




#===========================================================================================================================================================
# 출력하기!

print("0-------------------------------")
lst = SList()
lst2 = SList()


lst.insertFront(Node(200))
lst.insertFront(Node(1000))
lst.insertFront(Node(100))
lst.insertFront(Node(500))


print("1-------------------------------")
lst.insertSorted(Node(400))
lst.showList()

print("2-------------------------------")
lst.sort("UP")
lst.showList()

print("3-------------------------------")
for item in lst.list():
    print(item)
    
print("4-------------------------------")
# append는 제일 뒤에, insertFront는 제일 앞에 추가되는 차이
lst.append(Node(5000))
lst.insertFront(Node(4000))
lst.showList()







#===========================================================================================================================================================
# 5월 13일
"""
    이중 연결 리스트(double linked list)
"""


#=======================================================
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None
        self.prev = None
    
    def __str__(self):
        return f"[{self.data}]"
    
    
#========================================================
class DList:                    # 임의의 리스트에 연결부 만들어주기?
    def __init__(self):
        self.head = None
        self.tail = None
        self.count = 0
        
        
    #---------------------------------------------------
    # 리스트의 맨 뒤에 value 값을 가진 새 노드를 연결한다.
    def append(self, value):        # 값을 뒤에다 붙이기
        # 새로 추가할 노드 생성
        newNode = Node(value)
        # 빈 리스트인 경우를 먼저 확인하고 처리한다.
        if self.count == 0:
            self.head = newNode
            self.tail = newNode
        else:           # 빈 리스트가 아닌 경우에는 리스트의 tail이 가리키는 노드 뒤에 새 노드를 연결한다.
            self.tail.next = newNode
            newNode.prev = self.tail
            self.tail = newNode
        # 리스트의 노드 개수 증가 반영
        self.count += 1


    #---------------------------------------------------
    def insertFront(self, value):    # 값을 앞에다 붙이기
        newNode = Node(value)
        if self.count == 0:
            self.tail = newNode
            self.head = newNode
        else:
            self.head.prev = newNode
            newNode.next = self.head
            self.head = newNode
        self.count += 1
        
        
    #---------------------------------------------------
    # 리스트에서 value 값을 가진 첫 노드를 찾아서 반환한다.
    # 없으면 none 값을 반환
    def find(self, value):
        current = self.head
        while current:          # == while current is not none
            if value == current.data:
                return current
            else:
                current = current.next
        # vlaue를 찾지 못하면 while 종료
        return None        
    
    
    #---------------------------------------------------
    def showList(self):             # 리스트 보여주기
        print("head->", end="")
        # head부터 마지막 노드까지 차례대로 노드를 출력한다.
        current = self.head
        while current:      # == while current is not none
            print(current, end="-")
            current = current.next
        # 리스트의 노드 개수를 출력하면서 리스트 출력 마무리.
        print(f"({self.count} nodes)")
        
        
    #---------------------------------------------------
    # 리스트의 존재하는 target 앞에 value값을 가진 새 노드를 생성하여 삽입한다.                                                     속보! 이해안됨 지피티한테 물어보기
    def insertBefore(self, target, value):
        if target:
            return None
        if target is self.head:
            self.insertFront(value)
        else:
            newNode = Node(value)
            newNode.next = target
            newNode.prev = target.prev
            target.prev.next = newNode
            target.prev = newNode
        self.count += 1
        
    #---------------------------------------------------
    # 리스트에 존재하는 target 뒤에 value값을 가진 새 노드를 생성하여 삽입한다.
    def insertAfter(self, targetNode, value):
        # 다음수업까지 만들어오기
#========================================================
dlist = DList()
dlist.insertFront(100)
dlist.insertFront(200)
dlist.insertFront(300)
dlist.showList()
dlist.insertBefore(dl)
