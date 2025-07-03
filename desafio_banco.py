menu = '''
--------------- MENU ----------------
    Olá, selecione a opção desejada
    1 - Sacar
    2 - Depositar
    3 - Extrato
    4 - Sair
-------------------------------------
'''

conta_corrente = 0
LIMITE = 500
quantidade_saques = 0
extrato = ""
LIMITE_SAQUES = 3
sacar = 0

while True:

    opcao = int(input(menu))

    if opcao == 1:
            sacar = int(input("Digite o valor que deseja sacar: "))
            if quantidade_saques <= LIMITE_SAQUES:
                if sacar <= LIMITE:
                    if sacar <= conta_corrente:
                        print("Retire o seu dinheiro")
                        conta_corrente -= sacar
                        quantidade_saques += 1
                    else:
                        print("Seu saldo é insuficiente para este saque")
                else:
                    print("O valor indicado está acima do limite permitido por saque")
            else:
                print("Você atingiu o limite máximo de saques diários")

    elif opcao == 2:
            deposito = int(input("Digite o valor que deseja depositar: "))
            conta_corrente += deposito
            print("Depósito realizado com sucesso!")

    elif opcao == 3:
        print("Seu extrato: \n")
        print(f"Depósito: R$ {deposito}")
        print(f"\nSaque: R$ {sacar}")
        print(f"\nSaldo: R$ {conta_corrente}")

    elif opcao == 4:
        break
print("Obrigado por usar nosso sistema!")

