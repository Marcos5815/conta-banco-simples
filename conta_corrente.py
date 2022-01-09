from conta import Conta

class ContaCorrente(Conta):
    def __init__(self, agencia: int, n_conta: int, saldo: float, limite: float):
        super().__init__(agencia, n_conta, saldo)
        self._limite = limite
        
    
    @property
    def limite(self):
        return self._limite
    
    def sacar(self, valor: float):
        """
        :param valor: valor que será depositado
        """
        if not isinstance(valor, (int or float)):
            raise ValueError('Valor precisa ser um número')
            
        
        if (self.saldo + self.limite) < valor:
            print('Saldo insuficiente')
            return
        
        self.saldo -= valor
        