def somar(a, b):
    return a + b

def subtrair(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "Erro: divisão por zero"
    return a / b

def menu():
    print("""
=== CALCULADORA ===
+  Soma
-  Subtração
*  Multiplicação
/  Divisão
0  Sair
""")

historico = []

while True:
    menu()
    operacao = input("Escolha a operação: ")

    if operacao == "0":
        print("Encerrando...")
        break

    if operacao in ["+", "-", "*", "/"]:
        try:
            n1 = float(input("Primeiro número: "))
            n2 = float(input("Segundo número: "))
        except:
            print("Entrada inválida!")
            continue

        if operacao == "+":
            resultado = somar(n1, n2)
        elif operacao == "-":
            resultado = subtrair(n1, n2)
        elif operacao == "*":
            resultado = multiplicar(n1, n2)
        elif operacao == "/":
            resultado = dividir(n1, n2)

        print(f"Resultado: {resultado}")
        historico.append(f"{n1} {operacao} {n2} = {resultado}")

    elif operacao == "h":
        print("\nHistórico:")
        for item in historico:
            print(item)

    else:
        print("Operação inválida!")