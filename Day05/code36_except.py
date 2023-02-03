# 예외처리

def add(a, b):
    return a + b

def mul(a, b):
    return a * b

def div(a, b):
    return a / b

try:
    x, y = input('두 수를 입력하세요 > ').split()
    x = int(x)
    y = int(y)
except Exception as e:
    print(e)
    exit()
finally:
    print('계속 되나요?') # finally 먼저 실행 뒤, exit 실행 됨(종료)

# # 원시적인 예외처리
# if y == 0:
#     print('y에 0을 넣지 마세요.')
#     exit()

print('계산 테스트')

try: 
    print(div(x, y))
# except ZeroDivisionError as e:
#     print('0으로 나누지 마세요.') # zerodivisionerror와 exception 위치가 바뀌면 zerodivisionerror는 실행되지 않음
except Exception as e:
    print(e) # exception은 항상 제일 마지막에 쓸 것, zerodivision 없어도 실행 잘 되기 때문에 없어도 됨
finally:
    print("계산은 계속 됩니다.")
    # 예외가 나든 나지 않든 이 메세지는 계속 뜸

print(add(x, y))
print(mul(x, y))

# 예외처리 가장 많은 예