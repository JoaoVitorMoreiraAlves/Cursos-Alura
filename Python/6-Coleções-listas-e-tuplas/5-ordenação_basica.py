idades = [15,87,32,65,56,32,49,37]
print(sorted(idades))#Ordenando a lista
print('-'*40)
print(sorted(idades,reverse=True))#Ordenando a lista reversa, do maior para o menor
print('-'*40)
print(list(reversed(sorted(idades)))) #Também ordena a lista de forma reversa
print('-'*40)
#Entretando todos esses métodos não modifca a lista idades
print(idades)
print('-'*40)
#Ja o sort() modifica
idades.sort()
print(idades)