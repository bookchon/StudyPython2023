import sys
from PyQt5.QtWidgets import QApplication, QWidget
from PyQt5.QtGui import QIcon

class MyApp(QWidget): # 내가 myapp이라는 위젯을 만들 건데, qwidget이라는 부모를 상속 받을 예정임
    
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        # GUI 화면 설정
        self.setWindowTitle('Simple Windows') # 타이틀을 파이썬에서 심플윈도우즈로 바꿈
        # 아이콘 추가
        self.setWindowIcon(QIcon('C:\Source\StudyPython2023\Day09\iot.png'))
        # self.move(1440 // 2 - 200, 900) # 200, 200지점으로 옮김(가운데에서 벗어남) / 경로 위치 잡기
        self.resize(400, 200)
        self.show() # 핵심

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())