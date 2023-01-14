from os import system
def jogar():
    system('cls')
    print('*'*40)
    print('Bem Vindo no jogo da Forca')
    print('*'*40)

    palavra_secreta = 'banana'
    enforcou = False
    acertou = False
    lista = ['_','_','_','_','_','_']
    #Enquanto não enforcou E não acertou ele continua a permitir o usuário responder!
    print(f'A Palavra secreta possue {len(palavra_secreta)} letras')
    while (not enforcou and not acertou):
        for i in lista:
            print(i,end='')
        print('')
        chute = str(input("Digite uma letra: ")).strip()
        if (chute == palavra_secreta):
            print('Parabéns você acertou a palavra')
            break
        else:
            if (chute in palavra_secreta):
            for i in range(0,len(palavra_secreta)):
                if (chute.lower()[0] == palavra_secreta[i]):
                    lista[i] = chute.lower().strip()[0]
        
if (__name__ == '__main__'):
    jogar()