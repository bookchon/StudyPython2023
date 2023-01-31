# 자료형
 # None 값이 없는 값(아예 지정되지 않음)
None
print(None)
print(0 == None)
print('' == None)

 # none는 형태가 존재하지 않음. 아무것도 없어서 none으로 지칭함
 # none과 0은 다름

# 숫자형
val = 3
print(type(val)) # 정수형 class 타입

val = 3.14
print(type(val)) # 실수형 calss 타입

val = "Hello"
print(type(val)) # 문자형 class 타입

val = 0b1010
print(type(val)) # 2진수 또한 정수로 나옴 

val = 4_520_000
print(val)

# 문자열형
val = "Life is short, You need Python."
print(val)
print(type(val))

val = 'hello\nWorld' # 탈출문자 종류(\n = 엔터, 파이썬에선 한 줄 안에 끝나야 함. 그래서 엔터를 하고 싶으면 \n을 써야함)
print(val)

val = 'hello\tworld' # 탈출문자 종류(\t 네 칸 띄워짐)
print(val)

val = 'hello\t\bworld' # 탈출문자 종류(\b 백스페이스)
print(val)

val = '''hello,
world''' # 따옴표를 여러 개 쓰면 \n 기능 대신할 수 있음
print(val)

# 불린형 or 불형
참 = True
거짓 = False
print(type(거짓))

print(1 + 1 == 2)
# 거짓이라는 False 값 변수가 참이냐

print(거짓 == True)
print(거짓 == False)
print(거짓 is False)

print(bool(1)) # 1 == true
print(bool(0)) # 0 == False 참은 1, 거짓은 0

#복합형 -> 여기서 부터 자료구조라고 부름. 위에 있던 형태를 엮어서 새로운 것을 만들기 때문. 알고리즘 할 때 반드시 필요함
