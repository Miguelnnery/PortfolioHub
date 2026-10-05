class Curso:

    def __init__(self, nome, preco, alunos, categoria):
        self.__nome = nome
        self.__preco = preco
        self.__alunos = alunos
        self.__categoria = categoria

    # Gets

    def get_nome(self):
        return self.__nome

    def get_preco(self):
        return self.__preco

    def get_alunos(self):
        return self.__alunos

    def get_categoria(self):
        return self.__categoria

    # Sets

    def set_nome(self, nome):
        self.__nome = nome

    def set_preco(self, preco):
        self.__preco = preco

    def set_alunos(self, alunos):
        self.__alunos = alunos

    def set_categoria(self, categoria):
        self.__categoria = categoria

    # Aumenta o preço do curso

    def aumentar_preco(self, valor):
        self.__preco = self.__preco + valor

    # Adiciona alunos ao curso

    def adicionar_alunos(self, quantidade):
        self.__alunos = self.__alunos + quantidade

    def mostrar(self):
        print("\nCurso:", self.__nome)
        print("Preço: R$", self.__preco)
        print("Alunos:", self.__alunos)
        print("Categoria:", self.__categoria)


def main():

    curso1 = Curso("Python", 80.0, 20, "Programação")
    curso2 = Curso("Excel", 60.0, 15, "Informática")
    curso3 = Curso("Marketing", 100.0, 10, "Marketing")

    print("Nome do curso 1:", curso1.get_nome())
    print("Preço do curso 1:", curso1.get_preco())
    print("Quantidade de alunos:", curso1.get_alunos())
    print("Categoria:", curso1.get_categoria())

    curso1.set_nome("Python Básico")
    curso1.set_preco(90.0)
    curso1.set_alunos(25)
    curso1.set_categoria("Programação")

    aumento = float(input("\nDigite o valor que deseja aumentar no preço: R$ "))

    curso1.aumentar_preco(aumento)
    curso2.aumentar_preco(aumento)
    curso3.aumentar_preco(aumento)

    curso1.adicionar_alunos(5)
    curso2.adicionar_alunos(3)
    curso3.adicionar_alunos(7)

    curso1.mostrar()
    curso2.mostrar()
    curso3.mostrar()


main()