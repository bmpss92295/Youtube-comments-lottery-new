# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'youtube.ui'
#
# Created by: PyQt5 UI code generator 5.15.7
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(120, 90, 151, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.textEdit = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit.setGeometry(QtCore.QRect(10, 180, 771, 341))
        self.textEdit.setObjectName("textEdit")
        self.URLbutton = QtWidgets.QPushButton(self.centralwidget)
        self.URLbutton.setGeometry(QtCore.QRect(300, 90, 81, 31))
        self.URLbutton.setObjectName("URLbutton")
        self.CB_name = QtWidgets.QCheckBox(self.centralwidget)
        self.CB_name.setGeometry(QtCore.QRect(110, 20, 73, 16))
        self.CB_name.setObjectName("CB_name")
        self.CB_content = QtWidgets.QCheckBox(self.centralwidget)
        self.CB_content.setGeometry(QtCore.QRect(190, 20, 73, 16))
        self.CB_content.setObjectName("CB_content")
        self.CB_time = QtWidgets.QCheckBox(self.centralwidget)
        self.CB_time.setGeometry(QtCore.QRect(30, 20, 73, 16))
        self.CB_time.setObjectName("CB_time")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 90, 191, 31))
        self.label_4.setObjectName("label_4")
        self.dateEdit_1 = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit_1.setGeometry(QtCore.QRect(360, 10, 141, 31))
        self.dateEdit_1.setObjectName("dateEdit_1")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 140, 91, 41))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(520, 10, 21, 31))
        self.label_3.setObjectName("label_3")
        self.dateEdit_2 = QtWidgets.QDateEdit(self.centralwidget)
        self.dateEdit_2.setGeometry(QtCore.QRect(560, 10, 141, 31))
        self.dateEdit_2.setObjectName("dateEdit_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(430, 60, 151, 31))
        self.label.setObjectName("label")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(560, 60, 151, 31))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(430, 120, 191, 31))
        self.label_5.setObjectName("label_5")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(560, 120, 151, 31))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.total = QtWidgets.QLabel(self.centralwidget)
        self.total.setGeometry(QtCore.QRect(20, 530, 91, 41))
        self.total.setObjectName("total")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.URLbutton.setText(_translate("MainWindow", "送出"))
        self.CB_name.setText(_translate("MainWindow", "名稱"))
        self.CB_content.setText(_translate("MainWindow", "內容"))
        self.CB_time.setText(_translate("MainWindow", "時間"))
        self.label_4.setText(_translate("MainWindow", "請輸入影片網址 :"))
        self.label_2.setText(_translate("MainWindow", "顯示結果"))
        self.label_3.setText(_translate("MainWindow", "到"))
        self.label.setText(_translate("MainWindow", "留言須包含特定字串:"))
        self.label_5.setText(_translate("MainWindow", "抽獎功能 : 設定人數"))
        self.total.setText(_translate("MainWindow", "共有 ? 筆資料"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())