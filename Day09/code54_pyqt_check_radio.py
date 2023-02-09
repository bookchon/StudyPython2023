# 체크박스, 라디오버튼
import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import Qt

class MyApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        cbShowTitle = QCheckBox('Show Title', self)
        cbShowTitle.move(20, 20)
        cbShowTitle.toggle()
        # signal 종류 statecganged
        # connect() 매개변수 -> 슬롯함수
        cbShowTitle.stateChanged.connect(self.changeTitle)

        cbkorea = QCheckBox('한국', self)
        cbkorea.move(20, 60)
        cbkorea.stateChanged.connect(self.checkkorea)

        rbMale = QRadioButton('남성', self)
        rbMale.move(150, 20)
        rbMale.setChecked(True)
        rbFemale = QRadioButton('여성', self)
        rbFemale.move(150, 40)

        # 필수 설정
        self.setWindowTitle('절대 배치')
        self.setGeometry(300, 300, 300, 300)
        self.show()

    def checkkorea(self, state):
        if state == Qt.CheckState.Checked:
            self.setWindowTitle('나는 한국인')
        else:
            self.setWindowTitle('None')

    def changeTitle(self, state):
        if state == Qt.CheckState.Checked: # Qt.Checked도 사용가능
            self.setWindowTitle('체크박스 체크')
        else:
            self.setWindowTitle('체크박스 체크 해제')


if __name__ == '__main__':
    app =  QApplication(sys.argv)
    ex = MyApp()
    sys.exit(app.exec_())