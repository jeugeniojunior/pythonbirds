class Pessoa:
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


