from codigo.bytebank import Funcionario

from pytest import mark
    
class TestClass:
    def test_quando_idade_recebe_13_03_2000_deve_retornar_22(self):
        entrada = '13/03/2001' # Given-Contexto
        esperado = 22

        funcionario_teste = Funcionario('Teste', entrada, 1111)
        resultado = funcionario_teste.idade() # When-ação

        assert resultado == esperado  # Then-desfecho
    
    @mark.calcular_bonus
    def test_quando_sobrenome_recebe_Lucas_Carvalho_deve_retornar_Carvalho(self):
        entrada = ' Lucas Carvalho ' # Given
        esperado = 'Carvalho'

        lucas = Funcionario(entrada, '11/11/2000', 1111)
        resultado = lucas.sobrenome() # When

        assert resultado == esperado

    @mark.calcular_bonus
    def test_quando_decrescimo_salario_recebe_100000_deve_retornar_90000(self):
        entrada_salario = 100000 #given
        entrada_nome = 'Paulo Bragança'
        esperado = 90000

        funconario_teste = Funcionario(entrada_nome, '11/11/2000', entrada_salario)
        funconario_teste.decrescimo_salario() # when
        resultado = funconario_teste.salario

        assert resultado == esperado  # then
        
    def test_retorno_str(self):
        nome, data_nascimento, salario = ('teste', '12/03/2000', 1000) #given
        esperado =  f'Funcionario(teste, 12/03/2000, 1000)'

        funconario_teste = Funcionario(nome, data_nascimento, salario)
        funconario_teste.decrescimo_salario() # when
        resultado = funconario_teste.__str__()

        assert resultado == esperado  # then
    





