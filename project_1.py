from datetime import datetime
menu = """

[d] Depositar
[s] Sacar
[e] Extrato
[q] Sair

=> """

saldo = 0
limite = 500
numero_saques = 0
limite_saques = 3
contador = 0
extrato = []

while True:
    opcao = input(menu)

    if opcao == 'd':
        valor_deposito = float(input("Digite o valor de depósito: "))
        if valor_deposito < 0:
            print("Valor inválido! Por favor, digite um valor positivo!")
            valor_deposito = float(input("Digite o valor de depósito: "))
        else:
            print(f"O seu depósito no valor de {valor_deposito} foi realizado com sucesso")
            saldo += valor_deposito
        data_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        extrato.append({"data_hora": data_hora, "valor": valor_deposito})

    elif opcao == 'e':
        print("Extrato")
        if len(extrato) == 0:
            print("Não há movimentações em seu extrato.")
        else:
            for item in extrato:
                print(f"Data e hora: {item['data_hora']}, Valor: R$ {item['valor']}")
            print(f"\nSaldo atual: R$ {saldo}")

    elif opcao == 's':
        if contador >= limite_saques:
            print("Você chegou ao limite de saques por hoje. Volte novamente amanhã!")
        else:
            saque = float(input("Digite o valor para saque: "))

            if saque > saldo:
                print("Saldo insuficiente!")
            elif saque > 500:
                print("O limite máximo para saque é de R$ 500")
            else:
                saldo -= saque
                contador += 1
                print(f"Seu saque de R$ {saque} foi realizado com sucesso!")


    elif opcao == 'q':
        break
    else:
        print("Operação inválida, por favor tente outra opção!")