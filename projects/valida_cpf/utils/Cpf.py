from .Factory import Factory  

from validate_docbr import CPF

class Cpf(Factory):
    def __str__(self):
        if self.doc_type.upper() == 'CPF':
            return self.format_cpf()
    
    def cpf_e_Valido(self, cpf: str):
        if len(cpf) == 11:
            validator = CPF()
            return validator.validate(cpf)
        else:
            raise ValueError(
                "Quantidade de dígitos inválida!"
            )

    def format_cpf(self):
        cpf_mask = CPF()
        return cpf_mask.mask(self.cpf)
