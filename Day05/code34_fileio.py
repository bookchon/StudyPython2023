# 파일 읽어오기
file = open('./Day05/sample06.txt', 'r', encoding='utf-8')

while True:
    text = file.read()

    if not text: break

    print(text)

file.close() # 파일을 오픈 하면 무조건 close를 해야 함. 다른 언어에서는 읽히지 않음`    `