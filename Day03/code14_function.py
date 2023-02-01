# 함수

# 함수 정의 - 실행이 아님
def add(x, y): # 함수 사용 시 무조건 앞에 def 를 붙여야 함
    result = x + y
    return result
# 함수는 정의, 함수를 쓰려면 함수를 불러와야 함(함수호출)
# add는 x + y 로 result에 담음

def sub(x, y):
    result = x - y
    return result
    
def mul(x, y):
    result = x * y
    return result

def div(x, y):
    result = x // y
    return result

# 함수 호출
val = add(1024, 5)
print(val) # 함수를 호출한 대상자에게 값을 되돌려주는 것이 return

# 함수를 호출하면 실행을 하고 함수 정의로 돌아감
# 다른 함수가 있으면 다른 함수로 돌아감. 리턴하고 리절트 후 결과값을 도출함

val = sub(1024, 1000)
print(val)

val = mul(512, 2)
print(val)

val = div(108, 10)
print(val)