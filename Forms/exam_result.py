# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\ExamResultDialog.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(336, 222)
        Dialog.setMinimumSize(QtCore.QSize(336, 222))
        Dialog.setMaximumSize(QtCore.QSize(336, 222))
        font = QtGui.QFont()
        font.setBold(True)
        font.setItalic(False)
        font.setWeight(75)
        Dialog.setFont(font)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./data/img/EGE.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        Dialog.setWindowIcon(icon)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(40, 180, 271, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label_result = QtWidgets.QLabel(Dialog)
        self.label_result.setGeometry(QtCore.QRect(0, 10, 331, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_result.setFont(font)
        self.label_result.setStyleSheet("color: rgb(90, 175, 255)")
        self.label_result.setAlignment(QtCore.Qt.AlignCenter)
        self.label_result.setObjectName("label_result")
        self.label_score = QtWidgets.QLabel(Dialog)
        self.label_score.setGeometry(QtCore.QRect(0, 50, 331, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_score.setFont(font)
        self.label_score.setStyleSheet("color: rgb(90, 175, 255)")
        self.label_score.setAlignment(QtCore.Qt.AlignCenter)
        self.label_score.setObjectName("label_score")
        self.label_result_2 = QtWidgets.QLabel(Dialog)
        self.label_result_2.setGeometry(QtCore.QRect(0, 90, 331, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_result_2.setFont(font)
        self.label_result_2.setStyleSheet("color: rgb(0, 0, 0)")
        self.label_result_2.setAlignment(QtCore.Qt.AlignCenter)
        self.label_result_2.setObjectName("label_result_2")
        self.label_timescore = QtWidgets.QLabel(Dialog)
        self.label_timescore.setGeometry(QtCore.QRect(0, 130, 331, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.label_timescore.setFont(font)
        self.label_timescore.setStyleSheet("color: rgb(0, 0, 0)")
        self.label_timescore.setAlignment(QtCore.Qt.AlignCenter)
        self.label_timescore.setObjectName("label_timescore")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept) # type: ignore
        self.buttonBox.rejected.connect(Dialog.reject) # type: ignore
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Результаты тестирования"))
        self.label_result.setText(_translate("Dialog", "Здесь будет надпись"))
        self.label_score.setText(_translate("Dialog", "Вы набрали 70 баллов"))
        self.label_result_2.setText(_translate("Dialog", "Затрачено времени"))
        self.label_timescore.setText(_translate("Dialog", "17:21"))
