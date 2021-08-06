from tkinter import *
import pygame
from threading import Thread
import time 

main = Tk()
main.title("Piano Python")
main.geometry("775x400")
main.maxsize(775,400)
main.configure(background="#03BB85")
pygame.mixer.init()
pygame.init()

class Piano:
    def __init__ (self, main):
        self.main = main
        self.teclas = dict()
        self.pretas_temp = dict()

        

        self.teclas_para_reproduzir = list() # lista q ira armazenar as notas q estão sendo gravadas
        self.tempo_teclas_para_reproduzir = list()
        ## Display

        self.apresentar=Label(main,text="Bem vindo ao Piano Virtual! \n Obrigado pela preferência :) \n Criado por Gabriel Gardini \n @ggardini1",font=("Helvetica",15),bg= "#03BB85",fg="white")
        self.apresentar.place(x=188,y=25,width=400,height=100)

        ## Recording

        self.is_recording = False

        self.botao_gravar_img=PhotoImage(file="imagens\gravar.png")
        self.img_label_gravar=Label(image=self.botao_gravar_img)

        self.botao_parar_img=PhotoImage(file="imagens\parar.png")
        self.img_label_parar=Label(image=self.botao_parar_img)
        

        self.botao_gravar = Button(main, image=self.botao_gravar_img, command=self.record)
        self.botao_gravar.place(x=725,y=30)
        
        
        ## Play recorded button

        self.botao_play_img=PhotoImage(file="imagens\play.png")
        self.img_label_play=Label(image=self.botao_parar_img)

        self.botao_play = Button(main, image=self.botao_play_img, command=self.save_playlist, state='disabled')
        self.botao_play.place(x=725, y=80)


        self.nome_notas = [
            "Dó3", "Ré", "Mi", "Fá", "Sol","Lá","Si",
            "Dó4","Ré","Mi", "Fá", "Sol", "Lá", "Si",
            "Dó5", "Ré", "Mi", "Fá", "Sol", " ",
            ]
        
        self.nome_notas_numerada = [
            "c3", "d3", "e3", "f3", "g3","a4","b4",
            "c4","d4","e4", "f4", "g4", "a5", "b5",
            "c5", "d5", "e5", "f5", "g5", " ",
            ]
        
        self.notas_pretas = [
            "Dó#", "Ré#", "Fá#", "Sol#","Lá#",
            "Dó#","Ré#", "Fá#", "Sol#", "Lá#",
            "Dó#", "Ré#", "Fá#", "Sol#", " ",
            ]

        self.notas_pretas_numeradas = [
            "c-3", "d-3", "f-3", "g-3","a-4",
            "c-4","d-4", "f-4", "g-4", "a-5",
            "c-5", "d-5", "f-5", "g-5", " ",
            ]

        ## Teclas brancas

        for i in range(20):
            self.tecla = Button(main, text=self.nome_notas[i], anchor=S)
            self.tecla.place(x=i*40, y=150, width=40, height=250)
            self.teclas[self.tecla] = self.nome_notas_numerada[i]
            self.tecla.bind('<Button-1>', self.tocar)

        ## Teclas Pretas

        aux = 25
        count = -1

        for i in range(1, 7):

            if i % 2 == 0:
                u = 3
            else:
                u = 2

            for j in range(u):
                count +=1 
                self.tecla_preta = Button(main, text=f't{j}',bg='black', fg='white', anchor=S)
                self.tecla_preta.place(x=aux, y=150, width=30, height=180)
                self.pretas_temp[f'tecla {count}'] = self.tecla_preta
                aux += 40

            aux += 40

        ## nomeia teclas pretas

        for i in range(len(self.notas_pretas)):
            self.t = self.pretas_temp[f'tecla {i}']
            self.t.bind('<Button-1>', self.tocar)
            self.teclas[self.t] = self.notas_pretas_numeradas[i]
            self.t['text'] = self.notas_pretas[i]


    def tocar(self, event):
        nota = self.teclas[event.widget]
        pygame.mixer.music.load(f"sons\{nota}.mp3")
        pygame.mixer.music.play(loops=0)
        if self.is_recording:
            time  = self.clock.tick()
            self.teclas_para_reproduzir.append(nota)            
            self.tempo_teclas_para_reproduzir.append(time)
            print(f'{nota} demora {time}ms')

    def record(self):
        self.is_recording = True
        self.clock = pygame.time.Clock()
        self.botao_gravar.config(image=self.botao_parar_img, command=self.stop_recording, relief='sunken')
        self.teclas_para_reproduzir = list()
        self.tempo_teclas_para_reproduzir = list()
        self.play_button_is_active = False
        self.botao_play.config(state='disabled')


    def stop_recording(self):
        self.is_recording = False
        self.botao_gravar.config(image=self.botao_gravar_img, command=self.record, relief='raised')
        if self.teclas_para_reproduzir != []:
            self.botao_play.config(state='normal')


    def save_playlist(self):
        playlist = []
        for nota in self.teclas_para_reproduzir:
            playlist.append(f"sons\{nota}.mp3")

        if self.tempo_teclas_para_reproduzir[-1] != 0:
            self.tempo_teclas_para_reproduzir.append(0)

        self.run_playlist(playlist, 0, 1)

    def run_playlist(self, playlist, playlist_index, tick_index):
        if playlist_index < len(playlist):
            self.botao_play.config(state='disabled')
            self.botao_gravar.config(state='disabled')
            pygame.mixer.music.load(playlist[playlist_index])
            pygame.mixer.music.play()
            print(f'{playlist[playlist_index]} rodou aos {self.tempo_teclas_para_reproduzir[tick_index]}ms')
            self.main.after(self.tempo_teclas_para_reproduzir[tick_index], lambda pl = playlist, i = playlist_index+1, j = tick_index+1: self.run_playlist(pl, i, j))
        else:
            self.botao_play.config(state='normal')
            self.botao_gravar.config(state='normal')


j = Piano(main)

main.mainloop()
