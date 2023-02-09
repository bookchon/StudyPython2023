# 레이아웃 절대적 배치
import sys
from PyQt5.QtWidgets import *

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        grid = QGridLayout()
        self.setLayout(grid)

        grid.addWidget(QLabel('Title'), 0, 0)
        grid.addWidget(QLabel('Author'), 1, 0)
        grid.addWidget(QLabel('Review'), 2, 0)

        grid.addWidget(QTextEdit(), 0, 1)
        grid.addWidget(QTextEdit(), 1, 2)
        grid.addWidget(QTextEdit(), 2, 3)

        btnOk = QPushButton('OK')
        btnCancel = QPushButton('Cancel')
        grid.addWidget(btnOk, 3, 1)
        grid.addWidget(btnCancel, 4, 1)

        # 필수 설정
        self.setWindowTitle('절대 배치')
        self.setGeometry(300, 300, 300, 300)
        self.show()


if __name__ == '__main__':
    app =  QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())