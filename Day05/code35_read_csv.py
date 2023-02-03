# 공공데이터포털 csv파일 읽기
# 부산광역시 시내버스, 마을버스 현황

import csv
filename = 'busanbus.csv'
dirname = "C:/Source/StudyPython2023/"
fullpath = dirname + filename

file = open(fullpath, 'r', encoding='utf-8')
reader = csv.reader(file, delimiter=',')
next(reader)

for line in reader:
    print(line)

file.close() # 반드시 달아주세요!

 # 자료구조가 리스트로 되어 있음