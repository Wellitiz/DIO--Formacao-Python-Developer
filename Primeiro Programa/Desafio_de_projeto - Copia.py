# Operação de depósito
#Deve ser possível depositar valores positivos para a minha conta bancária.

# Operação de saque
# O sistema deve permitir realizar 3 saques diários com limite máximo de R$ 500,00 por saque. Caso o usuário não tenha saldo em conta, o sistema deve exibir uma mensagem informando que não será possível sacar o dinheiro por falta de saldo. Todos os saques devem ser armazenados em uma variável e exibidos na operação de extrato.

# Operação de extrato
# Essa operação deve listar todos os depósitos e saques realizados na conta. No fim da listagem deve ser exibido o saldo atual da conta. Se o extrato estiver em branco, exibir a mensagem: Não foram realizadas movimentações.
# Os valores devem ser exibidos utilizando o formato R$ xxx.xx, exemplo:
# 1500.45 = R$ 1500.45

nome = "Wellington"
saldo = 500
limite = 500
limiteSaque = 3
contadorSaque = 0
extrato = []

#Mensagem de apresentação para o usuario
mensagem = f""" 
================================================
            Bem Vindo {nome}

    Digite uma opção para fazer uma operação:
    [1] Depósitar
    [2] Sacar
    [3] Extrato
    [0] Sair
================================================
"""
#Operaao definica diferente de 0 para iniciar o loop do programa
operacao = 1
while int(operacao) != 0:
    operacao = input (mensagem)
    if int(operacao) == 1: #Entra na função de deposito
        valor_deposito = -1
        while valor_deposito < 0:
            valor_deposito = int(input('Qual o valor do Depósito? '))
            if valor_deposito < 0:
                print("Por favor, insira um valor positivo.")
        saldo += valor_deposito
        extrato.append(f'Deposito de R${valor_deposito:.2f}') #Adiciona o valor do Extrato
        print("Depósito relizado com Sucesso")
    elif int(operacao) == 2:
        if contadorSaque >= limiteSaque:
            print("Você atingiu o limite de saques.")
            continue
        valor_saque = -1
        while valor_saque < 0 or valor_saque > limite or valor_saque > saldo: #Caso o valor de Saque seja maior que o saldo ou o limite apresenta esta mensagem.
            valor_saque = int(input('Qual o valor para saque?' ))
            if valor_saque < 0:
                print("Por favor, insira um valor positivo.")
            elif valor_saque > limite:
                print("Valor maior que o limite permitido.")
            elif valor_saque > saldo:
                print("Não há limite disponível em conta.")
        saldo -= valor_saque
        extrato.append(f'Saque de -R${valor_saque:.2f}') #Adiciona o valor do Extrato
        print(saldo)
        contadorSaque += 1
    elif int(operacao) == 3:
        if not extrato:
            print("Não a extratos a serem exibidos")
            print(f'Seu saldo atual é de R${saldo}')
        else:
            for i, extrato in enumerate(extrato):
                print(f'Extrato {i+1}: {extrato}')
                print(f'Seu saldo atual é de R${saldo}')
    elif int(operacao) == 0:
        print("Obrigado por ser nosso cliente")
