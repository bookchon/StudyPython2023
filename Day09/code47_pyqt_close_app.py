# 윈도우 창닫기 앱
# 2023. 2. 9.

import sys
from PyQt5.QtWidgets import QApplication, QPushButton, QWidget
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import QCoreApplication


class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    # 버튼 만들기
    def initUI(self):
        btn = QPushButton('Quit', self)
        btn.move(300, 150)
        btn.resize(btn.sizeHint())
        # 버튼 툴팁
        btn.setToolTip('누르면 꺼집니다.')
        btn.clicked.connect(QCoreApplication.instance().quit)
        

        self.setWindowIcon(QIcon('./Day09/iot.png'))
        self.setWindowTitle('Quit Button')
        self.setGeometry(1200, 200, 400, 200) # x, y, w, h 위치(x, y), 넓이, 높이, 한번에 설정 가능 
        self.show()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())