import datetime

def calcular_idade(ano_nascimento):
    ano_atual = datetime.date.today().year
    idade = ano_atual - ano_nascimento
    return idade

def main():
    while True:
        nome = input("Digite seu nome completo: ")
        try:
            ano_nascimento = int(input("Digite seu ano de nascimento (1922-2022): "))
            if 1922 <= ano_nascimento <= 2022:
                break
            else:
                print("Ano de nascimento fora do intervalo permitido. Tente novamente.")
        except ValueError:
            print("Valor inválido. Por favor, insira um ano válido.")

    idade = calcular_idade(ano_nascimento)
    print(f"Olá, {nome}! Você completou ou completará {idade} anos no ano de 2023.")

if __name__ == "__main__":
    main()
