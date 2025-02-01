while True:
    num1 = float(input("Digite o primeiro numero: "))
    num2 = float(input("Digite o segundo número: "))

    operacao = input("Qual operação matematica deseja fazer? ").upper()
    if operacao == "SOMA" or operacao == "+":
        print(num1 + num2)
    elif operacao == "SUBTRACAO" or operacao == "-":
        print(num1 - num2)
    elif operacao == "MULTIPLICACAO"  or operacao == "*" or operacao == "X":
        print(num1 * num2)
    elif operacao == "DIVISAO" or operacao == "/":
        print(num1 / num2)
    else:
        print("Operação inválida")

    continuar = input("Deseja fazer outro cálculo? (Sim/Não): ").strip().upper()
    if continuar == "NÃO" or "N":
        print("Encerrando o programa...")
        break
