from abc import ABC, abstractmethod

class Conta(ABC):
    def __init__(self, agencia: int, n_conta: int, saldo: float):
        """Descrição
        
        :param agencia: Número da agência
        :param n_conta: Número da conta
        :param saldo: Saldo disponível na conta     
        """
        
        self._agencia = agencia
        self._n_conta = n_conta
        self._saldo = saldo
        

    @property
    def agencia(self):
        return self._agencia
    
    @property
    def n_conta(self):
        return self._n_conta
    
    @property
    def saldo(self):
        return self._saldo
    
    @saldo.setter
    def saldo(self, valor):
        self._saldo = valor
        
    def depositar(self, valor: float):
        """
        :param valor: valor que será depositado
        """
        if not isinstance(valor, (int or float)):
            raise ValueError('Valor precisa ser um número')
        
        self._saldo += valor
    
    @abstractmethod
    def sacar(self, valor: float):
        pass
    
    
    def mostrar(self):
        print(f'{self.saldo}')