from tkinter import *
import random
players = ["X", "O"]
player = random.choice(players)
spaces = 9

def empty_spaces():
    global spaces
    for row in range(3):
        for column in range(3):
            if buttons[row][column]["text"] != "":
                spaces -= 1
    if spaces == 0:
        return False
    else:
        return True


def wincheck():
    for row in range(3):
        if buttons[row][0]['text'] == buttons[row][1]['text'] == buttons[row][2]['text'] != "":
            buttons[row][0].config(bg="#5402CE")
            buttons[row][1].config(bg="#5402CE")
            buttons[row][2].config(bg="#5402CE")
            return True

    for column in range(3):
        if buttons[0][column]['text'] == buttons[1][column]['text'] == buttons[2][column]['text'] != "":
            buttons[0][column].config(bg="#5402CE")
            buttons[1][column].config(bg="#5402CE")
            buttons[2][column].config(bg="#5402CE")
            return True

    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != "":
        buttons[0][0].config(bg="#5402CE")
        buttons[1][1].config(bg="#5402CE")
        buttons[2][2].config(bg="#5402CE")
        return True

    elif buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != "":
        buttons[0][2].config(bg="#5402CE")
        buttons[1][1].config(bg="#5402CE")
        buttons[2][0].config(bg="#5402CE")
        return True

    elif empty_spaces() is False:

        for row in range(3):
            for column in range(3):
                buttons[row][column].config(bg="yellow")
        return "TIE"

    else:
        return False


def next_turn(row, column):
    global player
    if buttons[row][column]["text"] == "" and wincheck() is False:
        if player == players[0]:
            if wincheck() is False:
                buttons[row][column]["text"] = player
                player = players[1]
                label.config(text=("TURN:" + player), font=("Monaco, BOLD", 45))
            if wincheck() is True:
                label.config(text=("WINNER:" + players[0]), font=("Monaco, BOLD", 45))
            elif wincheck() == "TIE":
                label.config(text="TIE", font=("Monaco, BOLD", 45))
        elif player == players[1]:
            if wincheck() is False:
                buttons[row][column]["text"] = player
                player = players[0]
                label.config(text=("TURN:" + player), font=("Monaco, BOLD", 45))
            if wincheck() is True:
                label.config(text=("WINNER:" + players[1]), font=("Monaco, BOLD", 45))
            elif wincheck() == "TIE":
                label.config(text="TIE", font=("Monaco, BOLD", 45))

def restart():
    global buttons
    global spaces
    global player

    spaces = 9
    player = random.choice(players)
    label.config(text=("TURN:" + player), font=("Monaco, BOLD", 45), bg="#404040")

    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="", bg="#404040")

window = Tk()
window.geometry("700x670")
window.maxsize(700, 670)
window.minsize(700, 670)
window.configure(bg="black")
window.title("Tic-Tac-Toe")

top_frame = Frame(window)
top_frame.place(rely=0.01, relx=0.02, relheight=0.13, relwidth=0.96)
bottom_frame = Frame(window)
bottom_frame.place(rely=0.15, relx=0.02, relheight=0.86, relwidth=0.96)

label = Label(top_frame, text=("TURN:" + player), font=("Monaco, BOLD", 45), bg="#404040")
label.place(relx=0, rely=0, relheight=1, relwidth=0.50)

buttons = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(bottom_frame, text="", bg="#404040", font=("Monaco, BOLD", 46), height=2, width=6,
                                      command=lambda row = row, column = column: next_turn(row, column))
        buttons[row][column].grid(row=row, column=column)

restart_button = Button(top_frame, text="RESTART", bg="#404040", font=("Monaco, BOLD", 45), command=restart())
restart_button.place(relx=0.50, rely=0, relheight=1, relwidth=0.50)

window.mainloop()
