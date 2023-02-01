# 함수

# 함수 정의 - 실행이 아님
# 함수 만드는 방법 4가지
# 1. 파라미터O 리턴O
# 2. 파라미터O 리턴X
# 3. 파라미터X 리턴X
# 4, 파라미터X 리턴X
def add(x, y): # 함수 사용 시 무조건 앞에 def 를 붙여야 함
    result = x + y
    return result
# 함수는 정의, 함수를 쓰려면 함수를 불러와야 함(함수호출)
# add는 x + y 로 result에 담음

def sub(x, y):
    result = x - y
    print(result)
    
def mul(x, y):
    result = x * y
    print(result)

def div(x, y):
    result = x // y
    print(result)

def hello():
    print("Hello!")

def hello2():
    msg = 'hlelo, hello'
    return msg

# 함수 호출
add(1024, 5)
sub(1024, 1000)
mul(512, 2)
div(108, 10)