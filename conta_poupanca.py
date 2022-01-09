from conta import Conta

class ContaPoupanca(Conta):
    def __init__(self, agencia: int, n_conta: int, saldo: float):
        super().__init__(agencia, n_conta, saldo)
        
        
    def sacar(self, valor: float):
        """
        :param valor: valor que será depositado
        """
        if not isinstance(valor, (int or float)):
            raise ('Valor precisar ser um número')
        
        if self.saldo < valor:
            print('Saldo insuficiente')
            return
        
        self.saldo -= valor 