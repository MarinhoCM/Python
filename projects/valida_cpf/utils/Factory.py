"""
Módulo responsável por armazenar a classe Factory e seu construtor
"""
class Factory:
    def __init__(self, doc: str, doc_type: str) -> None:
        self.doc_type = str(doc_type)
        doc = str(doc)
        if self.doc_type.upper() == "CPF":
            if self.cpf_e_Valido(doc):
                self.cpf = doc
            else:
                raise ValueError("CPF inválido!")
        elif self.doc_type.upper() == "CNPJ":
            if self.cnpj_e_valido(doc):
                self.cnpj = doc
            else:
                raise ValueError("CNPJ inválido!")
        else:
            raise ValueError("Documento inválido!")
    