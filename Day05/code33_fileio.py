# 파일 만들기
# file = open('C:/DEV/Temp/Bank/sample01.hwp', 'w', encoding='utf-8') # 1 파일 쓰기로 만듦
file = open('./Day05/sample06.txt', 'w', encoding='utf-8') # 1 파일 쓰기로 만듦
# 절대경로 확장자 상관 없이 만들 수 있음(슬래시, 역슬래시 상관 없음)
# 상대경로 .. 부모폴더 . 나

file.write('안녕하세요.\n') # 2
file.write('두번째 파일입니다.\n')
file.write('절대 경로에 파일이 생성 될 겁니다.\n') # 2

file.close() # 1
print('sample06.txt가 생성되었습니다.') #2 

# 글자 인코딩 (encoding='utf-8')
# ASCII -> 한 단어를 표현하는 체계(영어)
# Unicode(UTF-8) -> 모든 나라 언어를 다 표현 가능함

# 파일/폴더 경로
# 절대경로