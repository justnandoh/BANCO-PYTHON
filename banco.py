from conta import Conta
import json
contas = {}


with open ('dados.json') as arquivo:
    dados = json.load(arquivo)
for nome, info in dados.items():
    contas[nome] = Conta(
        info['nome'],
        info['saldo'],
        info['senha'],
    )

def salvar_dados():
    dados = {}
    for nome, conta in contas.items():
        dados[nome] = conta.para_dicionario()
    with open('dados.json', 'w') as arquivo:
        json.dump(dados, arquivo)

def start():
    opcoes = {'1': criar_conta,
              '2': login,
                }
    
    while True:
        escolha = input('Bem Vindo! Digite 1 para criar conta, 2 para logar ou F para encerrar:\n').strip().lower()
        if escolha == 'f':
            print('Encerrando...')
            break
        if escolha not in opcoes:
            print('Opção inválida.')
            continue
        opcoes[escolha]()


def criar_conta():
    while True:
        nome = input('Digite seu nome para criar a conta ou F para voltar: ').strip().lower()
        if nome in contas:
            print('Conta já existente.')
            continue
        if nome == 'f':
            break
        if nome == '':
            print('Nome inválido.')
            continue
        if not nome.replace(' ', '').isalpha():
            print('O nome não pode possuir símbolos ou números.')
            continue
        senha = input('Digite a senha para criar a conta ou F para voltar: ').strip().lower()
        if senha == 'f':
            break
        if senha == '':
            print('Senha inválida.')
            continue
        contas[nome] = Conta(nome, 0, senha)
        salvar_dados()
        print('Conta criada.')
        
        login()
        break

def login():
    while True:
        nome = input('Digite seu nome para logar ou F para voltar: ').strip().lower()
        if nome == 'f':
            break
        if nome not in contas:
            print('Nome inválido.')
            continue
        while True:
            senha = input('Digite sua senha para logar ou F para voltar: ').strip().lower()
            if senha == 'f':
                break
            if senha != contas[nome].senha:
                print('Senha incorreta.')
                continue
            print(f'Login efetuado em {contas[nome].nome.title()} com sucesso. Bem vindo!')
            conta = contas[nome]
            menu_conta(conta)
            break

def validar_senha(conta):
    senha = input('Digite sua senha: ').strip().lower()
    if senha != conta.senha:
        print('Senha inválida.')
        return False
    return True

def pedir_valor(mensagem):
    while True:
        try:
            valor = float(input(mensagem))
            if valor <= 0:
                print('Valor inválido.')
                continue
            return valor
        except:
            print('Digite um número válido.')

def menu_conta(conta):
    while True:
        print('\nBANCO DO JUSTNANDOH\n' \
        '1: Ver saldo\n' \
        '2: Depositar\n' \
        '3: Sacar\n' \
        '4: Transferir\n' \
        '5: Logout\n' \
        '')

        escolha = input('').strip().lower()

        if escolha == '1':
            conta.ver_saldo()

        elif escolha == '2':
            valor = pedir_valor('Valor a depositar ou F para voltar: ')
            if valor == 'f':
                break
            conta.depositar(valor)
            salvar_dados()

        elif escolha == '3':
            while True:
                if validar_senha(conta):
                    break   
            valor = pedir_valor('Valor a sacar ou F para voltar: ')
            conta.sacar(valor)
            salvar_dados()

        elif escolha == '4':
            while True:
                if validar_senha(conta):
                    break
            while True:
                destinatario = input('À quem deseja enviar ou F para voltar: ').strip().lower()
                if destinatario == 'f':
                    break
                if destinatario in contas:
                    valor = pedir_valor('Valor a enviar: ')
                    conta.transferir(valor, contas[destinatario])
                    salvar_dados()
                    break
                
                print('Destinatário inválido.')
                continue
        elif escolha == '5':
            print('Logout realizado.')
            break
        
        else:
            print('Opção inválida.')

start()