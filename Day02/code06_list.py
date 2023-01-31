# 복합형

# 리스트
# 리스트는 여러개의 값(요소)을 일렬로 늘어놓은 형태. 변수에 값을 지정할 때 대괄호로 묶어주면 리스트, 값은 콤마로 구분함
arr = [1,2,3,4,5,6,7,8,9,10] # 리스트(=배열)는 대괄호 상의 콤마로 구분함 / 같은 값들을 수를 나열할 때 씀. 이것을 배열이라고 함
print(arr)
sum = 0
for i in arr: # for문
    sum += i

print(sum)

arr1 = [1,2,3]
arr2 = [1.1,2.2,3.3]
arr3 = ['Hello', 13, 'World!', True]
print(type(arr3)) # arr3은 정수, 실수, 문자열 함께 있어 list로 작성함
# print('arr1의 2번 인덱스값' + str(arr1[3]))


arr4 = [] # 빈 리스트
arr5 = list()
print(arr5)

arr6 = [1,2,3,4,[6,7,8,[9,10]]] # 3차원 배열, 리스트 안에 리스트를 넣을 수 있음
print(arr6)

arr7 = [[1,2,3,4],[5,6,7,8]] # 2차원 배열
print(arr7)

# 튜플
# 튜플은 여러개의 값(요소)을 일렬로 늘어놓은 형태. 요소의 값을 변경하거나 추가할 수 없고 괄호로 묶어서 튜플과 콤마로 구분함
# 괄호로 묶지 않아도 값만 콤마로 구분하더라도 튜플이 됨
tuple1 = (1,23,4)
print(tuple1)

arr5.append('4')
print(arr5)

# tuple1.append(4)
# print(tuple1) # 튜플은 한 번 만들면 값(변경, 추가)을 넣을 수 없음, 리스트 배열은 한 번 만들어도 값(변경, 추가)을 넣을 수 있음
# 주석처리 단축 키 전체 드래그 후 컨트롤 슬래시

print(type(tuple1))

# 딕셔너리 (비순차적)
# 모든 리스트, 튜플의 처음은 0부터 시작함(0 ~ 9, C언어 기준) / 리스트의 마지막 인덱스(9 이후)는 -1임
# 대괄호 리스트, 중괄호 딕셔너리
# 딕셔너리는 중괄호 안에 키 : 값 형식으로 저장하며, 키와 값은 콤마로 구분함
# 딕셔너리 = { 키1 : 값1, 키2: 값2}
# 프린트 시 딕셔너리에 저장된 값에접근할 때에는 대괄호를 지정해줌
# 형태 잘 기억해 둘것 중괄호, 콜론
spiderman = { 'name' : 'Peter Parker',
              'age' : 18,
              'weapen' : 'Web Shooter'}

print(type(spiderman))
print(spiderman['age']) # 소괄호 후 대괄호시 딕셔너리에 저장 된 나이가 불러와짐
print(spiderman['weapen'])
print(spiderman['name'])

# 집합
set1 = set([1,2,3,4])
print(set1)

set1 = set("Hello World")
print(set1) # 중복값을 제거함, 스페이스도 문자열로 처리하여 나옴
