class Conta:
    def __init__(self, nome, saldo, senha):
        self.nome = nome
        self.saldo = saldo
        self.senha = senha

    def para_dicionario(self):
        return {
            'nome': self.nome,
            'saldo': self.saldo,
            'senha': self.senha
        }
    def ver_saldo(self):
        print(f'seu saldo é: {self.saldo}')

    def depositar(self, valor):
        if valor <= 0:
            print('valor invalido/negativo')
            return
        self.saldo += valor
        print(f'seu novo saldo: {self.saldo}')

    def sacar(self, valor):
        if valor <= 0:
            print('valor invalido')
            return
        if valor > self.saldo:
            print(f'{valor} é valor maior do que saldo')
            return

        self.saldo -= valor
        print(f'seu novo saldo {self.saldo}')

    def transferir(self, valor, destinatario):
        if valor <= 0:
            print('valor invalido')
            return
        if valor > self.saldo:
            print('valor maior do que saldo')
            
        self.saldo -= valor
        destinatario.depositar(valor)
        print(f'Valor de {valor} transferido para {destinatario.nome.title()}.')


