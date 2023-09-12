#Funcões

#def= palavra reservada para declara uma função

#escrever_multiplicação= nome que damos à fução

#num1,num2 = parametros

#return = palavra reservada para retornar o resultado da função

#str() = usa o "str" para contatenar o parametro em "string" ex str(num1)= fica "5" em string

def escrever_multiplicacao(num1,num2):
    multiplicacao = num1 * num2
    resultado = str(num1) + " x " + str(num2) + " = " + str(multiplicacao)
    return resultado

resposta = escrever_multiplicacao(5, 8)
print(resposta)