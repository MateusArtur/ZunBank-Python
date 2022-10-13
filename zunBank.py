import sys

#banco em python  Versão-1.0

print('____________________________________________________')
print('|0-------------- --- 001101011 ----------01011---01|')
print('|0|________       /0|   |001101010|   ___    \         |     |10|')
print('|001101011/   /00|   |0010101|   |010 |    \         |    |01|')
print('|00100110/  /100|   |001010 1|   |110 |    |\ \     |     |10|')
print('|1100011/   /0110|   |11001010|   |010|    |1\ \    |    |01|')
print('|001101/   /11001|   |_________|    |110|    |01\   \|    |00|')
print('|11010/   /00010 |_______________|00 |__|010\_____|01|')
print('|0110/   /_________________________________________ |')
print('|010|______________________________________________||')
print('|___________________________________________________|')
print(' O BANCO QUE TE TORNA ILIMITADO!')

senha1 = 123
saldo = 0
deposito = 0
saque = 0

nome = input('Qual é o seu nome? ')

verif = 0

while (verif < 3):
    senha = int(input('Digite sua senha: '))
    if (senha == senha1):
        break
    else:
        print('Senha incorreta, tente novamente!')
        verif = verif + 1
    if (verif == 3):
        print('Encerrando sistema.')
        sys.exit()

print('Bem vindo de volta', nome, '!')

while (True):
    print('*------------------------------------------------*')
    print('| 1-DEPÓSITO  | 2-SAQUE  | 3-SALDO | 4- Encerrar |')
    print('*------------------------------------------------*')

    operacao = int(input('Qual operação deseja realizar?'))

    if (operacao == 1):
        deposito = float(input('Qual o valor do depósito? '))
        saldo = saldo + deposito
        print('Depósito de R$', deposito, ' efetuado com sucesso, seu saldo atual é de R$%.2f' % saldo)
        print('*' * 80)
        print('\n' * 8)
    elif (operacao == 2):
        saque = float(input('Qual valor deseja sacar? '))
        saldo = saldo - saque
        if (saldo < 0):
            print('Saldo negativo, após três dias será acrescentado juros!')
            print('Saque de R$', saque, ' efetuado com sucesso, seu saldo atual é de R$%.2f' % saldo)
        else:
            print('Saque de R$', saque, ' efetuado com sucesso, seu saldo atual é de R$%.2f' % saldo)
        print('*' * 80)
        print('\n' * 8)
    elif (operacao == 3):
        print('Seu saldo atual é de R$%.2f' % saldo)
        print('*' * 80)
        print('\n' * 8)
    elif (operacao == 4):
        break
    else:
        print('Não conseguimos identificar o que deseja, por favor, verifique o número da operação e tente novamente. ')
        print('*' * 80)
        print('\n' * 8)

print('Esperamos ter ajudado, agradecemos por utilizar o ZUN BANK !')
