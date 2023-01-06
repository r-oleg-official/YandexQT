# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '.\new_task.ui'
#
# Created by: PyQt5 UI code generator 5.15.6
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_new_task(object):
    def setupUi(self, New_task):
        New_task.setObjectName("new_task")
        New_task.setWindowModality(QtCore.Qt.ApplicationModal)
        New_task.resize(943, 345)
        self.centralwidget = QtWidgets.QWidget(New_task)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 10, 281, 21))
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap("./data/img/EGE.png"), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        New_task.setWindowIcon(icon)
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.task_edit = QtWidgets.QPlainTextEdit(self.centralwidget)
        self.task_edit.setGeometry(QtCore.QRect(10, 40, 921, 251))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.task_edit.setFont(font)
        self.task_edit.setObjectName("task_edit")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 300, 281, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        font.setBold(True)
        font.setWeight(75)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.answer_edit = QtWidgets.QLineEdit(self.centralwidget)
        self.answer_edit.setGeometry(QtCore.QRect(280, 300, 111, 31))
        self.answer_edit.setObjectName("answer_edit")
        self.save_btn = QtWidgets.QPushButton(self.centralwidget)
        self.save_btn.setGeometry(QtCore.QRect(720, 300, 101, 31))
        self.save_btn.setObjectName("save_btn")
        self.cancel_btn = QtWidgets.QPushButton(self.centralwidget)
        self.cancel_btn.setGeometry(QtCore.QRect(830, 300, 101, 31))
        self.cancel_btn.setObjectName("cancel_btn")
        New_task.setCentralWidget(self.centralwidget)

        self.retranslateUi(New_task)
        QtCore.QMetaObject.connectSlotsByName(New_task)

    def retranslateUi(self, new_task):
        _translate = QtCore.QCoreApplication.translate
        new_task.setWindowTitle(_translate("new_task", "Новое задание"))
        self.label.setText(_translate("new_task", "Введите текст задания"))
        self.label_2.setText(_translate("new_task", "Введите правильный ответ"))
        self.save_btn.setText(_translate("new_task", "Сохранить"))
        self.cancel_btn.setText(_translate("new_task", "Отмена"))