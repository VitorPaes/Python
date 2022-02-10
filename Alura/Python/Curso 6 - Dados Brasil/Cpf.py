from xml.dom.expatbuilder import DOCUMENT_NODE


class Cpf:
    def __init__(self, documento):
        documento = str(documento)
        if self.cpf_eh_Valido(documento):
            self.cpf = documento
        else:
            raise ValueError("CPF invalido")
    
    def __str__(self):
        return self.format_cpf()
    
    def cpf_eh_Valido(self, documento):
        if len(documento) == 11:
            return True
        else:
            return False
    
    def format_cpf(self):
        fatia_um = self.cpf[:3]
        fatia_dois = self.cpf[3:6]
        faita_tres = self.cpf[6:9]
        fatia_quatro = self.cpf[9:]
        
        return (
            "{}.{}.{}-{}".format(
            fatia_um,
            fatia_dois,
            faita_tres,
            fatia_quatro
            )
        )
