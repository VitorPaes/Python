from cpf_cnpj import Documento

#cpf_um = Cpf("15316267454")
#print(cpf_um)
exemplo_cnpj = "35379838000112"
documento = Documento.cria_documento(exemplo_cnpj)
print(documento)