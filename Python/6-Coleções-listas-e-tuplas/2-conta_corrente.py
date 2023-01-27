class ContaCorrente:
    def __init__(self,codigo):
        self.codigo = codigo
        self.saldo = 0
    
    def deposita(self,valor):
        self.saldo += valor
    
    def __str__(self):
        return (f'Código {self.codigo} saldo {self.saldo}')


conta_do_joao = ContaCorrente(20)
print(conta_do_joao)
print('-'*40)
conta_da_dani = ContaCorrente(47685)
conta_da_dani.deposita(1000)
print(conta_da_dani)
print('-'*40)
contas = [conta_do_joao, conta_da_dani, conta_do_joao] #Colocar objetos numa lista não o INSTANCIA, ele somente armaze na posição da lista o ponteiro do objeto

#Então por exemplo se eu adiciono 100 de valor no objeto conta_do_joao
conta_do_joao.deposita(100)
#Esse valor vai ser expelhado também nos objetos da posição 0 e 2 da lista contas
print('Print da conta do joao', contas[0], contas[2])
print('-'*40)
#Também é possível printar os objetos da lista através de um for
for conta in contas:
    print(conta)

#Caso eu tente printar a lista diretamente ira sair somente os valores que representam o local da memoria que está o objeto
print('-'*40)
print('Local da memoria dos objetos: ', contas)
print('-'*40)


def deposita_para_todas(contas):
    for conta in contas:
        conta.deposita(100)

contas = [conta_do_joao, conta_da_dani]
print(contas[0], contas[1])
deposita_para_todas(contas)
print(contas[0], contas[1])


joao = ('João Vitor', 19, 2003) #Tupla
daniela = ('Daniela', 31, 1987)
#joao.append(5) #Da erro pois tuplas são imutaveis
print('-'*40)
usuarios = [joao, daniela] #Colocando tuplas dentro de lista
print(usuarios)
print('-'*40)
usuarios.append(('Paulo', 39,1979))
print(usuarios)
print('-'*40)

conta_do_joao = ContaCorrente(15)
conta_do_joao.deposita(500)
conta_da_dani = ContaCorrente(23032)
conta_da_dani.deposita(1000)
contas = (conta_do_joao, conta_da_dani) #Colocando lista dentro de tupla
for conta in contas:
    print(conta)
print('-'*40)
#contas.append(3847234234) #não é possível pois a tupla é imutavel eu tenho que utilizar da seguinte forma

contas[0].deposita(300) 
#Ele vai no objeto da posição 0 e fazer o deposito, nesse caso é possível realizar, pois o objeto é mutável
for conta in contas:
    print(conta)
print('-'*40)