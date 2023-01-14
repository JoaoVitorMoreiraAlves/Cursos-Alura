from time import sleep
import adivinhacao, forca
print('*'*40)
print('Bem vindo ao Menu de Jogos')
print('*'*40)
print('[1] Forca\n[2] Adivinhação')
jogo = int(input("Qual jogo deseja jogar?: "))

if (jogo == 1):
    print('Iniciando jogo da forca...')
    sleep(2)
    forca.jogar()
elif (jogo == 2):
    print('Iniciando o jogo da Adivinhação...')
    sleep(2)
    adivinhacao.jogar()