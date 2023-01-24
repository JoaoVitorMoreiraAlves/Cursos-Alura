endereço = 'Rua da Flores 72, apartamento 1002, Laranjeiras, Rio de Jnaeiro, RJ, 23440-120'

import re #Regular Expression - RegEx

# 5 digitos + hífen (opcional) + 3 digitos

#Posso usar assim: padrao = re.compile('[0123456789][0123456789][0123456789][0123456789][0123456789][-]?[0123456789][0123456789][0123456789]')

padrao = re.compile('[0-9]{5}[-]{0,1}[0-9]{3}')

busca = padrao.search(endereço) #Match
if busca:
    cep = busca.group()
    print(cep)