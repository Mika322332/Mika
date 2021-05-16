from PyQt5.QtCore import Qt
from random import randint ,shuffle
#создай приложение для запоминания информации
from PyQt5.QtWidgets import QApplication, QWidget, QHBoxLayout, QVBoxLayout, QLabel, QPushButton, QRadioButton, QGroupBox, QButtonGroup
class Question():
    def __init__(self, question, right_answer, wrong1, wrong2,wrong3, wrong4, wrong5,):
        self.question = question
        self.right_answer = right_answer
        self.wrong1 = wrong1
        self.wrong2 = wrong2
        self.wrong3 = wrong3
        self.wrong4 = wrong4
        self.wrong5 = wrong5

question_list = []
question_list.append(Question("Какая болезнь бушевала в 2020 году", "Коронавирус", "Грипп", "Свинной грипп", "Птичий грипп", "Простуда", "Ничего не бушевало"))
question_list.append(Question("Какая страна самая большая по площади в мире", "Россия", "Китай", "США", "Казахстан", "Индия", "Франция"))
question_list.append(Question("В какой стране проживает больше всего человек", "Китай", "Россия", "Индия", "США", "Испания", "Великобритания"))
pru = QApplication([])
bgh=QLabel("Caмый главный вопрос")
s1 = QRadioButton("Вариант 1")
s2 = QRadioButton("Вариант 2")
s3 = QRadioButton("Вариант 3")
s4 = QRadioButton("Вариант 4")
s5 = QRadioButton("Вариант 5")
s6 = QRadioButton("Вариант 6")
ok = QWidget()
glava = QVBoxLayout()
glava2 = QVBoxLayout()
a1 = QHBoxLayout()
a2 = QHBoxLayout()
a3 = QHBoxLayout()
a4 = QHBoxLayout()
a5 = QHBoxLayout()
Radio=QButtonGroup()
Radio.addButton(s1)
Radio.addButton(s2)
Radio.addButton(s3)
Radio.addButton(s4)
Radio.addButton(s5)
Radio.addButton(s6)
aqs=QGroupBox("Варианты ответов:")
h1 = QPushButton("Ответить")


glava.addWidget(s1)
glava.addWidget(s2)
glava.addWidget(s3)

glava2.addWidget(s4)
glava2.addWidget(s5)
glava2.addWidget(s6)

a3.addLayout(glava)
a3.addLayout(glava2)

aqs.setLayout(a3)
ansgroupbo = QGroupBox("Результат")
ib = QLabel("Прав ты или нет?")
ibc=QLabel("Ответ будет тут!")




clacc = QVBoxLayout()
clacc.addWidget(ib)
clacc.addWidget(ibc)

ansgroupbo.setLayout(clacc)

asd = QHBoxLayout()
ash = QHBoxLayout()
asw = QHBoxLayout() 
asd.addWidget(bgh,alignment=Qt.AlignHCenter)
ash.addWidget(aqs)
ash.addWidget(ansgroupbo)

ansgroupbo.hide()
aqs.show()
asw.addWidget(h1)

aww=QVBoxLayout()

aww.addLayout(asd)
aww.addLayout(ash)
aww.addLayout(asw)
ok.setLayout(aww)
def show_result():
    aqs.hide()
    ansgroupbo.show()
    h1.setText("Следущий вопрос")
def show_question():
    aqs.show()
    ansgroupbo.hide()
    h1.setText("Ответить")
    Radio.setExclusive(False)
    s1.setChecked(False)
    s2.setChecked(False)
    s3.setChecked(False)
    s4.setChecked(False)
    s5.setChecked(False)
    s6.setChecked(False)
    Radio.setsetExclusive(True)

ansfer = [s1, s2, s3, s4, s5, s6]

def ask(q:Question):
    shuffle(answers)
    answers[0].setText(q.right_answer)
    answers[1].setText(q.wrong1)
    answers[2].setText(q.wrong2)
    answers[3].setText(q.wrong3)
    answers[4].setText(q.wrong4)
    answers[5].setText(q.wrong5)
    ib.setText(q.question)
    ibc.setText(q.right_answer)
def show_correct(res):
    ib.setText(res)
    show_result()
def check_answer():
    ib.setText(res)
    show_result()
def check_answer():
    if answers[0].isChecked():
        show_correct("Правильно!")
    else:
            if answer[1].isChecked() or answer[2].isChecked or answer[3].isChecked:
                    show_correct("Неверно")
                    print("Рейтинг: ", (window.score/window.total*100), "%")
def next_question():
        window.total += 1
        print("Статистика/n-Всего вопросов: ", window.total,"\n-Правильных ответов: ",window.score)
        



ok.show()
pru.exec()