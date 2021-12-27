# “http://bytebank.naoexiste/cambio”

import re

url = 'http://www.bytebank.com/cambio'
padrao_url = re.compile('(http(s)?://)?(www.)?bytebank.com(.br)?/cambio')
match = padrao_url.match(url)

if not match:
    raise ValueError("A Url nao e valida")

print("A Url e valida")