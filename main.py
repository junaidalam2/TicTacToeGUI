from tkinter import *
from tkinter import messagebox
from tktooltip import ToolTip


board_length = 3
board_height = board_length


root = Tk()
root.title('Tic-Tac-Toe')
p1 = PhotoImage(file='hashtag.png')
root.iconphoto(False, p1)
root.resizable(False, False)

# frames
frame1 = Frame(root)  # display player names, number of games won by each player, reset button
frame1.grid(row=0, column=0, rowspan=2)
frame2 = Frame(root)  # display player with the next turn
frame2.grid(row=0, column=1)
frame3 = Frame(root)  # gameboard
frame3.grid(row=1, column=1)
empty_frame1 = Frame(root, height=10)  # empty frame below gameboard
empty_frame1.grid(row=2, column=0, columnspan=2)
empty_frame2 = Frame(root, width=10)  # empty frame right of gameboard
empty_frame2.grid(row=0, column=2, rowspan=3)

# declaring variables
beg_of_game_turn = True  # player X's turn is True; player O's turn is False
turn = beg_of_game_turn  # player X's turn is True; player O's turn is False
playerx_wincount = 0  # counter for games won by player x
playero_wincount = 0  # counter for games won by player y
draw_game_count = 0  # counter for number of draw games

# set counter variables to strings so can be inputted into label
str_playerx_wincount = StringVar()
str_playerx_wincount.set(str(playerx_wincount))

str_playero_wincount = StringVar()
str_playero_wincount.set(str(playero_wincount))

str_draw_game_count = StringVar()
str_draw_game_count.set(str(draw_game_count))


# message to display when a player wins
def winning_message():
    global playerx_wincount, playero_wincount

    if turn:
        playerx_wincount += 1
        str_playerx_wincount.set(str(playerx_wincount))
        return messagebox.showinfo(title=None, message=f"{name_playerx.get()} wins!")
    else:
        playero_wincount += 1
        str_playero_wincount.set(str(playero_wincount))
        return messagebox.showinfo(title=None, message=f"{name_playero.get()} wins!")


# clear contents of board
def clear_board():
    for i in range(board_length):
        for j in range(board_height):
            buttons[i][j]['text'] = ''


# change color, provide message, return color, clear board
def win_function(btn1, btn2, btn3):
    global beg_of_game_turn

    win_color = '#fca14c'
    start_color ='#add9f0'

    # change color of winning squares
    btn1.config(bg=win_color)
    btn2.config(bg=win_color)
    btn3.config(bg=win_color)

    winning_message()  # win message

    # return winning squares to original color
    btn1.config(bg=start_color)
    btn2.config(bg=start_color)
    btn3.config(bg=start_color)

    clear_board()  # clear board

    beg_of_game_turn = not beg_of_game_turn

    return True


# check for a winning conditions
def check_won():
    # check rows & columns
    for i in range(board_length):
        if buttons[i][0]['text'] == buttons[i][1]['text'] == buttons[i][2]['text'] != '':
            return win_function(buttons[i][0], buttons[i][1], buttons[i][2])

        if buttons[0][i]['text'] == buttons[1][i]['text'] == buttons[2][i]['text'] != '':
            return win_function(buttons[0][i], buttons[1][i], buttons[2][i])

    # check diagonals
    if buttons[0][0]['text'] == buttons[1][1]['text'] == buttons[2][2]['text'] != '':
        return win_function(buttons[0][0], buttons[1][1], buttons[2][2])

    if buttons[0][2]['text'] == buttons[1][1]['text'] == buttons[2][0]['text'] != '':
        return win_function(buttons[0][2], buttons[1][1], buttons[2][0])


# check for draw game
def check_draw():
    global draw_game_count, beg_of_game_turn

    count = 0
    for i in range(board_length):
        for j in range(board_height):
            if buttons[i][j]['text'] != '':
                count += 1
    if count == board_length * board_height:
        draw_game_count += 1
        str_draw_game_count.set(str(draw_game_count))
        messagebox.showinfo(title=None, message="Draw game!")
        clear_board()

    beg_of_game_turn = not beg_of_game_turn


