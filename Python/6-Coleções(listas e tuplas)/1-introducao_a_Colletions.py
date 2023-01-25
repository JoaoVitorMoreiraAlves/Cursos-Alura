idade1 = 39
idade2 = 30
idade3 = 27
idade4 = 18

print(idade1)
print(idade2)
print(idade3)
print(idade4)

idades = [20,39,18]
idades.extend([27,19])
print(idades)

idades_no_ano_que_vem = [(idade+1) for idade in idades if idade > 21]
print(idades_no_ano_que_vem)


def faz_processamento_da_visualizacao(lista):
    print(len(lista))

print(faz_processamento_da_visualizacao(idades))