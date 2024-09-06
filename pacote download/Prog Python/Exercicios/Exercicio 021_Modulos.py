#Faça um programa em python que abra e reproduza o áudio de um arquivo MP3

from pygame import mixer

mixer.init()

mixer.music.load('Queria.mp3')
mixer.music.play()
x = input('Digite a nota que você da pra essa musica: ')

