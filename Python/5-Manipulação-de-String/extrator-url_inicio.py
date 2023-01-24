# url = 'https://bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar'

url = ' '
#Sanitização da URL
url = url.strip()



#Validação da URL
if url == '':
    raise ValueError('A URL está vazia!!')
#Separa a base e os parâmetros
indice_interrogacao = url.find('?') #Vê em qual posição encontra a interrogação
url_base = url[:indice_interrogacao]# Separa a base do inicio da url até a interrogação

url_parametro = url[indice_interrogacao+1:]# Separa o parametro depois do ponto de interrogação até o final da url
print(url_parametro)#printa o parametro


#Busca o valor de um parâmetro
parametro_busca = 'quantidade'
indice_parametro = url_parametro.find(parametro_busca)#Procura em qual posição dos parametro está a palavra 'quantidade'

indice_valor = indice_parametro + len(parametro_busca) + 1 #Pega a posição em termina a palavra 'quatidade' + 1 ou seja ele vai pular o sinal de igualdade

indice_e_comercial = url_parametro.find('&',indice_valor) #Procura em qual posição está o E comercial nos parametros a partir da posição indice_valor que ira indicar o primeiro valor do primeiro parametro

if indice_e_comercial == -1: #Caso não seja encontrado o E comercial ele entra no IF printando o indice_valor que representa a posição que inicial o valor do primeiro parametro
    valor = url_parametro[indice_valor:]
else:#Caso exista o E comercial ele vai printar da posição indice_valor até o E comercial
    valor = url_parametro[indice_valor:indice_e_comercial]
print(valor)