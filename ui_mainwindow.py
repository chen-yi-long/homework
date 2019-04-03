# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.11.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(300, 400)
        #window_pale = QtGui.QPalette()
        #window_pale.setBrush(self.backgroundRole(), QtGui.QBrush(QtGui.QPixmap("D:\Documents\Pictures\Saved Pictures\cloud.jpg")))
        #self.setPalette(window_pale)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.buttonBox = QtWidgets.QDialogButtonBox(self.centralwidget)
        self.buttonBox.setGeometry(QtCore.QRect(72, 170, 151, 31))
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.output_text = QtWidgets.QTextBrowser(self.centralwidget)
        self.output_text.setGeometry(QtCore.QRect(72, 199, 151, 101))
        self.output_text.setObjectName("output_text")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(72, 128, 54, 16))
        self.label_2.setObjectName("label_2")
        self.input_city = QtWidgets.QLineEdit(self.centralwidget)
        self.input_city.setGeometry(QtCore.QRect(72, 102, 151, 21))
        self.input_city.setObjectName("input_city")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(72, 84, 54, 16))
        self.label.setObjectName("label")
        self.layoutWidget = QtWidgets.QWidget(self.centralwidget)
        self.layoutWidget.setGeometry(QtCore.QRect(70, 150, 155, 18))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.radioButton_tod = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton_tod.setObjectName("radioButton_tod")
        self.horizontalLayout_2.addWidget(self.radioButton_tod)
        self.radioButton_tom = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton_tom.setObjectName("radioButton_tom")
        self.horizontalLayout_2.addWidget(self.radioButton_tom)
        self.radioButton_aft = QtWidgets.QRadioButton(self.layoutWidget)
        self.radioButton_aft.setObjectName("radioButton_aft")
        self.horizontalLayout_2.addWidget(self.radioButton_aft)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 23))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)
        self.buttonBox.rejected.connect(MainWindow.close)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "城市天气查询器"))
        self.label_2.setText(_translate("MainWindow", "Date/日期"))
        self.label.setText(_translate("MainWindow", "City/城市"))
        self.radioButton_tod.setText(_translate("MainWindow", "今天"))
        self.radioButton_tom.setText(_translate("MainWindow", "明天"))
        self.radioButton_aft.setText(_translate("MainWindow", "后天"))
        self.output_text.setText("Hello，欢迎您的使用!")

