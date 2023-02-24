from tkinter import *
import random
def next_turn(row, column):
    global player
    if buttons[row][column]["text"] == "" and wincheck() is False:
        if player == players[0]:
            buttons[row][column]["text"] = player
            if wincheck() is False:
                player = players[1]
                label.config(text=("TURN:" + player))
            if wincheck() is True:
                label.config(text=("WINNER:" + players[0]), bg="#5402CE")
            elif wincheck() == "TIE":
                label.config(text="!!TIE!!", bg="#00FFFF")
        else:
            buttons[row][column]["text"] = player
            if wincheck() is False:
                player = players[0]
                label.config(text=("TURN:" + player))
            if wincheck() is True:
                label.config(text=("WINNER:" + players[1]), bg="#5402CE")
            elif wincheck() == "TIE":
                label.config(text="!!TIE!!", bg="#00FFFF")

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
                buttons[row][column].config(bg="#00FFFF")
        return "TIE"

    else:
        return False
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

def restart():
    global player

    player = random.choice(players)

    label.config(text=("TURN:" + player), bg="#404040")

    for row in range(3):
        for column in range(3):
            buttons[row][column].config(text="", bg="#404040")

window = Tk()
width = 725
height = 730

screen_width = window.winfo_screenwidth()  # Width of the screen
screen_height = window.winfo_screenheight()  # Height of the screen

# Calculate Starting X and Y coordinates for Window
x = (screen_width / 2) - (width / 2)
y = (screen_height / 2) - (height / 2)

window.geometry('%dx%d+%d+%d' % (width, height, x, y))
window.resizable(False, False)
window.configure(bg="#A0A0A0")
window.title("Tic-Tac-Toe")

players = ["X", "O"]
player = random.choice(players)

buttons = [[Button, Button, Button],
           [Button, Button, Button],
           [Button, Button, Button]]

top_frame = Frame(window, bg="#A0A0A0")
top_frame.place(relx=0.01, rely=0.01, relheight=0.15, relwidth=0.98)

label = Label(top_frame, text=("TURN:" + player), font=("Monaco", 35), bg="#404040", fg="#A0A0A0")
label.place(rely=0.01, relheight=0.98, relwidth=0.4)

restart_button = Button(top_frame, text="RESTART", bg="#404040", font=("Monaco", 35), activebackground="#FF3300", fg="#A0A0A0",
                        bd=4, command=restart)
restart_button.place(relx=0.6, rely=0.01, relheight=0.98, relwidth=0.4)

bottom_frame = Frame(window, bg="#A0A0A0")
bottom_frame.place(relx=0.01, rely=0.17, relheight=0.82, relwidth=0.98)

for row in range(3):
    for column in range(3):
        buttons[row][column] = Button(bottom_frame, text="", bg="#404040", font=("Monaco, BOLD", 47), height=2, width=6,
                                      activebackground="#FF3300", fg="#A0A0A0", bd=4,
                                      command=lambda row = row, column = column: next_turn(row, column))
        buttons[row][column].grid(row=row, column=column)


window.mainloop()
