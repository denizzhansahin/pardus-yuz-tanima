# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'yeni.ui'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_basarili(object):
    def setupUi(self, basarili):
        basarili.setObjectName("basarili")
        basarili.resize(800, 600)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("/usr/local/bin/icons/pencere_icon.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        basarili.setWindowIcon(icon)
        self.centralwidget = QtWidgets.QWidget(basarili)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(90, 270, 621, 141))
        self.label.setStyleSheet("font: 81 40pt \"Cantarell\";")
        self.label.setObjectName("label")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(240, 520, 301, 20))
        self.label_4.setObjectName("label_4")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(290, 40, 201, 201))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("/usr/local/bin/icons/pencere_icon.png"))
        self.label_2.setObjectName("label_2")
        basarili.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(basarili)
        self.statusbar.setObjectName("statusbar")
        basarili.setStatusBar(self.statusbar)

        self.retranslateUi(basarili)
        QtCore.QMetaObject.connectSlotsByName(basarili)

    def retranslateUi(self, basarili):
        _translate = QtCore.QCoreApplication.translate
        basarili.setWindowTitle(_translate("basarili", "basarili"))
        self.label.setText(_translate("basarili", "<html><head/><body><p align=\"center\"><span style=\" font-weight:600; color:#000000;\">Başarısız Giriş Denemesi</span></p></body></html>"))
        self.label_4.setText(_translate("basarili", "<html><head/><body><p>Denizhan ŞAHİN - <a href=\"www.denizhansahin.com\"><span style=\" text-decoration: underline; color:#0000ff;\">www.denizhansahin.com</span></a></p></body></html>"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    basarili = QtWidgets.QMainWindow()
    ui = Ui_basarili()
    ui.setupUi(basarili)
    basarili.show()
    sys.exit(app.exec_())