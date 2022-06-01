class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá, meu nome é {self.nome}'

    @staticmethod
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos{cls.olhos}'

class Homem(Pessoa):
    def cumprimentar(self):
        cumprimentar_da_classe = super().cumprimentar()
        return f'{cumprimentar_da_classe}. Aperto de mão'

class Mutante(Pessoa):
    olhos = 3
    pass

if __name__ == '__main__':
    junior = Mutante(nome='Junior')
    eugenio = Homem(junior, nome = 'Eugenio')
    print(Pessoa.cumprimentar(eugenio))
    print(id(eugenio))
    print(eugenio.cumprimentar())
    print(eugenio.nome)
    print(eugenio.idade)
    for filho in eugenio.filhos:
        print(filho.nome)

    eugenio.sobrenome = 'Silva'
    del eugenio.filhos
    print(eugenio.__dict__)
    print(junior.__dict__)
    eugenio.olhos = 1
    del eugenio.olhos
    print(Pessoa.olhos)
    print(eugenio.olhos)
    print(junior.olhos)
    print(id(Pessoa.olhos), id(eugenio.olhos), id(junior.olhos))
    print(Pessoa.metodo_estatico(), eugenio.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe(), eugenio.nome_e_atributos_de_classe())
    pessoa = Pessoa('Anonimo')
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Homem))
    print(isinstance(junior, Pessoa))
    print(isinstance(junior, Homem))
    print(junior.olhos)
    print(junior.cumprimentar())
    print(eugenio.cumprimentar())




