class Conta:

    def __init__(self,numero,titular,saldo,limite):
        print(f'Construindo Objeto...\n{self}')
        self.__numero = numero
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite


    @property
    def numero(self):
        return self.__numero
    

    @property
    def titular(self):
        return self.__titular.title()
    

    @property
    def saldo(self):
        return self.__saldo
    


    #Método estático(ou seja o método é da classe e não é necessário instancia um objeto para executa-lo)
    @staticmethod
    def codigo_banco():
        return '001'


    @staticmethod
    def codigos_bancos():
        return {'BB': '001', 'Caixa': '104', 'Bradesco': '237'}

        
     #O @Property serve para poder chamar o método limite sem precisar utilizar o get_limite, basta utilizar variavel.limite
    @property
    def limite(self):
        return self.__limite


    #O @setter serve para poder chamar o método limite sem precisar utilizar o set_limite, basta somente utilizar variavel.limite = valor
    @limite.setter
    def limite(self,limite):
        self.__limite = limite


    def extrato(self):
        print(f'O saldo do titular {self.__titular} é de {self.__saldo} reais')


    def deposita(self,valor):
        self.__saldo += valor
    
    
    def __pode_sacar(self, valor):
        return valor <= self.__saldo + self.__limite


    def saque(self,valor):
        if (self.__pode_sacar(valor)):
            self.__saldo -= valor
        else:
            print(f'O valor {valor} passou do limite')

    def transfere(self,valor,destino):
        self.saque(valor)
        destino.deposita(valor)