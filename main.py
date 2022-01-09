from conta_corrente import ContaCorrente
from conta_poupanca import ContaPoupanca

c1 = ContaPoupanca(1, 1111, 100)
c2 = ContaCorrente(2, 2222, 100, 100)

c1.depositar(50)
c1.sacar(100)
c1.mostrar()

c2.depositar(50)
c2.sacar(200)
c2.mostrar()