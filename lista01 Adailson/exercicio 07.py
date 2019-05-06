'''Escreva, em sua linguagem de programação favorita, um algoritmo para segmentação
de sentenças(orações) de textos em português. Use o arquivo “texto_pt.txt” em seus
testes.
Dica: baseie-se no algoritmo do slides da Aula 02.'''

#Regras  para segmentação de sentenças(orações) de textos em português.:
# 1 Todo ? ! é um ESO
# 2 se " ou' aparecer antes do período, é EOS.

# 3 se o seguinte caractere não for espaço em branco, não é eso.

# 4 Se tiver )}] antes do período, é o ESO.

# 5 se o token ao qual o período está anexado for capitalizado e for <5 caracteres e
# o próximo token começar em maiúsculas, não será EOS.

# 6 se o token ao qual o período está anexado tiver outros períodos, não será EOS.

# 7 se o token ao qual o período está anexado começar com uma letra minúscula e o próximo
# token após o espaço em branco ser maiúsculo, será EOS.

# 8 se o token ao qual o período está anexado tiver <2 caracteres, não será EOS.

# 9 se o próximo token após o espaço em branco começar com $ ({['" é EOS.  caso contrário, o período não é EOS.


arq = open('texto_pt.txt', 'r', encoding="utf8", errors='ignore')
texto = arq.read().replace('\n', '')
arq.close()

# Usando a biblioteca BLTK
from nltk.tokenize import sent_tokenize
lista = sent_tokenize(texto)
print(lista)

#Tokenização algoritmo

delimitador = [' ', ',', '.', ';', ':', '!', '?', '(', ')','<','>', '+', '"', '\n\t', '\n']
listaToken =[]
palavraAtual =''

for letra in texto:
    if letra in delimitador:
        if letra != ' ' and letra != '\n\t' and letra != '' and palavraAtual == '':
            listaToken.append(letra)
        else:
            if palavraAtual != '':
                listaToken.append(palavraAtual)
                if letra != ' ' and letra != '\n':
                    listaToken.append(letra)
                palavraAtual = ''

    else:
        palavraAtual += letra

# algoritmo para segmentação de sentenças(orações) de textos em português.

listaOracoes = []

oracaoTemp = ''

for token in listaToken:
    if token =='.':
        oracaoTemp = oracaoTemp[:-1]
        oracaoTemp += token
        listaOracoes.append(oracaoTemp)
        oracaoTemp = ''
    else:
        oracaoTemp += token +' '

for i in listaOracoes:
    print(i+'\n')

print('\n\n\n Sentence split do arquivo de texto texto_pt.txt')
