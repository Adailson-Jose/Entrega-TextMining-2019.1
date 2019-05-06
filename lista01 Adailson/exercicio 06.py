'''Escreva, em sua linguagem de programação favorita, um algoritmo de tokenização
para a língua portuguesa. Use o arquivo “texto_pt.txt” em seus testes.
Dica: baseie-se no algoritmo dos slides da Aula 02.'''


arq = open('texto_pt.txt', 'r', encoding="utf8", errors='ignore')
texto = arq.read().replace('\n', '')
arq.close()
# Usando a biblioteca NLTK
from nltk.tokenize import word_tokenize
lista = word_tokenize(texto)
#print(lista)
#Meu algoritmo

delimitador = [' ' ,',', '.', ';', ':', '!', '?', '(', ')','<','>', '+', '"', '\n\t', '\n']
listaToken =[]
palavraAtual =''

for letra in texto:
    if letra in delimitador:
        if letra != ' ' and letra != '\n\t' and letra != '' and palavraAtual == '':
            listaToken.append(letra)
        else:
            if palavraAtual != '' :
                listaToken.append(palavraAtual)
                if letra != ' ':
                    listaToken.append(letra)
                palavraAtual = ''

    else:
        palavraAtual += letra

for i in listaToken:
    print(i)
print('\n\nTokens  da arquivo de texto texto_pt.txt')
