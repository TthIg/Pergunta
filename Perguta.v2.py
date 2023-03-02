import tkinter as tk
from tkinter import*
import random


root=tk.Tk()
root.title("Supreme Question")
root.configure(background="#c8c8c8")
root.resizable(False, False)
root.geometry('1268x200')

def hover(event):
    x = random.randint(10, 900)
    y = random.randint(60, 160)
    nao.place(x=x, y=y)

def mensagem():
    message = tk.Label(root, text='hmm :D',
                font=("Georgia", 12), bg="#c8c8c8", fg="black")
    message.place(x=140, y=120, relx=0, rely=0)

pergunta = tk.Label(root, text='is Thiago Monteiro Cerqueira belonging to CPF **6.**8.**5-61,it is a fantastic person and the bestest volleyball player of the holy world,besides of a exeptional basketball player!?',
                font=("Georgia", 12), bg="#c8c8c8", fg="black")
pergunta.grid(column=0, row=0)

nao = tk.Button(root, text='nop',
                font=("Georgia", 12), bg="#c8c8c8", fg="red", bd=0, highlightthickness=0)
nao.place(x=438, y=100)
nao.bind('<Enter>', hover)

sim = tk.Button(root, text='OF COURSE,HE`S THE BEST EVERYTHING', command=mensagem,
                font=("Georgia", 12), bg="#c8c8c8", fg="green", bd=0, highlightthickness=0)
sim.place(x=630, y=100)

root.mainloop()
