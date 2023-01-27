class ContaSalario:
    def __init__(self,codigo):
        self._codigo = codigo
        self._saldo = 0
    
    def __eq__(self, outro):
        if type(outro) != ContaSalario:
            return False
        return self._codigo == outro._codigo and self._saldo == outro._saldo

    def deposita(self,valor):
        self._saldo += valor
    
    def __str__(self):
        return f'>>>Código {self._codigo} Saldo {self._saldo}<<<'

conta1 = ContaSalario(37)
print(conta1)

print('-'*40)
conta2 = ContaSalario(37)
print(conta2)

print('-'*40)

print(conta1 == conta2) #De Inicio ele retorna falso pois ele vai comparar o valor na memoria dos dois objetos e não se ambos são do tipo ContaSalario, mas se usarmos o método __eq__, e definirmos como ver a igualdade da para deixar verdadeiro pois ele vai comparar o código de cada conta
print('-'*40)

contas = [conta1]
print(conta1 in contas) 
print('-'*40)
print(conta2 in contas)
print('-'*40)

#Builtins como enumerated, range e desempacotamento automatico de tuplas

idades = [15,87,32,65,56,32,49,37]
for num in range(0,len(idades)):
    print(f'Idade {idades[num]} na posição {num}')
#Posso fazer com enumerated que é melhor
print('-'*40)
for indice,valor in enumerate(idades,0):
    print(f'Indice: {indice} X Valor: {valor}')
print('-'*40)

usuarios = [
    ('Guilherme',37,1981),
    ('Danieal',31,1987),
    ('Joao',19,2003)]

for nome,idade,nascimento in usuarios: #Desempacotando
    print(nome)
print('-'*40)
for nome, _, _ in usuarios: #Desempacotando só que agora possui os anderlines, O "_" siginifca que estou ignorando a idade e a data de nascimento
    print(nome)