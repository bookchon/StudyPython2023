# 변수 variable(변동이 심한, 가변적인)
# 변수에서 값을 다 못 담고 넘치는 것을 overflow라고 함
val = 'hello'
print(val) # type = string

val = 3.1415
print(val) # type = float

val = 10 // 2
print(val) # type = int
print(id(val))
 # val이라는 변수에다 hello를 넣고 val을 출력
 # id는 실행 될 때마다 바뀜

# 변수명 단어들의 조합
plant_major_upper_code = 'U13TEMP'
 # 변수명 중 특수문자 중에서 유일하게 쓸 수 있는 것 underbar(_)
 # 변수명 지정 시 앞에 숫자가 오는 것은 변수명으로 지정이 되지 않음
 # 빨간색 밑줄 = 오류, TAB은 들여쓰기, PYTHON은 세미콜론이 존재하지 않아서 들여쓰기를 잘못하면 오류 남
print(id(plant_major_upper_code))
# 모든 변수는 id가 정해져있음, 컴퓨터 메모리 상에 저장 됨. id를 치면 메모리의 id가 나옴