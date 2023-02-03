# 다중입력
# x, y = input('두 영단어를 입력하세요. > ').split()
# print(x)
# print(y)

# 완전 다중입력(개수가 몇개이든지 상관 없음) / 리스트로 만듦
# inputs = list(map(str, input('숫자를 입력하세요.').split())) # map은 나열하는 기능
# print(inputs)

inputs = list(map(int, input('정수를 입력하세요.').split()))
print(inputs)