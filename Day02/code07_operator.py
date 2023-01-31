# 연산자
# 할당연산 (assignment)
val = 1 # = 는 변수에다가 원하는 값을 지정하여 넣는것(할당)

# equal 연산자
print(1 == 1)

# 사칙연산
print(1 + 1)
print(10 * 10)
print(1024 / 2) # 소수나누기
print(1024 // 2) # 정수 나누기
print(1 // 3)
print(1024 % 2) # 나머지
print(3 % 3) # 나머지

# print(6 / 0) # 0은 무한대로 컴퓨터에서 계산할 수 없음
# print(6 // 0)

print(10 ** 2) # 10의 2승

# 문자열 연산
first = 'Hello'
second = 'World'
print(first + second) # 더하기, 곱하기만 문자열 연산 사용 가능
print(first, second)

print(first * 4) # first 네번 곱해서 출력해 달라

# 문자열 길이
print(len(first)) # length
print(first[1]) # 문자열 길이 이상으로 치면 오류

# 파이썬 인덱스를 찾는 특이한 방법
print(first[-1])
print(first[-2]) # - 는 역순으로 셈

current = '2023-01-31 15:14:02' # 현재시간
print(len(current))
print(current[0:4])
print(current[5:7])
print(current[8:10])
print(current[11:13])
print(current[14:16])
print(current[17:19])

print(current[0:4] + '년' + current[5:7] + '월' + current[8:10] + '일')
print(current[-19:-15]) # 거꾸로도 출력 가능

# 리스트 연산
que = [1,2,3,4,5]
que[0] = 7
print(que) # 리스트는 숫자를 변환할 수 있어 에러가 나지 않음
# que[5] = 10 / 값 추가 시 이런식으로는 데이터를 추가 할 수 없음
que.append(10) # append 덧붙임 괄호 안에 값을 입력하면 새로운 요소를 array 맨 끝에 객체로 추가함
print(que)

que.insert(3,99)
print(que) # insert는 내가 원하는 위치에 넣음

que.remove(99)
print(que) # 해당 값 삭제
# tup = (1,2,3,4,5)
# tup[1] = 9
# print(tup) # 튜플은 숫자를 변환할 수 없어서 에러가 남


# 문자열 = 문자리스트
title = 'python' # 문자의 요소를 따로 출력하는 것이 아닌 따로 출력하는 것, 문자열에서는 값 변경이 되지 않음
print(title[0])
print(title[1])
print(title[2])
print(title[3])
print(title[4])
print(title[5])
print('P' + title[1:5])

# 문자열 포맷팅
# 문자열을 만들 때 원하는 위치에 특정한 값(변수)을 삽입해서 문자열을 그때그때 출력하는 것
print("I'm so happy {0} to you!!, {1}".format(2, 'Hey')) # format 사용하여 중괄호에 2를 넣겠다고 하는 것
#최신식 문자열 포맷팅
preword = 2
sayhello = 'Hey'
print(f"I'm so happy {preword} you, {sayhello}!!")
#f = f-string

pi = 3.141592
print(f'파이는 {pi} 입니다.') # 3.141592 다 나옴
print(f'파이는 {pi:0.2f} 입니다.') # 3.141592 다 나옴 # 0.02f = 소수점 두 번째 까지 출력하라는 뜻
print(f'파이는 {pi:10.3f} 입니다.') # 소수점 셋째짜리까지 표현하고, 앞의 공간을 10칸을 만들라는 뜻

print(round(pi,2))
print(int(pi))

full_name = "o seul yena"
print(type(full_name))
vals = full_name.split() # 공백을 기준으로 자름(space)
print(type(vals)) # 공백을 기준으로 잘라서 str -> 리스트로 변환됨
print(vals)

vals = full_name.split('s') # 특정 문자(지정하여)로 자르기 자주 씀
print(vals)

print(full_name.replace('o seul yena', 'monggata')) # replace는 언어 변환

# 문자열 공백 없애기
hi = '           Hello,  Bye.          '
print(hi.lstrip() + '|') # left strip , | 파이프키라고 부름
print(hi.rstrip() + '|') # right strip
print(hi.strip() + '|') # all strip


print(full_name.index("o")) # index는 지정한 문자열이 어디에 있는지 확인 시켜주는 것 , -1은 값이 없다는 뜻

# 찾는 단어의 개수를 알려줌
print(full_name.count('o'))

# 모든 단어를 대문자/소문자로 변경
print(full_name.upper())
print(full_name.lower())

# 연산자 우선순위
print(3 + 4 * 2)