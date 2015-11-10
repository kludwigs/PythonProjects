from Tkinter import *
#from graphics import *
#win = GraphWin()
import ctypes  # An included library with Python install.

__author__ = 'Karl'
print(__author__)


class TicTacToe:
    # used to determine X'x or O's turn

    __turn = False
    __gameover = False

    def __init__(self, master, width, height):

        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenheight()

        # calculate position x and y coordinates
        # center frame
        x = (screen_width / 2) - (width / 2)
        y = (screen_height / 2) - (height / 2)
        # root.geometry('%dx%d+%d+%d' % (width, height, x, y))
        root.geometry('+%d+%d' % (x, y))

        frame = Frame(master)
        frame.grid(row=0, column=0)

        self.btn = [[0 for x in xrange(3)] for x in xrange(3)]
        for x in range(3):
            for y in range(3):
                self.btn[x][y] = Button(frame, text="", height=4, width=8, command=lambda x1=x, y1=y,: self.mark_button
                (x1, y1, (x * 3 + y + 1)))
                self.btn[x][y].grid(row=x + 1, column=y)

    def mark_button(self, x, y, button_number):
        if (self.btn[x][y]['text'] == '' and self.__gameover == False):

            self.__turn = not self.__turn

            if (self.__turn):
                self.btn[x][y]['text'] = 'X'
                # ctypes.windll.user32.MessageBoxA(0, "GameOver", "X wins!", 1)
            else:
                self.btn[x][y]['text'] = '0'
                #

            self.determine_winner()

    def determine_winner(self):
        # across
        # 123, 456, 789
        # diagnoal
        # 159, 753
        # vertical
        # 147, 258, 369

        p1 = self.btn[0][0]['text']
        p2 = self.btn[0][1]['text']
        p3 = self.btn[0][2]['text']
        p4 = self.btn[1][0]['text']
        p5 = self.btn[1][1]['text']
        p6 = self.btn[1][2]['text']
        p7 = self.btn[2][0]['text']
        p8 = self.btn[2][1]['text']
        p9 = self.btn[2][2]['text']

        winner = False

        # across
        if p1 == p2 and p1 == p3 and p1 != "" \
                or p4 == p5 and p4 == p6 and p4 != "" \
                or p7 == p8 and p7 == p9 and p7 != "":
            winner = True
            # diagonals
        elif p1 == p5 and p1 == p9 and p1 != "" \
                or p3 == p5 and p3 == p7 and p3 != "":
            winner = True
        # vertical
        elif p1 == p4 and p1 == p7 and p1 != "" \
                or p2 == p5 and p2 == p8 and p2 != "" \
                or p3 == p6 and p3 == p9 and p3 != "":
            winner = True

        # if a winner display who won
        if winner:
            # game is over
            self.__gameover = True

            # print out who won
            if self.__turn:
                print("X wins")
                ctypes.windll.user32.MessageBoxA(0, "GameOver", "X wins", 1)
            else:
                print("O wins")
                ctypes.windll.user32.MessageBoxA(0, "GameOver", "O wins", 1)


root = Tk()
# app = TicTacToe(root, 198,212)
app = TicTacToe(root, 500, 500)
root.mainloop()
