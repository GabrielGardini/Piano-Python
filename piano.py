from tkinter import *
import pygame

janela = Tk()
janela.title("Piano Python")
janela.geometry("775x400")
janela.maxsize(775,400)
janela.configure(background="#03BB85")

pygame.mixer.init()

def play_c3():
    pygame.mixer.music.load("sons\c3.mp3")
    pygame.mixer.music.play(loops=0)

def play_d3():
    pygame.mixer.music.load("sons\\d3.mp3")
    pygame.mixer.music.play(loops=0)

def play_e3():
    pygame.mixer.music.load("sons\e3.mp3")
    pygame.mixer.music.play(loops=0)

def play_f3():
    pygame.mixer.music.load("sons\\f3.mp3")
    pygame.mixer.music.play(loops=0)

def play_g3():
    pygame.mixer.music.load("sons\g3.mp3")
    pygame.mixer.music.play(loops=0)

def play_a4():
    pygame.mixer.music.load("sons\\a4.mp3")
    pygame.mixer.music.play(loops=0)

def play_b4():
    pygame.mixer.music.load("sons\\b4.mp3")
    pygame.mixer.music.play(loops=0)

def play_c4():
    pygame.mixer.music.load("sons\c4.mp3")
    pygame.mixer.music.play(loops=0)

def play_d4():
    pygame.mixer.music.load("sons\\d4.mp3")
    pygame.mixer.music.play(loops=0)

def play_e4():
    pygame.mixer.music.load("sons\e4.mp3")
    pygame.mixer.music.play(loops=0)

def play_f4():
    pygame.mixer.music.load("sons\\f4.mp3")
    pygame.mixer.music.play(loops=0)

def play_g4():
    pygame.mixer.music.load("sons\g4.mp3")
    pygame.mixer.music.play(loops=0)

def play_a5():
    pygame.mixer.music.load("sons\\a5.mp3")
    pygame.mixer.music.play(loops=0)

def play_b5():
    pygame.mixer.music.load("sons\\b5.mp3")
    pygame.mixer.music.play(loops=0)

def play_c5():
    pygame.mixer.music.load("sons\c5.mp3")
    pygame.mixer.music.play(loops=0)

def play_d5():
    pygame.mixer.music.load("sons\\d5.mp3")
    pygame.mixer.music.play(loops=0)

def play_e5():
    pygame.mixer.music.load("sons\e5.mp3")
    pygame.mixer.music.play(loops=0)

def play_f5():
    pygame.mixer.music.load("sons\\f5.mp3")
    pygame.mixer.music.play(loops=0)

def play_g5():
    pygame.mixer.music.load("sons\g5.mp3")
    pygame.mixer.music.play(loops=0)



#teclas pretas

def play_c_3():
    pygame.mixer.music.load("sons\c-3.mp3")
    pygame.mixer.music.play(loops=0)

def play_d_3():
    pygame.mixer.music.load("sons\\d-3.mp3")
    pygame.mixer.music.play(loops=0)

def play_f_3():
    pygame.mixer.music.load("sons\\f-3.mp3")
    pygame.mixer.music.play(loops=0)

def play_g_3():
    pygame.mixer.music.load("sons\g-3.mp3")
    pygame.mixer.music.play(loops=0)

def play_a_4():
    pygame.mixer.music.load("sons\\a-4.mp3")
    pygame.mixer.music.play(loops=0)

def play_c_4():
    pygame.mixer.music.load("sons\c-4.mp3")
    pygame.mixer.music.play(loops=0)

def play_d_4():
    pygame.mixer.music.load("sons\\d-4.mp3")
    pygame.mixer.music.play(loops=0)

def play_f_4():
    pygame.mixer.music.load("sons\\f-4.mp3")
    pygame.mixer.music.play(loops=0)

def play_g_4():
    pygame.mixer.music.load("sons\g-4.mp3")
    pygame.mixer.music.play(loops=0)

def play_a_5():
    pygame.mixer.music.load("sons\\a-5.mp3")
    pygame.mixer.music.play(loops=0)

def play_c_5():
    pygame.mixer.music.load("sons\c-5.mp3")
    pygame.mixer.music.play(loops=0)

def play_d_5():
    pygame.mixer.music.load("sons\\d-5.mp3")
    pygame.mixer.music.play(loops=0)

def play_f_5():
    pygame.mixer.music.load("sons\\f-5.mp3")
    pygame.mixer.music.play(loops=0)

def play_g_5():
    pygame.mixer.music.load("sons\g-5.mp3")
    pygame.mixer.music.play(loops=0)



#Teclas Brancas
c3 = Button(janela, text="Dó3", command=play_c3, anchor=S)
c3.place(x=0,y=150, width=40, height=250)

d3 = Button(janela, text="Ré",command=play_d3, anchor=S)
d3.place(x=40,y=150, width=40, height=250)

e3 = Button(janela, text="Mi",command=play_e3, anchor=S)
e3.place(x=80,y=150, width=40, height=250)

