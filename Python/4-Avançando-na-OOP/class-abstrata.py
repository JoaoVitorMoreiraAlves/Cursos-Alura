#Como criar uma class abstrata para que as susas sub-classes sejam obrigadas a herdar seus métodos

#Class abstrata
from abc import ABCMeta, abstractmethod 
class Programa(metaclass = ABCMeta): 
    @abstractmethod 
    def __str__(self): 
        pass


#Jeito Errado
class Filme(Programa):
    def __init__(self,nome):
        self.nome = nome


#Jeito Certo
class Series(Programa):
    def __init__(self,nome):
        self.nome = nome
    
    def __str__(self):
        return self.nome


vikings = Series('Vikings')
print(vikings)

vingadores = Filme('Vingadores')
print(vingadores)