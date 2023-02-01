# 라이프 스코프
a = 1

# def vartest(x): # 파라미터 또한 변수
#     x = x + 1
#     return x

# a = vartest(a) # 1을 가지고 vartest로 돌아감
# print(a)
# # 바깥 쪽에 있는 변수(a) 전역 변수, 안 쪽에 있는 변수(a)를 지역변수라고 함

def vartest(x):
    global a # 전역에 있는 a를 함수(지역)에서 가져다 쓰겠다는 뜻
    a = a + x + 1
    return a

a = vartest(a)
print(a)