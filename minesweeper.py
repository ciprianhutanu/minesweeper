from tkinter import *
from matrixgeneration import *

mainscreen = Tk()

mainscreen.title("Minesweeper")

def nonecompletion(x, y):
    global Lf, colordict, n, m, Checker
    df = [1, 0, -1, 0, 1, 1, -1, -1]
    ds = [0, 1, 0, -1, 1, -1, -1, 1]
    for i in range(8):
        copyx = x + df[i]
        copyy = y + ds[i]
        if 0 <= copyx < n and 0 <= copyy < m and Checker[copyx][copyy] == 0:
            button_change(copyx, copyy)


def button_change(x, y):
    global Lf, colordict, n, m, Checker
    aux = Lf[x][y]
    Checker[x][y] = 1
    b = Button(mainscreen, width=5, height=2, text=f"{aux}", font='arial 9 bold', foreground=colordict[aux], background='dark gray', borderwidth=0)
    b.grid(row=x, column=y, padx=0, pady=0)
    if aux == 0:
        nonecompletion(x, y)
    


n = 10
m = 13
bombs = 14

Lb = bombgeneration(n, m, bombs)
Lf = bombsneighbourhood(Lb, n, m)
Checker = [[0]*m for x in range(n)]
colordict = {0:'gray',1:'blue', 2:'green', 3:'orange', 4:'purple', 5:'red', 6:'yellow', 7:'black', 8:'black', 9:'red'}

for i in range(n):
    for j in range(m):
        b = Button(mainscreen, width=5, height=2, command=lambda x=i, y=j: button_change(x, y))
        b.grid(row=i, column=j, padx=0, pady=0)


mainscreen.mainloop()