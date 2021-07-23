from tkinter import *
import pygame

janela = Tk()
janela.title("Piano Python")
janela.geometry("800x500")
janela.configure(background="#FFFF00")

pygame.mixer.init()

def play_do():
    pygame.mixer.music.load("C:\\Users\Gabri\Desktop\piano\sons\do.mp3")
    pygame.mixer.music.play(loops=0)

def play_re():
    pygame.mixer.music.load("C:\\Users\Gabri\Desktop\piano\sons\\re.mp3")
    pygame.mixer.music.play(loops=0)

def play_mi():
    pygame.mixer.music.load("C:\\Users\Gabri\Desktop\piano\sons\mi.mp3")
    pygame.mixer.music.play(loops=0)

def play_fa():
    pygame.mixer.music.load("C:\\Users\Gabri\Desktop\piano\sons\\fa.mp3")
    pygame.mixer.music.play(loops=0)

def play_sol():
    pygame.mixer.music.load("C:\\Users\Gabri\Desktop\piano\sons\sol.mp3")
    pygame.mixer.music.play(loops=0)

def play_la():
    pygame.mixer.music.load("C:\\Users\Gabri\Desktop\piano\sons\la.mp3")
    pygame.mixer.music.play(loops=0)

def play_si():
    pygame.mixer.music.load("C:\\Users\Gabri\Desktop\piano\sons\si.mp3")
    pygame.mixer.music.play(loops=0)

def play_doo():
    pygame.mixer.music.load("C:\\Users\Gabri\Desktop\piano\sons\doo.mp3")
    pygame.mixer.music.play(loops=0)

#teclas pretas

def play_reb():
    pygame.mixer.music.load("C:\\Users\Gabri\Desktop\piano\sons\do#.mp3")
    pygame.mixer.music.play(loops=0)

def play_mib():
    pygame.mixer.music.load("C:\\Users\Gabri\Desktop\piano\sons\\re#.mp3")
    pygame.mixer.music.play(loops=0)

def play_solb():
    pygame.mixer.music.load("C:\\Users\Gabri\Desktop\piano\sons\\fa#.mp3")
    pygame.mixer.music.play(loops=0)

def play_lab():
    pygame.mixer.music.load("C:\\Users\Gabri\Desktop\piano\sons\sol#.mp3")
    pygame.mixer.music.play(loops=0)

def play_sib():
    pygame.mixer.music.load("C:\\Users\Gabri\Desktop\piano\sons\la#.mp3")
    pygame.mixer.music.play(loops=0)


#Teclas Brancas
do = Button(janela, text="Dó", command=play_do)
do.place(x=0, y=250, width=100, height=250)

re = Button(janela, text="Ré",command=play_re)
re.place(x=100, y=250, width=100, height=250)

mi = Button(janela, text="Mi",command=play_mi)
mi.place(x=200, y=250, width=100, height=250)

fa = Button(janela, text="Fá",command=play_fa)
fa.place(x=300, y=250, width=100, height=250)

sol = Button(janela, text="Sol",command=play_sol)
sol.place(x=400, y=250, width=100, height=250)

la = Button(janela, text="Lá",command=play_la)
la.place(x=500, y=250, width=100, height=250)

si = Button(janela, text="Si",command=play_si)
si.place(x=600, y=250, width=100, height=250)

doo = Button(janela, text="Dó",command=play_doo)
doo.place(x=700, y=250, width=100, height=250)

#Teclas Pretas

reb = Button(janela, text="Dó#", bg="black", fg="white",command=play_reb)
reb.place(x=60, y=250, width=80, height=200)

mib = Button(janela, text="Ré#", bg="black", fg="white",command=play_mib)
mib.place(x=160, y=50, width=80, height=200)

solb = Button(janela, text="Fá#", bg="black", fg="white",command=play_solb)
solb.place(x=360, y=50, width=80, height=200)

lab = Button(janela, text="Sol#", bg="black", fg="white",command=play_lab)
lab.place(x=460, y=50, width=80, height=200)

sib = Button(janela, text="Lá#", bg="black", fg="white",command=play_sib)
sib.place(x=560, y=50, width=80, height=200)




janela.mainloop()
