#Projeto Integrador: exercício 12
#Nomes: Luiz Daniel (RA:4115066), Vinicius Moreira (RA:4054172), Leonardo Mendes (RA:4136381)


while True:
    print('='*52)
    operacao = input('Qual operação (+,-,*,/100,/,%,**) você quer fazer?\nCaso não digite \'S\' para sair: ')
    print('='*52)
    if operacao == 'S' or operacao == "s":
        print('Programa Finalizado!!!!')
        break
    elif operacao == '+' or operacao == '-' or operacao == '*' or operacao == '/' or operacao == '%' or operacao == '/100' or operacao == '**':
        print('Uma variável é um nome que se refere a um valor.')
        num1 = int(input('Digite o primeiro numero: '))
        print('A finalidade da função int() é apresentar números sem casa decimais.')
        num2 = float(input('Digite o segundo numero: '))
        print("A finalidade da função float() é apresentar casa decimais.")

    else:
        print('Operacao invalida')

    if operacao == '+':
        total = num1 + num2
        print('Resultado da soma {} + {} é: {}'.format(num1, num2, total))
        print()
        print()
    elif operacao == '-':
        total = num1 - num2
        print('Resultado da subtração {} - {} é: {}'.format(num1, num2, total))
        print()
        print()
    elif operacao == '*':
        total = num1 * num2
        print('Resultado da multiplicação {} * {}  é: {}'.format(num1, num2, total))
        print()
        print()
    elif operacao == '/':
        total = num1 / num2
        print('Resultado da divisão {} / {}  é: {}'.format(num1, num2, total))
        print()
        print()
    elif operacao == '/100':
        total = num1 * ((num2/100))
        print('Resultado da porcentagem {} * {} é: {}'.format(num1, num2, total))
        print()
        print()
    elif operacao == '%':
        total = num1 % num2
        print('Resultado do resto {} % {} é: {}'.format(num1, num2, total))
        print()
        print()
    elif operacao == '**':
        total = num1 ** num2
        print('Resultado do exponenciação {} ** {} é: {}'.format(num1, num2, total))
        print()
        print()


    



