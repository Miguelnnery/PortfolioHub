class Produto:

    def __init__(self, nome, codigo, preco_compra, quantidade):
        self.nome = nome
        self.codigo = codigo
        self.preco_compra = preco_compra
        self.quantidade = quantidade

    def get_nome(self):
        return self.nome

    def get_codigo(self):
        return self.codigo

    def get_preco_compra(self):
        return self.preco_compra

    def get_quantidade(self):
        return self.quantidade


    def set_nome(self, nome):
        self.nome = nome

    def set_codigo(self, codigo):
        self.codigo = codigo

    def set_preco_compra(self, preco):
        if preco >= 0:
            self.preco_compra = preco
            print("Preço alterado com sucesso!")
        else:
            print("Erro: o preço de compra não pode ser negativo.")

    def set_quantidade(self, quantidade):
        if quantidade >= 0:
            self.quantidade = quantidade
        else:
            print("Erro: a quantidade não pode ser negativa.")

    def mostra_dados(self):
        print("Nome:", self.nome)
        print("Código:", self.codigo)
        print("Preço de compra:", self.preco_compra)
        print("Quantidade:", self.quantidade)
        print("-------------------------")


    def aumentar_preco(self, aumento):
        self.preco_compra = self.preco_compra + aumento


    def vender_produto(self, quantidade_vendida):
        if quantidade_vendida <= self.quantidade:
            self.quantidade = self.quantidade - quantidade_vendida
            print("Venda realizada com sucesso!")
        else:
            print("Erro: quantidade insuficiente em estoque.")



print("===== SISTEMA DE PRODUTOS =====")

produto1 = Produto("Teclado", 101, 80.00, 10)
produto2 = Produto("Mouse", 102, 45.50, 20)
produto3 = Produto("Monitor", 103, 650.00, 5)
produto4 = Produto("Headset", 104, 120.00, 8)



produto1.mostra_dados()
produto2.mostra_dados()
produto3.mostra_dados()
produto4.mostra_dados()


print("Nome do produto 1:", produto1.get_nome())
print("Código do produto 1:", produto1.get_codigo())
print("Preço do produto 1:", produto1.get_preco_compra())
print("Quantidade do produto 1:", produto1.get_quantidade())


produto1.set_nome("Teclado Gamer")
produto1.set_codigo(201)
produto1.set_quantidade(15)

print("\nDados do produto 1 depois das alterações:")
produto1.mostra_dados()



produto1.set_preco_compra(90.00)


produto1.set_preco_compra(-50.00)



aumento = float(input("\nDigite o valor do aumento no preço do produto 1: "))

produto1.aumentar_preco(aumento)

print("\nPreço depois do aumento:")
print(produto1.get_preco_compra())



print("\nVendendo 3 unidades do produto 1:")
produto1.vender_produto(3)

print("Quantidade atual:", produto1.get_quantidade())



print("\nDADOS FINAIS ")

produto1.mostra_dados()
produto2.mostra_dados()
produto3.mostra_dados()
produto4.mostra_dados()