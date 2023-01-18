class Programa:
    def __init__(self,nome,ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0
    

    @property
    def likes(self):
        return self._likes


    def dar_like(self):
        self._likes += 1

    @property
    def nome(self):
        return self._nome
    

    @nome.setter
    def nome(self, novo_nome):
        self._nome = novo_nome.title()


    def __str__(self):
        return f'Nome: {self._nome} - Likes: {self._likes}'


class Filme(Programa):
    def __init__(self,nome,ano,duracao):
        super().__init__(nome,ano)
        self.duracao = duracao
        
    def __str__(self):
        return f'Nome: {self._nome} - {self.duracao} min - Likes: {self._likes}'


class Series(Programa):
    def __init__(self,nome,ano,temporadas):
        super().__init__(nome,ano)
        self.temporadas = temporadas


    def __str__(self):
        return f'Nome: {self._nome} - {self.temporadas} temporadas - Likes: {self._likes}'


class Playlist():
    def __init__(self,nome,programas):
        self.nome = nome
        self._programas = programas
    
    #Torna a lista Playlist em uma lista iteravel
    def __getitem__(self,item):
        return self._programas[item]
        
    def __len__(self):
        return len(self._programas)

vingadores = Filme('vingadores - guerra infinita', 2018, 160)
atlanta = Series('atlanta', 2018, 2)
vingadores.dar_like()
vingadores.dar_like()
vingadores.dar_like()

atlanta.dar_like()
atlanta.dar_like()

listinha = [vingadores, atlanta]
minha_playlist = Playlist('fim de semana', listinha)
print(f'Tamanho da Playlist: {len(minha_playlist)}')
for programa in minha_playlist:
    print(programa)