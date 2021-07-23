from tkinter import *
import pygame

janela = Tk()
janela.title("Piano Python")
janela.geometry("775x400")
janela.maxsize(775,400)
janela.configure(background="#03BB85")

pygame.mixer.init()

teclas = dict()

pretas_temp = dict()

nome_notas = [
    "Dó3", "Ré", "Mi", "Fá", "Sol","Lá","Si",
    "Dó4","Ré","Mi", "Fá", "Sol", "Lá", "Si",
    "Dó5", "Ré", "Mi", "Fá", "Sol", " ",
    ]

nome_notas_numerada = [
    "c3", "d3", "e3", "f3", "g3","a4","b4",
    "c4","d4","e4", "f4", "g4", "a5", "b5",
    "c5", "d5", "e5", "f5", "g5", " ",
    ]

notas_pretas = [
    "Dó#", "Ré#", "Fá#", "Sol#","Lá#",
    "Dó#","Ré#", "Fá#", "Sol#", "Lá#",
    "Dó#", "Ré#", "Fá#", "Sol#", " ",
    ]

notas_pretas_numeradas = [
    "c-3", "d-3", "f-3", "g-3","a-4",
    "c-4","d-4", "f-4", "g-4", "a-5",
    "c-5", "d-5", "f-5", "g-5", " ",
    ]

def tocar_branco(event):
    nota = teclas[event.widget]
    pygame.mixer.music.load(f"sons\{nota}.mp3")
    pygame.mixer.music.play(loops=0)

for i in range(20):
    tecla = Button(janela, text=nome_notas[i], anchor=S)
    tecla.place(x=i*40, y=150, width=40, height=250)
    teclas[tecla] = nome_notas_numerada[i]
    tecla.bind('<Button-1>', tocar_branco)

# Teclas Pretas

aux = 25
count = -1

for i in range(1, 7):

    if i % 2 == 0:
        u = 3
    else:
        u = 2

    for j in range(u):
        count +=1 
        tecla_preta = Button(janela, text=f't{j}',bg='black', fg='white', anchor=S)
        tecla_preta.place(x=aux, y=150, width=30, height=180)
        pretas_temp[f'tecla {count}'] = tecla_preta
        aux += 40

    aux += 40

for i in range(len(notas_pretas)):
    t = pretas_temp[f'tecla {i}']
    t.bind('<Button-1>', tocar_branco)
    teclas[t] = notas_pretas_numeradas[i]
    t['text'] = notas_pretas[i]

apresentar=Label(janela,text="Bem vindo ao Piano Virtual! \n Obrigado pela preferência :) \n Criado por Gabriel Gardini \n @ggardini1",font=("Helvetica",15),bg= "#03BB85",fg="white")
apresentar.place(x=188,y=25,width=400,height=100)
janela.mainloop()
