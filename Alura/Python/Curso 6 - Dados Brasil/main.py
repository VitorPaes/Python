

from cpf_cnpj import Documento
from TelefonesBr import TelefonesBr
from datas_br import DatasBr
from datetime import datetime, timedelta
from acesso_cep import BuscaEnderoco
import requests
import re




cep = "03726000"
objeto_cep = BuscaEnderoco(cep)

bairro, cidade, uf = objeto_cep.acessa_via_cep() 

print(bairro, cidade, uf)