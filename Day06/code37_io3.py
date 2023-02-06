# 콘솔 출력 보충
# 이스케이프 캐릭터(탈출문자)
print('Hello.\r\nworld')
print('Hello.\n world') # 이걸 권장함

print('hello.\n\tworld') # t는 tab
print('hello.\n\t\bworld') # b는 backspace
print('hello.\n\'world\'') # \ 문자열 내에 홑따옴표를 쓰기 위하여(강조하기 위하여) 나눠 줌
print('hello.\"world\"')

print('hello. \ world') # 화면에 역슬래시를 표현하고 싶을 때(파이썬은 하나만 써도 역슬래시 표현이 가능하지만, 다른 언어에서는 쉽지 않음)
print('hello.\0') # \0은 문자열 끝에 씀. 문자열이 끝났다는 것을 알려줌

# 문자열 포맷팅 - 구 버전
# %(퍼센테이지)로 포맷코드 시작
me = '저'
name = '예나'
age = 28
print('%s는 %s입니다. %d세 입니다.'% (me, name, age)) # 튜플처럼 순서를 바꿔선 안됨.

print(f"{254.112233:.2f}") # 최신 방법
print('%4.4f' %(254.112233)) # 구식 / 전체자리수.소수점