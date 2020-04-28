# coding:utf-8
import sys, os
if hasattr(sys, 'frozen'):
    os.environ['PATH'] = sys._MEIPASS + ";" + os.environ['PATH']
from PyQt5 import  QtWidgets
from PyQt5.QtCore import *
from PyQt5 import QtCore
from PyQt5 import QtGui
class Login(QtWidgets.QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
        self.setFixedSize(200,200)
        self.setWindowFlags(Qt.FramelessWindowHint)  # 去边框
        self.setAttribute(Qt.WA_TranslucentBackground)  # 设置窗口背景透明
        self.label = QtWidgets.QLabel(self)
        self.label.setGeometry(QtCore.QRect(0, 0, 200, 200))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("Project/x.png"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        QtCore.QMetaObject.connectSlotsByName(self)

    def mousePressEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.m_drag = True
            self.m_DragPosition = e.globalPos() - self.pos()
            e.accept()
    def mouseReleaseEvent(self, e):
        if e.button() == Qt.LeftButton:
            self.m_drag = False
    def mouseMoveEvent(self, e):
        try:
            if Qt.LeftButton and self.m_drag:
                self.move(e.globalPos() - self.m_DragPosition)
                e.accept()
        except:
            print("错误代码:000x0")
def main():
    app = QtWidgets.QApplication(sys.argv)
    gui = Login()
    gui.show()
    sys.exit(app.exec_())
if __name__ == '__main__':
    main()
