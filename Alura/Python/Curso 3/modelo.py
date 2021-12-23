class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title ()
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

    def imprime(self):
        print(f'Nome: {self._nome} - {self.ano} - {self._likes} Likes' )

class Filme(Programa):
    def __init__(self, nome, ano, duracao):
        super().__init__(nome,ano)
        self.duracao = duracao
    
    def __str__(self):
        return f'Nome: {self._nome} - {self.ano} - {self.duracao} Duracao - {self._likes} Likes' 
        
       
class Serie(Programa):
    def __init__(self, nome, ano, temporadas):
        super().__init__(nome,ano)
        self.temporadas = temporadas 
        self._likes = 0
    
    def __str__(self):
        return f'Nome: {self._nome} - {self.ano} - {self.temporadas} Temp - {self._likes} Likes' 

vingadores = Filme('vingadores - guerra infinita', 2018, 160)
vingadores.dar_like()
vingadores.dar_like()


atlanta = Serie('atlanta', 2018, 2)
atlanta.dar_like()
print(f'Nome: {atlanta.nome} - Ano: {atlanta.ano} - '
      f'Temporada: {atlanta.temporadas} - Like: {atlanta.likes}' )

filmes_e_series = [vingadores,atlanta]

for programa in filmes_e_series:
    print(programa)
    