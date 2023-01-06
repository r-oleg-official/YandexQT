from PyQt5 import QtWidgets
import sqlite3
import random
from functools import lru_cache as lru

question_number = 0


def trajectory_error(self):
    QtWidgets.QMessageBox.critical(self, 'Ошибка в траектории расчёта',
                                   '''Введено неверное значение!\nТраектория вводится целыми числами через пробел!''',
                                   QtWidgets.QMessageBox.Ok)


def commands_empty(self):
    QtWidgets.QMessageBox.critical(self, 'Ошибка в командах', 'Не определено ни одной команды!',
                                   QtWidgets.QMessageBox.Ok)


def commands_error(self):
    QtWidgets.QMessageBox.critical(self, 'Неверное выражение!',
                                   'Неверно заданы команды, либо выражение бессмысленно!',
                                   QtWidgets.QMessageBox.Ok)


def wrong_answer(self):
    QtWidgets.QMessageBox.critical(self, 'Ошибка ввода', 'В поле ответа вводится только числа!',
                                   QtWidgets.QMessageBox.Ok)


def get_questions(n):
    con = sqlite3.connect('data/EGE23.db')
    cur = con.cursor()
    results = []
    rand_num = random.sample(range(1, 51), n)
    for question in rand_num:
        cur.execute(f'''SELECT * FROM Exam WHERE Id = {question}''')
        results.append(list(cur.fetchone()))
    cur.close()
    return results


def elapsed_time(seconds):
    hours = seconds // 3600
    minutes = seconds // 60 - hours * 60
    new_seconds = seconds - hours * 3600 - minutes * 60
    minutes = '0' + str(minutes) if minutes < 10 else str(minutes)
    new_seconds = '0' + str(new_seconds) if new_seconds < 10 else str(new_seconds)
    return minutes + ':' + new_seconds


@lru()
def calculate(start, end, moves, blocked):
    if end < start or start > end or start in blocked:
        return 0
    if end == start:
        return 1
    first_rez = calculate(moves[0][0](start, moves[0][1]), end, moves, blocked) if moves[0][0] != 0 else 0
    second_rez = calculate(moves[1][0](start, moves[1][1]), end, moves, blocked) if moves[1][0] != 0 else 0
    third_rez = calculate(moves[2][0](start, moves[2][1]), end, moves, blocked) if moves[2][0] != 0 else 0
    return first_rez + second_rez + third_rez
