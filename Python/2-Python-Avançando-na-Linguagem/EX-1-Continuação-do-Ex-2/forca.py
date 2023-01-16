def msg(txt):
    #Mensagem
    print('*'*40)
    print(f'{txt:^40}')
    print('*'*40)


def sortear_palavra():
    #Sortear uma fruta no arquivo palavras.txt
    from random import randrange
    arquivo = open('Python\Python-Avançando-na-Linguagem\EX-1-Continuação-do-Ex-2\palavras.txt', 'r')
    palavras = []
    for linha in arquivo:
        linha = linha.strip()
        palavras.append(linha)
    arquivo.close()
    return palavras[randrange(0,len(palavras))]


def printa(lista):
    for i in lista:
        print(i,end=' ')


def marca_chute_correto(chute,secreta,lista):
    if chute in secreta:
            for i in range(0,len(secreta)):
                if (chute == secreta[i]):
                    lista[i] = chute


def enforca(secreta):
    print("Puxa, você foi enforcado!")
    print("A palavra era {}".format(secreta))
    print("    _______________         ")
    print("   /               \       ")
    print("  /                 \      ")
    print("//                   \/\  ")
    print("\|   XXXX     XXXX   | /   ")
    print(" |   XXXX     XXXX   |/     ")
    print(" |   XXX       XXX   |      ")
    print(" |                   |      ")
    print(" \__      XXX      __/     ")
    print("   |\     XXX     /|       ")
    print("   | |           | |        ")
    print("   | I I I I I I I |        ")
    print("   |  I I I I I I  |        ")
    print("   \_             _/       ")
    print("     \_         _/         ")
    print("       \_______/           ")



def ganha():
    print("Parabéns, você ganhou!")
    print("       ___________      ")
    print("      '._==_==_=_.'     ")
    print("      .-\\:      /-.    ")
    print("     | (|:.     |) |    ")
    print("      '-|:.     |-'     ")
    print("        \\::.    /      ")
    print("         '::. .'        ")
    print("           ) (          ")
    print("         _.' '._        ")
    print("        '-------'       ")



def desenha_forca(erros):
    #Toda vez que acontece um erro mostra a forca e vai aumenta o personagem, quando o personagem aparece todo o jogo acaba em derrota
    print("  _______     ")
    print(" |/      |    ")

    if(erros == 1):
        print(" |      (_)   ")
        print(" |            ")
        print(" |            ")
        print(" |            ")

    elif(erros == 2):
        print(" |      (_)   ")
        print(" |      \     ")
        print(" |            ")
        print(" |            ")

    elif(erros == 3):
        print(" |      (_)   ")
        print(" |      \|    ")
        print(" |            ")
        print(" |            ")

    elif(erros == 4):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |            ")
        print(" |            ")

    elif(erros == 5):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |            ")

    elif(erros == 6):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      /     ")

    elif (erros == 7):
        print(" |      (_)   ")
        print(" |      \|/   ")
        print(" |       |    ")
        print(" |      / \   ")

    print(" |            ")
    print("_|___         ")
    print()


def jogar():
    msg('Bem Vindo no jogo da Forca')

    secreta = sortear_palavra()

    lista = ['_' for letra in secreta]
    
    enforcou = False
    ganhou = False
    erro = 0
    
    msg(f'A palavra secreta possue {len(secreta)} letras')


    while (not ganhou) and (not enforcou):
        printa(lista)
        
        print('')
        chute = str(input("Digite uma letra para o Chute: ")).strip().lower()[0]

        if (chute in secreta):
            marca_chute_correto(chute,secreta,lista)
        else:
            erro += 1
            desenha_forca(erro)

        ganhou = ('_' not in lista)
        enforcou = (erro == 7)
    if (ganhou):
        ganha()
    else:
        enforca(secreta)

    
if (__name__ == '__main__'):
    jogar()