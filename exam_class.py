from Forms.exam23_window import Ui_ExamWindow
from PyQt5.QtWidgets import QMainWindow
from PyQt5 import QtCore
from functions import *
from Main import ResultDialog, MyDialog
from datetime import datetime
import sqlite3


# Класс проведения тестирования
class Exam(QMainWindow, Ui_ExamWindow):
    def __init__(self):
        super().__init__()
        self.con = sqlite3.connect('data/EGE23.db')
        self.user_answers = {}
        self.right_answers = {}
        self.format_questions = []
        self.current_time = QtCore.QTime(0, 30, 0)
        self.timer = QtCore.QTimer()
        self.exam_time = ''
        self.end = None
        self.results = get_questions(10)
        self.setupUi(self)
        self.BtnEnd.clicked.connect(self.end_of_exam)
        self.BtnNext.clicked.connect(self.next_question)
        self.BtnPrev.clicked.connect(self.prev_question)
        self.BtnSave.clicked.connect(self.save_answer)
        self.start_exam = True
        self.user_name = ''
        self.exam_prepare()
        if self.start_exam:
            self.show()
        else:
            self.close()

    def exam_prepare(self):
        """
        Подготовка данных для начала тестирования.
        Запрашивается имя пользователя. Доступен выбор из БД и добавление нового.
        Запуск таймера тестирования.
        Получение из БД 10 случайных заданий для тестирования. Текст задания преобразуется для корректного
        отображения в форме.
        :return:
        """
        self.user_name = MyDialog().user_input()
        if self.user_name == 'Cancel':
            self.start_exam = False
            return
        self.timer.timeout.connect(self.showTime)
        self.timer.start(1000)
        self.lcd_time.display(self.current_time.toString())
        self.ExamProgress.setValue(0)
        for number, el in enumerate(self.results):
            format_question = el[1].split('|')
            format_question = '\n'.join(format_question)
            self.format_questions.append((format_question, el[0]))
            self.right_answers[number] = el[0], el[2]
        self.update_form()

    def showTime(self):  # функция таймера тестирования
        if self.current_time > QtCore.QTime(0, 0, 0):
            self.current_time = self.current_time.addSecs(-1)
            self.lcd_time.display(self.current_time.toString())
        else:
            self.timer.stop()
            self.time_out()

    def update_form(self, text=''):  # обновление формы тестирования при выборе очередного или предыдущего вопроса
        self.QuestionLabel.setText('Вопрос № ' + str(question_number + 1))
        self.QuestionsText.clear()
        self.AnswerLineEdit.setText(text)
        self.QuestionsText.appendPlainText(self.format_questions[question_number][0])

    def next_question(self):  # выбор следующего вопроса из выбранных для тестирования
        global question_number  # глобальная переменная, хранящая номер вопроса
        if question_number < 9:
            question_number += 1
        if question_number in self.user_answers:
            self.AnswerLineEdit.setText(str(self.user_answers[question_number][1]))
            self.update_form(str(self.user_answers[question_number][1]))
        else:
            self.update_form()

    def prev_question(self):  # выбор предыдущего вопроса из выбранных для тестирования
        global question_number  # глобальная переменная, хранящая номер вопроса
        if question_number > 0:
            question_number -= 1
        if question_number in self.user_answers:
            self.AnswerLineEdit.setText(str(self.user_answers[question_number][1]))
            self.update_form(str(self.user_answers[question_number][1]))
        else:
            self.update_form()

    def save_answer(self):  # промежуточное сохранение ответа пользователя
        try:
            int(self.AnswerLineEdit.text())
        except ValueError:
            wrong_answer(self)
            return None
        if question_number not in self.user_answers:
            self.user_answers[question_number] = \
                self.format_questions[question_number][1], int(self.AnswerLineEdit.text())
            self.ExamProgress.setValue(self.ExamProgress.value() + 10)
        else:
            self.user_answers[question_number] = \
                self.format_questions[question_number][1], int(self.AnswerLineEdit.text())
        self.next_question()

    def time_out(self):  # функция обработки истечения времени тестирования
        self.timer.stop()
        QtWidgets.QMessageBox.critical(None, 'Время истекло!',
                                       'Время, отведенное на выполнение заданий истекло!',
                                       QtWidgets.QMessageBox.Ok)
        self.BtnSave.setDisabled(True)
        self.AnswerLineEdit.setDisabled(True)

    def end_of_exam(self):  # окончание тестирование (нажата кнопка "Закончить тестирование"
        if self.BtnSave.isEnabled() and self.ExamProgress.value() < 100:
            reply = QtWidgets.QMessageBox.critical(None, 'Тестирование пройдено не полностью!',
                                                   'Вы решили не все задания. Уверены, что хотите завершить?',
                                                   QtWidgets.QMessageBox.Ok, QtWidgets.QMessageBox.Cancel)
            if reply == QtWidgets.QMessageBox.Cancel:
                return
            else:
                exam_end = True
        else:
            exam_end = True
        if not exam_end:
            return
        self.timer.stop()  # остановка таймера
        self.BtnSave.setDisabled(True)  # отключение возможности сохранения ответа
        self.AnswerLineEdit.setDisabled(True)  # и изменения ответа
        seconds = [x for x in map(int, self.current_time.toString().split(':'))]
        seconds = 1800 - (seconds[1] * 60 + seconds[2])
        self.exam_time = elapsed_time(seconds)
        exam_results = []
        for ind, answer in self.user_answers.items():
            if self.user_answers[ind] == self.right_answers[ind]:
                exam_results.append(10)
            else:
                exam_results.append(0)
        cur = self.con.cursor()
        all_users_id = cur.execute('''SELECT Id FROM Users''').fetchall()
        cur.execute(''' SELECT Id FROM Users WHERE Name=? ''', (self.user_name,))
        users = cur.fetchall()
        if not users:
            sql_query = """INSERT INTO Users (Name) VALUES
                                           (?);"""
            data = (self.user_name,)
            cur.execute(sql_query, data)
            self.con.commit()
            user_id = all_users_id[-1][0] + 1
        else:
            user_id = users[0][0]
        sql_query = """INSERT INTO Results (User_id, Result, DateOfExam, ExamTime) VALUES
                                        (?, ?, ?, ?);"""
        result = sum(exam_results)
        exam_date = datetime.today().strftime('%Y/%m/%d')

        data = (user_id, result, exam_date, self.exam_time)
        cur.execute(sql_query, data)
        self.con.commit()
        cur.close()
        self.close()
        ResultDialog().run(result, self.exam_time)

# Конец класса проведения тестирования
