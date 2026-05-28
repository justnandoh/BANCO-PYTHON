class Conta:
    def __init__(self, nome, saldo, senha, historico=None):
        self.nome = nome
        self.saldo = saldo
        self.senha = senha
        self.historico = historico or []

    def para_dicionario(self):
        return {
            'nome': self.nome,
            'saldo': self.saldo,
            'senha': self.senha,
            'historico': self.historico,
        }
    def ver_saldo(self):
        print(f'================\nSaldo: R${self.saldo:.2f}\n================')

    def depositar(self, valor):
        if valor <= 0:
            print('Valor inválido.')
            return
        
        self.saldo += valor
        print(f'Valor depositado! Novo saldo: {self.saldo:.2f}')
        self.historico.append(f'Deposito: +{valor:g}')

    def sacar(self, valor):
        if valor <= 0:
            print('Valor inválido.')
            return
        if valor > self.saldo:
            print(f'Saldo insuficiente para saque.')
            return
        
        self.saldo -= valor
        print(f'Valor sacado! Novo saldo: {self.saldo:.2f}.')
        self.historico.append(f'Saque: -{valor:g}')

    def transferir(self, valor, destinatario):
        if valor <= 0:
            print('Valor inválido.')
            return
        if valor > self.saldo:
            print(f'Saldo insuficiente para transferência.')
            
        self.saldo -= valor
        destinatario.depositar(valor)
        print(f'Valor de R${valor:.2f} transferido para {destinatario.nome.title()}.')
        self.historico.append(f'Transferência: -{valor:g}')

    def ver_historico(self):
        if not self.historico:
            print('Nenhum serviço executado.')
            return
        for transacao in self.historico:
            print(transacao)

    def ver_extrato(self):
        print('======== EXTRATO ========')
        print(f'Titular: {self.nome.title()}')
        print(f'Saldo atual: R${self.saldo:.2f}\n')
        
        num = 0
        for i in self.historico:
            num += 1
            print(f'[{num}] {i}')
