class Pessoa:
    olhos = 2

    def __init__(self, *filhos, nome=None, idade=35):
        self.idade = idade
        self.nome = nome
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

if __name__ == '__main__':
    junior = Pessoa(nome='Junior')
    eugenio = Pessoa(junior, nome = 'Eugenio')
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
    Pessoa.olhos = 3
    del eugenio.olhos
    print(Pessoa.olhos)
    print(eugenio.olhos)
    print(junior.olhos)
    print(id(Pessoa.olhos), id(eugenio.olhos), id(junior.olhos))




