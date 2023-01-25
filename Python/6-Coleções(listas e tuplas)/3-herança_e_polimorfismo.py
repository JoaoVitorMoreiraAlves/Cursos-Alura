from abc import ABCMeta, abstractmethod
class Conta(metaclass=ABCMeta):
    def __init__(self,codigo):
        self._codigo = codigo
        self._saldo = 0
    
    def deposita(self,valor):
        self._saldo += valor
    
    @abstractmethod
    def passa_o_mes(self):
        pass

    def __str__(self):
        return f'O código é {self._codigo} e o saldo é {self._saldo}'
    
   

print('-'*40)


class ContaCorrente(Conta):
    def passa_o_mes(self):
        self._saldo -= 2

class ContaPoupanca(Conta):
    def passa_o_mes(self):
        self._saldo *= 1.01
        self._saldo -= 3

conta16 = ContaCorrente(16)
conta16.deposita(1000)
conta16.passa_o_mes()
print(conta16) #Como a conta16 é do tipo conta corrente ao passar o mes é retirado da conta como juros 2 reais portanto o saldo q inicialmente era de 1k foi pra 998
print('-'*40)
conta17 = ContaPoupanca(17)
conta17.deposita(1000)
conta17.passa_o_mes()
print(conta17)#Como a conta17 é do tipo conta poupança ao passar o mes é somado a conta 1% e depois retira 3 reais de juros portanto a conta que inicialmente tinha 1k, foi para 1.010 por conta dos 1% e depois foi debitado 3 desse novo total

#Até aqui foi tudo normal utilizando herança basica, agora iremos utilizar o polimorfismo
print('-'*40)
contas = [conta16, conta17]
for conta in contas:
    conta.passa_o_mes() #Neste momento do código que acontece o duck typing, pois tudo aquilo que estiver na lista contas e se parecer com o tipo Conta, irá utilizar o método passa_o_mes(), por mais que os objetos qu estejam lá são contapoupanca ou contacorrente.
    print(conta)


print('-'*40)
print('-'*40)
# Array, (é bom evitar de usar o array, se precisarmos de trabalho numérico é aconselhavel utilizar a bibliotéca Numpy)
import array as arr
print(arr.array('d'), [1,3.5])
print('-'*40)
import numpy as np
numeros = np.array([1, 3.5])
print(numeros)
#Exemplo de utilização com o numpy
print('-'*40)
numeros += 4
print(numeros)