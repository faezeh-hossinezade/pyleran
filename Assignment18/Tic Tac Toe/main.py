import sys
from functools import partial
from PySide6.QtWidgets import QApplication,QMessageBox
from PySide6.QtUiTools import QUiLoader
from random import randint


    
# app=QApplication([])
app=QApplication(sys.argv)
player=1
loader=QUiLoader()
main_window=loader.load("main_window.ui")
main_window.show()


cells=[[main_window.btn_1, main_window.btn_2, main_window, main_window.btn_3],
       [main_window.btn_4, main_window.btn_5, main_window, main_window.btn_6],
       [main_window.btn_7, main_window.btn_8, main_window, main_window.btn_9]]


def check():
    if "X" == cells[0][0].text() == cells[1][1].text() == cells[2][2].text() or "X" == cells[0][2].text() == cells[1][1].text() == cells[2][0].text():
        return "player 1"
    elif "O" == cells[0][0].text() == cells[1][1].text() == cells[2][2].text() or "O" == cells[0][2].text() == cells[1][1].text() == cells[2][0].text():
        return "player 2"
    for i in range(3):
        if "X" == cells[i][0].text() == cells[i][1].text() == cells[i][2].text() or "X" == cells[0][i].text() ==cells[1][i].text() == cells[2][i].text():
            return "player 1"
        elif "O" == cells[i][0].text() ==cells[i][1].text() == cells[i][2].text() or "O" == cells[0][i].text() ==cells[1][i].text() ==cells[2][i].text():
            return "player 2"
        
    #####
    msg_box=QMessageBox(title="Congrajulation",text="Player one wins!")
    msg_box.exec()
    
    
def reset_game():
    global player
    player = 1
    for i in range(len(cells)):
        for j in range(len(cells[i])):
            cells[i][j].setText("")    
    
    
mode = "vs-cpu" if main_window.player_vs_cpu.isChecked() else "vs-player"
main_window.show()

def play(row,col):
    global player
    global cells
    if cells[row][col].text() == "":
        if player == 1:
            cells[row][col].setStyleSheet("color: #31C4BE; background-color: #1f3540;")
            cells[row][col].setText("X")
            if mode != "vs-cpu":
                player = 2
        else:
            cells[row][col].setStyleSheet("color: #EFB238; background-color: #1f3540;")
            cells[row][col].setText("O")
            player = 1
        winner = check()
        if winner:
            update_labels(winner)
        elif mode == "vs-cpu":
            row = randint(0, 2)
            col = randint(0, 2)
            while cells[row][col].text() != '':
                row = randint(0, 2)
                col = randint(0, 2)
            cells[row][col].setStyleSheet("color: #EFB238; background-color: #1f3540;")
            cells[row][col].setText('O')
            winner = check()
            if winner:
                update_labels(winner)
        else:
            msg = QMessageBox(text="It can't be done here! choose again.")
            msg.exec()

        
def new_game():
    global score_me, score_you, draw
    score_me = 0
    main_window.scored_me.setText(str(score_me))
    score_you = 0
    main_window.scored_you.setText(str( score_you))
    draw = 0
    main_window.scored_non.setText(str(draw))
    reset_game()


def show_info():
    msg_box = QMessageBox(text=""" تیک تاک یک بازی سرگرم کننده برای بازیکن است.
هر بازیکنی که اولین بار بتواند به سرعت یک سطر یا یک ستون یا مربع مورب را پر کند، به عنوان برنده اعلام میشود.
اگر تمام خانه های جدول پر شده باشد و هیچکس موفق به تکمیل شرایط ذکر شده نشود،
بازی مساوی خواهد شد
    """)
    msg_box.exec()

def change_player(player):
    global mode
    if player != mode:
        mode = player
        if player == "vs-cpu":
            main_window.you_btn.setText("O (CPU)")
        else:
            main_window.you_btn.setText("O (PLAYER 2)")
        new_game()


def update_labels(winner):
    global score_me, score_you, draw
    if winner == "player 1":
        score_me += 1
        main_window.scored_me.setText(str(score_me))
        msg_box = QMessageBox(text="You win")
    elif winner == "player 2":
        score_you += 1
        main_window.scored_you.setText(str(score_you))
        if mode == "vs-player":
            msg_box = QMessageBox(text="Player 2 wins")
        else:
            msg_box = QMessageBox(text="CPU wins")
    else:
        draw += 1
        main_window.score_non.setText(str(draw))
        msg_box = QMessageBox(text="Draw!")
    msg_box.exec()
    reset_game()
    
    
# for i in range (3):
#     for j in range (3):
#         cells[i][j].clicked.connect(partial(play,i,j))
        
### 40:54  

main_window.reset_btn.clicked.connect(new_game)
main_window.player_vs_cpu.clicked.connect(partial(change_player, "vs-cpu"))
main_window.player_vs_player.clicked.connect(partial(change_player, "vs-player"))
main_window.about_btn.clicked.connect(show_info)




main_window.btn_1.clicked.connect(partial(play,0,0))
main_window.btn_2.clicked.connect(partial(play,0,1))
main_window.btn_3.clicked.connect(partial(play,0,3))
main_window.btn_4.clicked.connect(partial(play,1,0))
main_window.btn_5.clicked.connect(partial(play,1,1))
main_window.btn_6.clicked.connect(partial(play,1,3))
main_window.btn_7.clicked.connect(partial(play,2,0))
main_window.btn_8.clicked.connect(partial(play,2,1))
main_window.btn_9.clicked.connect(partial(play,2,3))

app.exec()