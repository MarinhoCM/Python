from utils.Cep import Cep
from utils.Cpf import Cpf
from utils.Cnpj import Cnpj
from utils.Datas import Data
from utils.Telefone import Telefone

cep = Cep("01001000")
cpf = Cpf("12561263611", "cpf")
cnpj = Cnpj("12345678910112", "cnpj")
data = Data()
telefone = Telefone("5585985670102")

print(cep)
print(cpf) # invalido!
print(cnpj) # invalido!
print(data)
print(telefone)
