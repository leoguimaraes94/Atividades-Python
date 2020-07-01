#Projeto Integrador: exercício 04


resposta = "sim" 

while resposta == "sim" or resposta == "s" or resposta == "S":
    print("Digite um número: ")
    num1 = int(input())
    print("Digite a operação a ser realizada\n(+) Soma (-) Subtração (*) Multiplicação (/) Divisão: ")
    op = input()
    print("Digite o segundo valor: ")
    num2 = int(input())
    if op == "+":
        soma = num1 + num2
        print("Sua operação é soma.")
        print(f"Seu resultado é: {soma}")
    if op == "-":
        soma = num1 - num2
        print("Sua operação é subtração.")
        print(f"Seu resultado é: {soma}")
    if op == "*":
        soma = num1 * num2
        print("Sua operação é multiplicação.")
        print(f"Seu resultado é: {soma}")
    if op == "/":
        soma = num1 / num2
        print("Sua operação é divisão.")
        print(f"Seu resultado é: {soma}")
    resposta = input("Deseja realizar outra operação? [sim/não]: ")
while resposta == "não" or resposta == 'n' or resposta == 'N':
    print("FIM!")
    break

