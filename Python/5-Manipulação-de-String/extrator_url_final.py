import re
class ExtratorURL:
    def __init__(self,url):
        self.url = self.sanatiza_url(url)
        self.valida_url()

    def sanatiza_url(self,url):
        if type(url) == str:
            return url.strip()
        else:
            return ''

    def valida_url(self):
        if not self.url:
            raise ValueError('A URL está vazia!!')
        padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
        match = padrao_url.match(self.url)

        if not match:
            raise ValueError('A URL não é válida!!')

    def get_url_base(self):
        indice_interrogacao = self.url.find('?')
        url_base = self.url[:indice_interrogacao]
        return url_base

    def get_url_parametro(self):
        indice_interrogacao = self.url.find('?')
        url_parametro = self.url[indice_interrogacao + 1:]
        return url_parametro
    

    def get_valor_parametro(self, parametro_busca):
        indice_parametro = self.get_url_parametro().find(parametro_busca)

        indice_valor = (indice_parametro + len(parametro_busca) + 1) 

        indice_e_comercial = self.get_url_parametro().find('&',indice_valor)

        if indice_e_comercial == -1:
            valor = self.get_url_parametro()[indice_valor:]
        else:
            valor = self.get_url_parametro()[indice_valor:indice_e_comercial]
        return valor

    def __len__(self):
        return len(self.url)

    def __str__(self):
        return self.url + '\n' + 'URL Base: ' + self.get_url_base() + '\n' + 'Parâmetro: ' + self.get_url_parametro()
        
    def __eq__(self, other):
        return self.url == other.url

url = 'bytebank.com/cambio?quantidade=100&moedaOrigem=real&moedaDestino=dolar'
extrator_url = ExtratorURL(url)
extrator_url2 = ExtratorURL(url)
print(f'O tamanho da URL é {len(extrator_url)}')
#Métod dir pesquisa se tem ou não um método em um objeto
print('__len__' in dir(extrator_url)) #Inclusive da para usar o 'in' e ver se o objeto tem ou não aquele método

print(f'A URL1 é igual a URL2?: {extrator_url == extrator_url2}')

#Exercicios
#Modifique o nosso projeto, levando em conta o valor do dólar em real (por exemplo: DOLAR = 5.50), para, sabendo o valor do dólar em real (por exemplo: DOLAR = 5.50), ler da URL os 3 parâmetros (origem, destino e quantidade) e imprimir na tela o valor da conversão.
print("*"*40)
moeda_origem = extrator_url.get_valor_parametro('moedaOrigem')
quantidade = extrator_url.get_valor_parametro('quantidade')
moeda_destino = extrator_url.get_valor_parametro('moedaDestino')
total = float(quantidade) / 5.50
print(f'Como foi solicitado, a conversão de {quantidade} na moeda {moeda_origem} para a meoda {moeda_destino} resultou no saldo de {total:.2f}')
print("*"*40)