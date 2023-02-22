from tkinter import *
import random
players = ["X", "O"]
player = random.choice(players)


def empty_spaces():
    spaces = 9
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
                label.config(text=("TURN:" + player), font=("Monaco", 52))
            if wincheck() is True:
                label.config(text=("WINNER:" + players[0]), font=("Monaco", 52))
            elif wincheck() is "TIE":
                label.config(text="TIE", font=("Monaco", 52))
        elif player == players[1]:
            if wincheck() is False:
                buttons[row][column]["text"] = player
                player = players[0]
                label.config(text=("TURN:" + player), font=("Monaco", 52))
            if wincheck() is True:
                label.config(text=("WINNER:" + players[1]), font=("Monaco", 52))
            elif wincheck() is "TIE":
                label.config(text="TIE", font=("Monaco", 52))

window = Tk()
window.geometry("700x700")
window.title("Tic-Tac-Toe")

top_frame = Frame(window, bg="red")
top_frame.place(rely=0.02, relx=0.02, relheight=0.15, relwidth=0.96)
bottom_frame = Frame(window)
bottom_frame.place(rely=0.19, relx=0.02, relheight=0.79, relwidth=0.96)

label = Label(top_frame, text=("TURN:" + player), font=("Monaco", 52))
label.pack(side=LEFT)

buttons = [[0, 0, 0],
           [0, 0, 0],
           [0, 0, 0]]



for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(bottom_frame, text="", bg="#404040", font=("Monaco", 40),
                                      command=lambda row = row, column = column: next_turn(row, column))
        buttons[row][column].place(rely=column*0.33, relx=row*0.33, relwidth=0.33+row*0.33, relheight=0.33+column*0.33)
window.mainloop()

