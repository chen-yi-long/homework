#主运行文件

from ui_mainwindow import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
from find_class import mainwindow
import sys

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    w = mainwindow()
    w.radioButton_tod.toggled.connect(w.btnstate)
    w.radioButton_tom.toggled.connect(w.btnstate)
    w.radioButton_aft.toggled.connect(w.btnstate)
    w.buttonBox.accepted.connect(w.click_city)
    w.show()
    sys.exit(app.exec_())