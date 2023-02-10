# 라인 에디트 - textbox
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *

class MyApp(QWidget):

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        pixmap = QPixmap('./Day10/cat.png')

        lblimage =  QLabel(self)
        lblimage.setPixmap(pixmap)
        lblSize =  QLabel(str(pixmap.width()) + 'x' + str(pixmap.height()))
        lblSize.setAlignment(Qt.AlignmentFlag.AlignCenter) # Qt.AlignCenter 가능

        vbox = QVBoxLayout(self)
        vbox.addWidget(lblimage)
        vbox.addWidget(lblSize)

        self.setLayout(vbox)
        
        # 필수설정
        self.setWindowTitle('이미지 위젯')
        # self.setGeometry(300, 300, 300, 300)
        self.showFullScreen() # self.show() 본인 사이즈
    
        # 화면 중심 세팅
    def setCenter(self):
        qr = self.frameGeometry() # 윈도우 자기 자신의 위치 값을 위한 설정값
        cp = QDesktopWidget().availableGeometry().center() # 모니터 화면 중심
        qr.moveCenter(cp)
        self.move(qr.topLeft())

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())