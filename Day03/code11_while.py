# while문
hit = 0 # 변수 초기화 (0으로 초기화 함)

while hit < 11: # while이 11보다 작을 동안
    #while True = 끝이 나지 않고 계속 감
    hit += 1 # hit를 1씩 증가 시킴
    print(f'{hit}번째 시작')
    print(f'나무를 {hit}번 찍었습니다.') # 한 번 찍었다고 안내
    if hit == 10: # 만약 while의 hit가 10번이 되면
        print('나무가 넘어갔습니다.\n')
        break # 멈춤
    else:
            print('나무가 아직 넘어가지 않았습니다.\n')
            # 9번까지 실행하였을 때 아직 넘어가지 않았기 때문에 처음으로 돌아감
print('나무찍기 완료.')