# button clicked function
def click(btn):
    global turn

    if btn['text'] == '' and turn:
        btn['text'] = 'X'
        if not check_won():
            check_draw()
        turn = not turn
        player_next_turn(turn)
    elif btn['text'] == '' and not turn:
        btn['text'] = 'O'
        if not check_won():
            check_draw()
        turn = not turn
        player_next_turn(turn)
    else:
        messagebox.showerror(title=None, message='Please click on an empty square.')


# clear board, set counters to zero, reset names
def reset_match():
    global playerx_wincount, playero_wincount, draw_game_count, beg_of_game_turn

    clear_board()
    playerx_wincount = 0
    playero_wincount = 0
    draw_game_count = 0
    str_playerx_wincount.set(str(playerx_wincount))
    str_playero_wincount.set(str(playero_wincount))
    str_draw_game_count.set(str(draw_game_count))
    name_playerx.set("Player X")
    name_playero.set("Player O")
    beg_of_game_turn = True


# FRAME 1: player names, number of games won by each player, reset button

# column 0
label10 = Label(frame1, text='Player X', fg='#0f274d')
label10.grid(row=1, column=0, padx=10)

blank_label20 = Label(frame1, height=1)
blank_label20.grid(row=2, column=0)

label30 = Label(frame1, text='Player O', fg='#0f274d')
label30.grid(row=3, column=0, padx=10)

# column 1
label01 = Label(frame1, text='Enter Name', fg='#0f274d')
label01.grid(row=0, column=1)

name_playerx = StringVar()
name_playerx.set("Player X")
name_entry11 = Entry(frame1, textvariable=name_playerx, fg='#2d3542')
name_entry11.grid(row=1, column=1)

name_playero = StringVar()
name_playero.set("Player O")
name_entry31 = Entry(frame1, textvariable=name_playero, fg='#2d3542')
name_entry31.grid(row=3, column=1)

# column 2
blank_label02 = Label(frame1, width=1)
blank_label02.grid(row=0, column=2)

# column 3
label03 = Label(frame1, text='Number of Games Won', fg='#0f274d')
label03.grid(row=0, column=3, padx=10)

label13 = Label(frame1, textvariable=str_playerx_wincount, relief=GROOVE, anchor=S, justify=CENTER)
label13.grid(row=1, column=3)

label33 = Label(frame1, textvariable=str_playero_wincount, relief=GROOVE, anchor=S, justify=CENTER)
label33.grid(row=3, column=3)

blank_label43 = Label(frame1, height=1)
blank_label43.grid(row=4, column=3)

label53 = Label(frame1, text='Number of Draw Games', fg='#0f274d')
label53.grid(row=5, column=3, padx=10)

label63 = Label(frame1, textvariable=str_draw_game_count, relief=GROOVE, anchor=S, justify=CENTER)
label63.grid(row=6, column=3)

blank_label73 = Label(frame1, height=1)
blank_label73.grid(row=7, column=3)

button83 = Button(frame1, text='Reset Game', fg='#2d3542', command=lambda: reset_match())
button83.grid(row=8, column=3)
ToolTip(button83, msg="Reset all scores and player names.")


# FRAME 2: player's turn

next_turn = StringVar()


# determines text for text indicating the current player's turn
def player_next_turn(pturn):
    if pturn:
        players_turn_header = 'X'
    else:
        players_turn_header = 'O'

    next_turn.set(f"Player {players_turn_header}'s Turn to Play")


player_next_turn(turn)

player_turn_label = Label(frame2, textvariable=next_turn, font=('Arial bold', 10), fg='#0f274d', pady=5)
player_turn_label.pack()


# FRAME 3: gameboard

# create a list of buttons: name convention 'b + row number + column number'
buttons = [['b' + str(i) + str(j) for j in range(board_height)] for i in range(board_length)]

# create buttons within a 3x3 grid
for i in range(board_length):
    for j in range(board_height):
        buttons[i][j] = Button(frame3, text='', font=('Helvertica', 10), bg='#add9f0', height=6, width=12, command=lambda i=i, j=j: click(buttons[i][j]))
        buttons[i][j].grid(row=i, column=j)

root.mainloop()

