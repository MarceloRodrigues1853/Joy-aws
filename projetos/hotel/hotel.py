# Usando o laço for
for numero in range(1, 21):
    if numero != 13:
        print(numero, end=' ')

print("\n")

# Usando o laço while
numero = 1
while numero <= 20:
    if numero != 13:
        print(numero, end=' ')
    numero += 1

print("\n")

# Usando um loop "do-while" (simulado)
numero = 1
while True:
    if numero != 13:
        print(numero, end=' ')
    numero += 1
    if numero > 20:
        break

print("\n")

# Imprimindo em ordem decrescente
for numero in range(20, 0, -1):
    if numero != 13:
        print(numero, end=' ')
