class Funcionario:
    def __init__(self,nome):
        self.nome = nome

    def registra_horas(self, horas):
        print('Horas registradas...')

    def mostrar_tarefas(self):
        print('Fez muita coisa...')

class Caelum(Funcionario):
    def mostrar_tarefas(self):
        print('Fez muita coisa, Caelumer')

    def busca_cursos_do_mes(self, mes=None):
        print(f'Mostrando cursos - {mes}' if mes else 'Mostrando cursos desse mês')

class Alura(Funcionario):
    def mostrar_tarefas(self):
        print('Fez muita coisa, Alurete!')

    def busca_perguntas_sem_resposta(self):
        print('Mostrando perguntas não respondidas do fórum')


class Hipster:
    def __str__(self):
        return f'Hipster, {self.nome}'

class Junior(Alura):
    pass

class Pleno(Alura, Caelum):
    pass

class Senior(Alura, Caelum, Hipster):
    pass

print('Jose:') 
jose = Junior('jose')
jose.mostrar_tarefas()

print('*'*30)
print('Pedro')
pedro = Pleno('Pedro')
pedro.mostrar_tarefas()

#A seleção da super classe onde sera buscado o método é feita através do MRO (Method Resolution Order) basicamente quando chamamos o pedro.mostrar_tarefas() o algoritmo ira fazer a seguinte busca pelo método:
# Pleno > Alura > Funcionario > Caelum > Funcionario

#Entretando se nos fizer o método mostrar_tarefas da class Alura ser um comentario a ordem do MRO muda sendo para a seguinte busca:
# Pleno > Alura > Caelum > Funcionario, pois na parte de verificar a duplicidade o algoritmo procura uma 'good head' (uma boa cabeça), como o primeiro funcionario da ordem não é uma boa cabeça já que Caelum tb herda da super classe Funcionario, o algoritmo remove ele tornando Caelum 'uma boa cabeça'


print('*'*30)
print('Joao')
joao = Senior('Joao')
print(joao)