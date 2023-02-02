# 모듈 사용
import math as m # 클래스로 되지 ㅇ낳은 모듈
# as m 사용시 math를 사용하지 못함(m으로 사용하여야 함)
import code22_person as p # 우리가 만든 클래스
from code23_car import Car


 print(m.pi)

 print(m.cos(0))
 print(m.ceil(3.8)) # ceil 올림, floor 내림, round 반올림, 반내림
 print(2 ** 10)
 print(m.pow(2, 10))


# 우리가 만든 모듈을 사용
me = p.Person('홍길순', 155, '여성')
print(me)

#
mycar = Car()
print(mycar)