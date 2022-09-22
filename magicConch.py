from cgitb import text
import collections
from ctypes import resize
from distutils.cmd import Command
from gc import garbage
import importlib
from math import fabs
from random import random
import tkinter as tk
import random
from tkinter import Canvas, Label, ttk
from turtle import width
from urllib import response
from winsound import PlaySound
from PIL import Image, ImageTk
from playsound import playsound

root=tk.Tk()
root.title("마법의 소라고동")
root.geometry("300x280+100+100")
root.resizable(False, False)

image=tk.PhotoImage(file="소라고동 다시다시다시/magicConch.png")



label=tk.Label(root, image=image)
label.pack()

label1 = tk.Label(root, text="마법의 소라고동님...")
label1.pack()

#사진 바꾸기
def change_a():
    global photo2
    photo2 = tk.PhotoImage(file="소라고동 다시다시다시/magicConch2.png")
    label.config(image=photo2)

#사운드, 텍스트
def ps():
    number=random.randrange(1,11)
    if number == 1:
        label1.config(text='안돼')
        playsound('./소라고동 다시다시다시/sound/안돼.mp3')
    if number == 2:
        label1.config(text='그럼')
        playsound('./소라고동 다시다시다시/sound/그럼.mp3')
    if number == 3:
        label1.config(text='가만히 있어')
        playsound('./소라고동 다시다시다시/sound/가만히 있어.mp3')
    if number == 4:
        label1.config(text='다시 한 번 물어봐')
        playsound('./소라고동 다시다시다시/sound/다시 한 번 물어봐.mp3')
    if number == 5:
        label1.config(text='그것도 안돼')
        playsound('./소라고동 다시다시다시/sound/그것도 안돼.mp3')
    if number == 6:
        label1.config(text='안돼')
        playsound('./소라고동 다시다시다시/sound/안돼2.mp3')
    if number == 7:
        label1.config(text='둘 다 먹지마')
        playsound('./소라고동 다시다시다시/sound/둘 다 먹지마.mp3')
    if number == 8:
        label1.config(text='안돼')
        playsound('./소라고동 다시다시다시/sound/안돼3.mp3')
    if number == 9:
        label1.config(text='안돼')
        playsound('./소라고동 다시다시다시/sound/안돼4.mp3')
    if number == 10:
        label1.config(text='안돼')
        playsound('./소라고동 다시다시다시/sound/안돼5.mp3')

ent = tk.Entry(root)
ent.pack()
    
#질문 텍스트
button1 = tk.Button(root, text="질문하기", command=lambda:[change_a(),ps()])
button1.pack()

root.mainloop()