f3 = Button(janela, text="Fá",command=play_f3, anchor=S)
f3.place(x=120,y=150, width=40, height=250)

g3 = Button(janela, text="Sol",command=play_g3, anchor=S)
g3.place(x=160,y=150, width=40, height=250)

a4 = Button(janela, text="Lá",command=play_a4, anchor=S)
a4.place(x=200,y=150, width=40, height=250)

b4 = Button(janela, text="Si",command=play_b4, anchor=S)
b4.place(x=240,y=150, width=40, height=250)

c4 = Button(janela, text="Dó4",command=play_c4, anchor=S)
c4.place(x=280,y=150, width=40, height=250)

d4 = Button(janela, text="Ré",command=play_d4, anchor=S)
d4.place(x=320,y=150, width=40, height=250)

e4 = Button(janela, text="Mi",command=play_e4, anchor=S)
e4.place(x=360,y=150, width=40, height=250)

f4 = Button(janela, text="Fá",command=play_f4, anchor=S)
f4.place(x=400,y=150, width=40, height=250)

g4 = Button(janela, text="Sol",command=play_g4, anchor=S)
g4.place(x=440,y=150, width=40, height=250)

a5 = Button(janela, text="Lá",command=play_a5, anchor=S)
a5.place(x=480,y=150, width=40, height=250)

b5 = Button(janela, text="Si",command=play_b5, anchor=S)
b5.place(x=520,y=150, width=40, height=250)

c5 = Button(janela, text="Dó5",command=play_c5, anchor=S)
c5.place(x=560,y=150, width=40, height=250)

d5 = Button(janela, text="Ré",command=play_d5, anchor=S)
d5.place(x=600,y=150, width=40, height=250)

e5 = Button(janela, text="Mi",command=play_e5, anchor=S)
e5.place(x=640,y=150, width=40, height=250)

f5 = Button(janela, text="Fá",command=play_f5, anchor=S)
f5.place(x=680,y=150, width=40, height=250)

g5 = Button(janela, text="Sol",command=play_g5, anchor=S)
g5.place(x=720,y=150, width=40, height=250)

#Teclas Pretas

c_3 = Button(janela, text="Dó#", bg="black", fg="white",command=play_c_3, anchor=S)
c_3.place(x=25,y=150, width=30, height=180)

d_3 = Button(janela, text="Ré#", bg="black", fg="white",command=play_d_3, anchor=S)
d_3.place(x=65,y=150, width=30, height=180)

f_3 = Button(janela, text="Fá#", bg="black", fg="white",command=play_f_3, anchor=S)
f_3.place(x=145,y=150, width=30, height=180)

g_3 = Button(janela, text="Sol#", bg="black", fg="white",command=play_g_3, anchor=S)
g_3.place(x=185,y=150, width=30, height=180)

a_4 = Button(janela, text="Lá#", bg="black", fg="white",command=play_a_4, anchor=S)
a_4.place(x=225,y=150, width=30, height=180)

c_4 = Button(janela, text="Dó#", bg="black", fg="white",command=play_c_4, anchor=S)
c_4.place(x=305,y=150, width=30, height=180)

d_4 = Button(janela, text="Ré#", bg="black", fg="white",command=play_d_4, anchor=S)
d_4.place(x=345,y=150, width=30, height=180)

f_4 = Button(janela, text="Fá#", bg="black", fg="white",command=play_f_4, anchor=S)
f_4.place(x=425,y=150, width=30, height=180)

g_4 = Button(janela, text="Sol#", bg="black", fg="white",command=play_g_4, anchor=S)
g_4.place(x=465,y=150, width=30, height=180)

a_5 = Button(janela, text="Lá#", bg="black", fg="white",command=play_a_5, anchor=S)
a_5.place(x=505,y=150, width=30, height=180)

c_5 = Button(janela, text="Dó#", bg="black", fg="white",command=play_c_5, anchor=S)
c_5.place(x=585,y=150, width=30, height=180)

d_5 = Button(janela, text="Ré#", bg="black", fg="white",command=play_d_5, anchor=S)
d_5.place(x=625,y=150, width=30, height=180)

f_5 = Button(janela, text="Fá#", bg="black", fg="white",command=play_f_5, anchor=S)
f_5.place(x=705,y=150, width=30, height=180)

g_5 = Button(janela, text="Sol#", bg="black", fg="white",command=play_g_5, anchor=S)
g_5.place(x=745,y=150, width=30, height=180)

apresentar=Label(janela,text="Bem vindo ao Piano Virtual! \n Obrigado pela preferência :) \n Criado por Gabriel Gardini \n @ggardini1",font=("Helvetica",15),bg= "#03BB85",fg="white")
apresentar.place(x=188,y=25,width=400,height=100)

tapa_buraco=Button(janela)
tapa_buraco.place(x=760,y=330,width=30,height=70)

janela.mainloop()
