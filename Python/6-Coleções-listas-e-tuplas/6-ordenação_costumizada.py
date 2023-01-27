from operator import attrgetter

nomes = ['Guilherme', 'Danieal', 'Paulo']
print(sorted(nomes))
nomes = ['guilherme', 'Danieal', 'Paulo'] #Se a letra for minuscula ele modifica a ordem
print(sorted(nomes))
print('-'*40)
class ContaSalario:
    def __init__(self,codigo):
        self._codigo = codigo
        self._saldo = 0
    
    def __eq__(self, outro):
        if type(outro) != ContaSalario:
            return False
        return self._codigo == outro._codigo and self._saldo == outro._saldo

    def __lt__(self,outro):
        return self._saldo < outro._saldo

    def deposita(self,valor):
        self._saldo += valor
    
    def __str__(self):
        return f'>>>Código {self._codigo} Saldo {self._saldo}<<<'


conta_do_guilherme = ContaSalario(17)
conta_do_guilherme.deposita(500)

conta_da_daniela = ContaSalario(3)
conta_da_daniela.deposita(1000)

conta_do_paulo = ContaSalario(133)
conta_do_paulo.deposita(510)

contas = [conta_do_guilherme, conta_da_daniela, conta_do_paulo]
#for conta in contas:
#    print(sorted(conta)) não é possível

def extrai_saldo(conta):
    return conta._saldo #Forma errada de manipular o atributo, pois ele não permite o encapsulamento, portanto não iremos utilizar


for conta in sorted(contas,key= attrgetter('_saldo')): #Esse metodo para ordenar também é ruim pq temos q passar o '_saldo' q seria algo encapsulado, para isso podemos usar o __lt__
    print(conta)#Ordenou por ordem crescente do valor
print('-'*40)

print(conta_do_guilherme > conta_da_daniela)
print('-'*40)

for conta in sorted(contas):#Agora eu tenho a ordenação perfeita utilizando um método da classe que me garante o encapsulamento
    print(conta)