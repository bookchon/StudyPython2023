# for문
arr = [1,2,3,4,5]
# i 는 item의 준말
sum = 0
for item in arr:
    print(item) # arr에 리스트가 들어감
    # for를 만나서 인덱스 0번이 item 안으로 들어감. 그리고 출력이 끝나면 다시 처음부터 재실행.
    sum += item # +=는 sum = sum + item과 동일

print('합계는', sum) # 최종 출력 프린트는 for 문과 같은 어미로 취급함(띄어쓰기를 for문과 동일하게 맞춤)


# 홀짝
# 리스트를 편하게 만드는 방법
vals = [i for i in range(1, 11)]
# range(범위) 10까지 쓰려면 11까지 써야함
# for i in range를 i안에 집어넣으라는 명령어
print(vals)

# countinue / break
num = 0 
for item in vals: 
    num += 1 # 넘버에 1을 더함(아이템 값과 달라 새로 num를 만듦)
    if num % 2 == 0:
        # continue # 이후의 것을 수행하지 않고 다시 for문으로 되돌아감
                   # 열 번 반복 할 때마다 1씩 추가시킴
                   # 리스트 10번까지 나누어 0이 남지 않는 경우 else를 출력하고, 0이 남으면 처음부터 재실행함
                   # 컨티뉴는 재실행하고, 브레이크는 for문에 부합 시 완전히 탈출하고 끝남
        break # break를 만나면 for문을 완전히 탈출
              # countinue와 break를 for문에서만 사용함 
              # countinue처럼 재실행하지 않음
    else:
        print(num, '번 수는', item, '입니다.')

# range는 범위를 만듦
