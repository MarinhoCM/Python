from .Factory import Factory

from validate_docbr import CNPJ

class Cnpj(Factory):
    def __str__(self) -> str:
        if self.doc_type.upper() == 'CNPJ':
            return self.format_cnpj()
    
    def cnpj_e_valido(self, cnpj: str) -> bool:
        if len(cnpj) == 14:
            validate_cnpj = CNPJ()
            return validate_cnpj.validate(cnpj)
        else:
            raise ValueError(
                "Quantidade de dígitos inválida!"
            )
        
    def format_cnpj(self) -> None:
        cnpj_mask = CNPJ()
        return cnpj_mask.mask(self.cnpj)
    