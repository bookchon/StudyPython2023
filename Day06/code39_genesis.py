# Car class를 상속한 제네시스 클래스
from code38_car import Car

# CHILD CLASS
class Genesis(Car): # 나는 code38의 car 클래스를 상속 받아서 진행하겠다는 뜻

    def __init__(self, name, color,
                plate_number, prodct_year) -> None: ## 초기화
        super().__init__ # 부모도 초기화하는 생성자 함수

        self.__name = name
        self.__color = color
        self.__plate_number = plate_number
        self.__product_year = prodct_year
        print(f'{self.__name} 인스턴스 생성!')

    def set_name(self, name): # class 제네시스에 뭔가를 적어야 할 지 모르겠으면 pass를 씀
            self.__name = name # 부모가 가지고 있지 않던 걸 새로 만듦

    def get_name(self): # 부모가 아닌 내 것(자식)으로 재정의 해서 쓰겠다는 뜻
         return self.__name

    def run(self):
        return f'{self.__name}, 달립니다.' # 부모가 가지고 있는 것을 수정하는 것이 재정의

    def stop(self):
        return f'{self.__name}, 멈춥니다.'

gv80 = Genesis('팔공이', 'black', '66오 1004', 2022)
gv80.set_name('팔공이')
print(f'이 차의 이름은 {gv80.get_name()}입니다.') 
print(gv80.run()) # 부모의 run을 쓰지 않고 새로 씀(overriding 재정의)
print(gv80.stop())
