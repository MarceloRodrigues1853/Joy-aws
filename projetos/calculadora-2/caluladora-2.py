def soma(x, y):
    return x + y

def subtracao(x, y):
    return x - y

def multiplicacao(x, y):
    return x * y

def divisao(x, y):
    if y == 0:
        return "Erro! Divisão por zero."
    return x / y

while True:
    print("Escolha a operação:")
    print("1: Soma")
    print("2: Subtração")
    print("3: Multiplicação")
    print("4: Divisão")
    print("0: Sair")

    opcao = input("Digite o número para a operação correspondente: ")

    if opcao == '0':
        break
    elif opcao not in ('1', '2', '3', '4'):
        print("Essa opção não existe")
        continue

    num1 = float(input("Digite o primeiro valor: "))
    num2 = float(input("Digite o segundo valor: "))

    if opcao == '1':
        resultado = soma(num1, num2)
        print("Resultado:", resultado)
    elif opcao == '2':
        resultado = subtracao(num1, num2)
        print("Resultado:", resultado)
    elif opcao == '3':
        resultado = multiplicacao(num1, num2)
        print("Resultado:", resultado)
    elif opcao == '4':
        resultado = divisao(num1, num2)
        print("Resultado:", resultado)
