import random
import sys
from functools import partial
from PySide6.QtWidgets import QApplication, QMessageBox, QLCDNumber, QRadioButton
from PySide6.QtUiTools import QUiLoader
from PySide6.QtCore import Qt
###
QApplication.setAttribute(Qt.AA_ShareOpenGLContexts)
app = QApplication(sys.argv)

loader = QUiLoader()
main_window = loader.load("main_window.ui")
main_window.show()

player = "X"
win_count_X = 0
win_count_O = 0
game_mode = 2

lcd_X = main_window.findChild(QLCDNumber, "lcd_X")
lcd_O = main_window.findChild(QLCDNumber, "lcd_O")

def show_info():
    msg_box = QMessageBox(text=""" تیک تاک یک بازی سرگرم کننده برای بازیکن است.
هر بازیکنی که اولین بار بتواند به سرعت یک سطر یا یک ستون یا مربع مورب را پر کند، به عنوان برنده اعلام میشود.
اگر تمام خانه های جدول پر شده باشد و هیچکس موفق به تکمیل شرایط ذکر شده نشود،
بازی مساوی خواهد شد
    """)
    msg_box.exec()
    
    

def set_game_mode():
    global game_mode
    if main_window.one_player.isChecked():
        game_mode = 1
    else:
        game_mode = 2
    print(game_mode)


def new_game():
    for i in range (3):
        for j in range (3):
            cells[i][j].setText("")
            cells[i][j].setStyleSheet("")


def reset():
    new_game()
    global win_count_O, win_count_X
    win_count_X = 0
    win_count_O = 0
    update_lcd_value_X(win_count_X)
    update_lcd_value_O(win_count_O)

def update_lcd_value_X(new_value):
    lcd_X.display(new_value)

def update_lcd_value_O(new_value):
    lcd_O.display(new_value)


def check_game():
    global winner, win_count_X, win_count_O 
    winner = None
    if cells[0][0].text() == cells[1][1].text() == cells[2][2].text() != "":
        winner = cells[0][0].text()
    elif cells[0][2].text() == cells[1][1].text() == cells[2][0].text() != "":
        winner = cells[0][2].text()
    
    for i in range(3):
        if cells[i][0].text() == cells[i][1].text() == cells[i][2].text() !="":       
            winner = cells[i][0].text()
            break    
    for j in range(3):
        if cells[0][j].text() == cells[1][j].text() == cells[2][j].text() !="":
            winner = cells[0][j].text()
            break
    
    if not winner:
        for i in range(3):
            for j in range(3):
                if cells[i][j].text() == "":
                    return
    
        winner = "Nobody"

    if winner:    
        msg_box = QMessageBox(text= f"The Winner is {winner}")
        msg_box.exec()
        new_game()

        if winner == "X":
            win_count_X += 1
            update_lcd_value_X(win_count_X)
        elif winner == "O":
            win_count_O += 1
            update_lcd_value_O(win_count_O)
            


def ai_play():
   
    empty_cells = [(i, j) for i in range(3) for j in range(3) if cells[i][j].text() == ""]
    if empty_cells:
        chosen_cell = random.choice(empty_cells)
        cells[chosen_cell[0]][chosen_cell[1]].setText("O")
        cells[chosen_cell[0]][chosen_cell[1]].setStyleSheet("color: #EFB238; background-color: #1f3540;")
       


def play(row, col):
    global player
    if cells[row][col].text() == "":
        if player == "X":
            cells[row][col].setText("X")
            cells[row][col].setStyleSheet("color: #31C4BE; background-color: #1f3540;")
            player = "O"
            if game_mode == 1:
                ai_play()
                player = "X"


        elif player == "O" and game_mode ==2:
            cells[row][col].setText("O")
            cells[row][col].setStyleSheet("color: #EFB238; background-color: #1f3540;")
            player = "X"


        check_game()
        # print(empty_cells)




cells= [[main_window.btn_1, main_window.btn_2, main_window.btn_3],
           [main_window.btn_4, main_window.btn_5, main_window.btn_6],
           [main_window.btn_7, main_window.btn_8, main_window.btn_9],]


main_window.about_btn.clicked.connect(show_info)
for i in range(3):
    for j in range(3):
        cells[i][j].clicked.connect(partial(play, i, j))

main_window.btn_reset.clicked.connect(reset)


one_player = main_window.findChild(QRadioButton, "one_player")

one_player.toggled.connect(set_game_mode)

app.exec()