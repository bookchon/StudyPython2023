import code

# 자동차 클래스
class Car:
    __number = '54라 9538' # 차의 디폴트 번호

    def get_number(self)  -> str: # 상속 함수
        return self.__number

    # 클래스 외부에선 변경할 수 없고, 멤버 함수로는 내부를 조작할 수 있음
    def __init__(self, number= '54라 9538') -> None:
        self.__number = number
        print('__init__')

    #  def __new__(cls):
    #      print('__new__')
    #      return super().__new__(cls) #부모 
    #      # car, str, super는 class. super, class 괄호 열고 닫으면 생성자

    def __str__(self) -> str:
        return f'제 차 번호는 {self.__number}.'
    
yourcar = Car('88호 7645')
print(yourcar)
yourcar.__number = '54라 9999' # 외부에서는 멤버 변수에 접근할 수 없음
print(yourcar)
print('클래스 내부함수 사용')
yourcar.set_number('55오 5555')
print(yourcar)

mycar = Car() # new 매직메서드가 먼저 일어나고 init이 일어남. str은 생성할 때 생기는 것이 아니라, print 할 때 나옴
print(mycar)
print(f'제 차는 아이오닉이고, 번호는 {mycar.get_number()}입니다.')

mycar.__number = '132거 8874'
print(mycar.get_number())
