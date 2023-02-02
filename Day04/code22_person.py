# 클래스 생성
class Person: #함수이름
    name = '익명'
    height = ''
    gender = ''
    blood_type = 'A'

    ### 1. 생성자 초기화 추가
    # def __init__(self): ### 생성자 / contents assistance를 동작시키면 자동완성 됨
    #     self.name = '홍길동'
    #     self.height = '170'
    #     self.gender = 'male'
    #     self.blood_type = 'AB'

    def __init__(self, name = '홍길동', height = 170, gender = 'male') -> None: # name, height, gender 매개변수 / 맨 위는 global, 아래는 local
        self.name = name
        self.height = height
        self.gender = gender 
    # 내가 원하는 것으로 재정의(overriding) 하는 것

    def walk(self): # def walk(): 시 에러남, self를 적으면 에러가 나지 않음 / self는 파라미터의 맨 앞에 위치함
        print(f'{self.name}, 걷습니다.')
    
    def run(self, option):
        if option == 'Fast':
            self.walk()
            print(f'{self.name}, 빨리 뜁니다.')
        else:
            print(f'{self.name}, 천천히 뜁니다.')
        
    def stop(self):
        self.walk()
        print(f'{self.name}, 멈춥니다.')

    # 2. 생성자 외 매직메서드(펑션) __str__
    def __str__(self) -> str: # 출력 했을 때 뭐가 나오는지 확인하는 함수
        return f'출력: 이름은 {self.name}, 성별은 {self.gender}'

yena = Person('예나', 160, 'female') ## 객체생성 (Instance or object)
# # YENA = PERSON(CLASS)객체를 정의하여 예나라는 명사에 객체를 집어넣음(이 객체를 Instance(class의 실체)라 부름)
# ## class를 정의할 때는 괄호를 쓰지 않는데, person을 만들라는 동사로 괄호를 사용 함 / ## 함수호출
# yena.name = '예나' # 예나라는 객체의 속성에 변수를 지정하면 하나를 지칭하는 그룹이 됨(구조화 됨)
# yena.height = '160' # 원 변수는 하나씩 지정 됨. 그러나 클래스라는 그룹을 만들고, 이름을 지칭하면 하나를 묶게 됨
# yena.gender = 'female' # class = 변수와 함수의 집합
# yena.blood_type = 'RH+ A'

print(f'{yena.name}의 혈액형은 {yena.blood_type}입니다.')

yena.stop() # Fast 옵션을 넣어도 뛸 수 없음. 이유, self가 빠짐 / class 안에 들은 함수는 self를 반드시 넣어줘야 함
print(yena)

### 1. 초기화 후 객체생성
hong = Person()
hong.run('slow')
print(hong)

print("-----------------------")
### 2. 파라미터를 받는 생성자 실행
ashely = Person('애슐리', 165, 'Female') # class 의 객체를 생성하는 생성자 함수와 동일함
print(ashely.name)
print(ashely.height)
print(ashely.gender)
print(ashely.blood_type) # blood type 지정하지 않았기 때문에 a형으로 나옴
print(ashely)

# 매직 메서드는 재정의 __init__