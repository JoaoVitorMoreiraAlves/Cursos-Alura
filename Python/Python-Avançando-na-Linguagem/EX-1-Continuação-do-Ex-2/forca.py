from os import system
def jogar():
    system('cls')
    print('*'*40)
    print('Bem Vindo no jogo da Forca')
    print('*'*40)

    secreta = 'dia-a-dia'
    lista = []
    for letra in secreta:
        if letra == '-':
            lista.append('-')
        else:
            lista.append('_')
    enforcou = False
    ganhou = False
    erro = 6
    print(f'A palavra secreta possue {len(secreta)} letras')
    while (not ganhou) and (not enforcou):
        print(f'Você possue {erro} tentativas')
        for i in lista:
            print(i,end=' ')
        print('')
        chute = str(input("Digite uma letra para o Chute: ")).strip().lower()[0]
        erro -= 1
        if chute in secreta:
            for i in range(0,len(secreta)):
                if (chute == secreta[i]):
                    lista[i] = chute
            ganhou = ('_' not in lista)
        else:
            enforcou = (erro < 1)
        system('cls')
    if (ganhou):
        print(f'Parabéns você ganhou a palavra secreta era {secreta.upper()}!!')
    else:
        print(f"Você enforcou a palavra secreta era {secreta}")
if (__name__ == '__main__'):
    jogar()