# Import tkinter to build GUI
import tkinter.font
from tkinter import *
from tkinter import ttk
from colours import *
import random

win = Tk()
fonts = tkinter.font.Font(family='Helvetica', size= 13, weight='bold')
win.title("Password Generator + Saver")

win.maxsize(500, 900)
win.config(bg= LIGHT_GRAY)


typeList = ['No Restrictions', 'No Special Characters', 'Letters Only']
lenList = [8, 9, 10, 11, 12, 13]

character_choices = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*_+'
only_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
no_special_char = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890'

lengthPass = StringVar()

restrict = StringVar()
k = 0

x0 = 10
x1 = 390
y0 = -10
y1 = 10
def passwordGen():
    # Initialize the string the password will be generated to.
    # We want it to be empty since we want it to be randomly generated.
    password = ""
    global x0, x1, y0, y1

    # Recall, type == 2 means that the password is mixed.
    if type_menu.get() == 'No Restrictions':

        global k
        # This for loop runs for the length the user selected.
        for x in range(int(len_menu.get())):
            # Each iteration adds a random character from character_choices using the random.choice() function.
            password += random.choice(character_choices)

        k += 30
        y0 += 30
        y1 += 30

    # Recall, type == 1 means that the password is made only of letters.
    if type_menu.get() == 'Letters Only':
        # This for loop runs for the length the user selected.
        for i in range(int(len_menu.get())):
            # Each iteration adds a random character from character_choices using the random.choice() function.
            password += random.choice(only_letters)
        k += 30
        y0 += 30
        y1 += 30


    if type_menu.get() == 'No Special Characters':
        for x in range(int(len_menu.get())):
            # Each iteration adds a random character from character_choices using the random.choice() function.
            password += random.choice(no_special_char)
        k += 30
        y0 += 30
        y1 += 30

    # stops more elements from being created after capacity threshold is met
    if y0 >= 480:
        return

    # This conditional statement checks if the char at index 0(first char of password) is an a,b,c,s or q.
    win.update_idletasks()
    canvas.create_rectangle(x0, y0, x1, y1, fill=BLACK)

    canvas.create_text(60, k, text=password, fill=WHITE, font= fonts)

    return password



UI_frame = Frame(win, width= 400, height=700, bg=DARK_GRAY)
UI_frame.grid(row=0, column=0, padx=10, pady=10)

l1 = Label(UI_frame, text="Restrictions: ", bg=WHITE)
l1.grid(row=1, column=0, padx=10,pady=5, sticky=W)
type_menu = ttk.Combobox(UI_frame, textvariable= restrict, values=typeList)
type_menu.grid(row =1, column=1, padx=5, pady=5)
type_menu.current(0)

l2 = Label(UI_frame, text="Length: ", bg=WHITE)
l2.grid(row=2, column=0, padx=10,pady=5, sticky=W)
len_menu = ttk.Combobox(UI_frame, textvariable= lengthPass, values=lenList)
len_menu.grid(row =2, column=1, padx=5, pady=5)
len_menu.current(0)

b1 = Button(UI_frame, text="Generate", command=passwordGen, bg=WHITE)
b1.grid(row=3, column=0, padx=0, pady=5)

canvas = Canvas(win, width=400, height=500, bg=DARK_GRAY)
canvas.grid(row=1, column=0, padx=10, pady=5)




win.mainloop()