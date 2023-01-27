from operator import attrgetter
from functools import total_ordering
@total_ordering
class ContaSalario:
    def __init__(self,codigo):
        self._codigo = codigo
        self._saldo = 0
    
    def __eq__(self, outro):
        if type(outro) != ContaSalario:
            return False
        return self._codigo == outro._codigo and self._saldo == outro._saldo

    def __lt__(self,outro):
        if self._saldo != outro._saldo:
            return self._saldo < outro._saldo
        return self._codigo < outro._codigo

    def deposita(self,valor):
        self._saldo += valor
    
    def __str__(self):
        return f'>>>Código {self._codigo} Saldo {self._saldo}<<<'


conta_do_guilherme = ContaSalario(1700)
conta_do_guilherme.deposita(500)

conta_da_daniela = ContaSalario(3)
conta_da_daniela.deposita(1000)

conta_do_paulo = ContaSalario(133)
conta_do_paulo.deposita(500)

contas = [conta_do_guilherme, conta_da_daniela, conta_do_paulo]
#Queremos ordernar pela conta do paulo, dps do guilherme e dps da daniela

for conta in sorted(contas, key=attrgetter('_saldo','_codigo')): #Ordenando pelo saldo, e caso o saldo seja igual, ele ordena pelo código
    print(conta)
print('-'*40)
for conta in sorted(contas): #Ele ordena de forma correta também pois na função __lt__ nos fizemos uma mudança para caso o valor seja igual, ele ira comparar o código
    print(conta)
print('-'*40)
#print(conta_do_guilherme <= conta_da_daniela) #Da erro pois o '<=' é diferente do '< ou >', caso quiser colocar a igual na comparação, teremos q implementar outras funções, e para isso usando o total_ordering

print(conta_do_guilherme >= conta_da_daniela) #Agora da certo, pois implementamos o total_ordering