#Jogo de adivinhação
from os import system
import random

def jogar():
    system('cls')
    print('*'*40)
    print('Bem Vindo no jogo de Adivinhação')
    print('*'*40)

    numero_secreto = random.randrange(1,101)
    rodada = 1
    tentativa = 0
    pontos = 1000
    print('Qual nivel de dificuldade você deseja?')
    print('[1] Fácil\n[2] Médio\n[3] Dificil')

    nivel = int(input("Digite o nível: "))

    if (nivel == 1):
        tentativa = 20
    elif (nivel == 2):
        tentativa = 10
    else:
        tentativa = 5

    while (rodada <= tentativa):
        print('Tentativa {} de {}'.format(rodada,tentativa))
        chute = int(input("Digite um número entre 1 e 100: "))

        if (chute < 1 or chute > 100):
            print('Você deve digitar um número entre 1 e 100')
            continue

        if (numero_secreto == chute):
            print('Você acertou e fez {} pontos'.format(pontos))
            break
        elif (numero_secreto > chute):
            print("O número digitado é menor do que o número sorteado")
            pontos -= abs(numero_secreto - chute)
        else:
            print('O número digitado é maior do que o número sorteado')
            pontos -= abs(numero_secreto - chute)
        rodada += 1
    print('Fim do jogo\nVolte Sempre!!')

if (__name__ == '__main__'):
    jogar()