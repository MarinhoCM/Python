from classes import (ContaCorrente, ContaPoupanca)

conta1 = ContaCorrente(16)
conta1.deposita(1000)
conta1.passa_o_mes()
print(conta1)

conta2 = ContaPoupanca(17)
conta2.deposita(1000)
conta2.passa_o_mes()
print(conta2)

conta3 = ContaPoupanca(37)
print(conta3)
