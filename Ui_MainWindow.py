# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '/home/zhyu/workspace/PyDDosTool/MainWindow.ui'
#
# Created: Thu Oct 18 11:25:05 2012
#      by: pyside-uic 0.2.13 running on PySide 1.1.1
#
# WARNING! All changes made in this file will be lost!

from PySide import QtCore, QtGui

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(381, 213)
        self.centralWidget = QtGui.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.domainInput = QtGui.QLineEdit(self.centralWidget)
        self.domainInput.setGeometry(QtCore.QRect(90, 30, 131, 31))
        self.domainInput.setObjectName("domainInput")
        self.ipInput = QtGui.QLineEdit(self.centralWidget)
        self.ipInput.setGeometry(QtCore.QRect(90, 70, 131, 31))
        self.ipInput.setObjectName("ipInput")
        self.portInput = QtGui.QLineEdit(self.centralWidget)
        self.portInput.setGeometry(QtCore.QRect(90, 110, 131, 31))
        self.portInput.setObjectName("portInput")
        self.btnGrp = QtGui.QGroupBox(self.centralWidget)
        self.btnGrp.setGeometry(QtCore.QRect(240, 10, 120, 151))
        self.btnGrp.setObjectName("btnGrp")
        self.icmpChk = QtGui.QRadioButton(self.btnGrp)
        self.icmpChk.setGeometry(QtCore.QRect(10, 120, 94, 21))
        self.icmpChk.setObjectName("icmpChk")
        self.synChk = QtGui.QRadioButton(self.btnGrp)
        self.synChk.setGeometry(QtCore.QRect(10, 30, 94, 21))
        self.synChk.setChecked(True)
        self.synChk.setObjectName("synChk")
        self.udpChk = QtGui.QRadioButton(self.btnGrp)
        self.udpChk.setGeometry(QtCore.QRect(10, 90, 94, 21))
        self.udpChk.setObjectName("udpChk")
        self.tcpChk = QtGui.QRadioButton(self.btnGrp)
        self.tcpChk.setGeometry(QtCore.QRect(10, 60, 94, 21))
        self.tcpChk.setObjectName("tcpChk")
        self.getIPBtn = QtGui.QPushButton(self.centralWidget)
        self.getIPBtn.setGeometry(QtCore.QRect(20, 170, 91, 23))
        self.getIPBtn.setObjectName("getIPBtn")
        self.AtkBtn = QtGui.QPushButton(self.centralWidget)
        self.AtkBtn.setGeometry(QtCore.QRect(130, 170, 91, 23))
        self.AtkBtn.setObjectName("AtkBtn")
        self.StopBtn = QtGui.QPushButton(self.centralWidget)
        self.StopBtn.setGeometry(QtCore.QRect(240, 170, 91, 23))
        self.StopBtn.setObjectName("StopBtn")
        self.lb_1 = QtGui.QLabel(self.centralWidget)
        self.lb_1.setGeometry(QtCore.QRect(30, 40, 52, 14))
        self.lb_1.setObjectName("lb_1")
        self.lb_2 = QtGui.QLabel(self.centralWidget)
        self.lb_2.setGeometry(QtCore.QRect(30, 80, 52, 14))
        self.lb_2.setObjectName("lb_2")
        self.lb_3 = QtGui.QLabel(self.centralWidget)
        self.lb_3.setGeometry(QtCore.QRect(30, 120, 52, 14))
        self.lb_3.setObjectName("lb_3")
        MainWindow.setCentralWidget(self.centralWidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QtGui.QApplication.translate("MainWindow", "PyDDosTool", None, QtGui.QApplication.UnicodeUTF8))
        self.domainInput.setText(QtGui.QApplication.translate("MainWindow", "server.com", None, QtGui.QApplication.UnicodeUTF8))
        self.ipInput.setText(QtGui.QApplication.translate("MainWindow", "1.2.3.4", None, QtGui.QApplication.UnicodeUTF8))
        self.portInput.setText(QtGui.QApplication.translate("MainWindow", "80", None, QtGui.QApplication.UnicodeUTF8))
        self.btnGrp.setTitle(QtGui.QApplication.translate("MainWindow", "攻击类型:", None, QtGui.QApplication.UnicodeUTF8))
        self.icmpChk.setText(QtGui.QApplication.translate("MainWindow", "ICMP Flood", None, QtGui.QApplication.UnicodeUTF8))
        self.synChk.setText(QtGui.QApplication.translate("MainWindow", "SYN Flood", None, QtGui.QApplication.UnicodeUTF8))
        self.udpChk.setText(QtGui.QApplication.translate("MainWindow", "UDP Flood", None, QtGui.QApplication.UnicodeUTF8))
        self.tcpChk.setText(QtGui.QApplication.translate("MainWindow", "TCP Flood", None, QtGui.QApplication.UnicodeUTF8))
        self.getIPBtn.setText(QtGui.QApplication.translate("MainWindow", "获取IP", None, QtGui.QApplication.UnicodeUTF8))
        self.AtkBtn.setText(QtGui.QApplication.translate("MainWindow", "攻击", None, QtGui.QApplication.UnicodeUTF8))
        self.StopBtn.setText(QtGui.QApplication.translate("MainWindow", "停止", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_1.setText(QtGui.QApplication.translate("MainWindow", "目标域名:", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_2.setText(QtGui.QApplication.translate("MainWindow", "目标IP:", None, QtGui.QApplication.UnicodeUTF8))
        self.lb_3.setText(QtGui.QApplication.translate("MainWindow", "目标端口:", None, QtGui.QApplication.UnicodeUTF8))


if __name__ == "__main__":
    import sys
    app = QtGui.QApplication(sys.argv)
    MainWindow = QtGui.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
