'''Use o NLTK para criar um pipeline que realize as seguintes tarefas, nesta ordem:
 Tokenization, Sentence Splitting, Lemmatization, Stemming e POS tagging
Em seguida gere as seguintes informações estatísticas e gráficos de barras em relação ao
texto em inglês “texto_en.txt”:
a. Quantas palavras temos em todo o texto?
b. Quantos radicais (stemming) diferentes existem?
c. Qual o número de sentenças e a média de tokens por sentença?
d.

e. Gere um gráfico de barra do conjunto de POS tags de todas as palavras do texto.
Ordene os resultados e responda: quais classes gramaticais correspondem a mais
de 70 ou 80% do total?
f. Gera um outro gráfico de baras de todos os radicais presentes no texto. Ordene-os
por sua contagem no texto e depois responda:
o Existe alguma característica que se sobressai em relação as categorias
gramaticais dos primeiros colocados na lista ordenada?'''

from nltk import PorterStemmer, LancasterStemmer, WordNetLemmatizer,sent_tokenize, word_tokenize, pos_tag
import numpy
import matplotlib.pyplot as plt

arq = open('texto_en.txt', 'r', encoding="utf8", errors='ignore')
texto = arq.read().replace('\n', '')
arq.close()

lancaster=LancasterStemmer()
wordnet_lemmatizer = WordNetLemmatizer()
ps = PorterStemmer()

def tokenize_text(text):
    return word_tokenize(text)
def tokenize_sent(text):
    return sent_tokenize(text)


def removeCaracteresEspecias(listaToken):
    listaToken2= []
    punctuations = "?:!.,; ''``-_+={[]]}@#$%¨&*()+§<>|\/?°ªº"
    for word in listaToken:
        if word in punctuations:
            pass
        else:
            listaToken2.append(word)
    return listaToken2


def lematizer(listatoken):
    listaToken = removeCaracteresEspecias(listatoken)
    print("{0:20}{1:20}".format("Word","Lemma"))
    for word in listaToken:
        print ("{0:20}{1:20}".format(word,wordnet_lemmatizer.lemmatize(word)))

def stem_text(listaToken):
    listaToken = removeCaracteresEspecias(listaToken)
    listaRadicais = []
    for word in listaToken:
        listaRadicais.append(ps.stem(word))
    return listaRadicais

def posTag (listaToken):
    return pos_tag(listaToken)

listaToken = tokenize_text(texto)
listaSent = sent_tokenize(texto)
#lematizer(listaToken)
listaRadicais = stem_text(listaToken)
listaPOSTags = posTag(listaToken)

'''a. Quantas palavras temos em todo o texto?'''
totalPalavras = len(removeCaracteresEspecias(listaToken))
print('Tem : %d palavras.'%(totalPalavras))

'''b. Quantos radicais (stemming) diferentes existem?'''
listaS = stem_text(listaToken)
listaDiferentes =[]
for radical in listaS:
    if radical in listaDiferentes:
        pass
    else:
        listaDiferentes.append(radical)
print('O total de radicais diferente é: ', len(listaDiferentes))

'''c. Qual o número de sentenças e a média de tokens por sentença?'''

print('O número de sentenças é: %d, e a média de tokens de cada senteça é: %d.'%(len(listaSent), (totalPalavras/len(listaSent))))

'''e. Gere um gráfico de barra do conjunto de POS tags de todas as palavras do texto.
Ordene os resultados e responda: quais classes gramaticais correspondem a mais
de 70 ou 80% do total?'''
dicTiposDePOS = {}
dicTiposDePOS2 = {}
for pos in listaPOSTags:
    if pos[1] in dicTiposDePOS:
        dicTiposDePOS[pos[1]].append(pos[0])
    else:
        dicTiposDePOS[pos[1]] = []
listaPOSOrdenada = []
listaValoresPOSOrdenados = []
listaPOSMaiorFrequencia = []
for chave, valor in dicTiposDePOS.items():
    if chave not in "?:!.,; ''``-_+={[]]}@#$%¨&*()+§<>|\/?°ªº'":
        dicTiposDePOS2[chave] = len(valor)
for item in sorted(dicTiposDePOS2, key=dicTiposDePOS2.get):
    listaPOSOrdenada.append(item)
    listaValoresPOSOrdenados.append(dicTiposDePOS2[item])

cont = 0
for i in listaValoresPOSOrdenados:
    if ((i*100)/len(listaValoresPOSOrdenados)) > 70:
        listaPOSMaiorFrequencia.append(listaPOSOrdenada[cont])
    cont += 1
print('Essas classes gramaticais correspondem a mais de 70 ou 80% do total : ', listaPOSMaiorFrequencia)
plt.barh(listaPOSOrdenada, listaValoresPOSOrdenados, color='green')
plt.ylabel('POS Tags')
plt.xlabel('Frequência dos POS Tags')
plt.title('POS Tags ordenado pela frequência')
plt.show()


'''f. Gera um outro gráfico de baras de todos os radicais presentes no texto. Ordene-os
por sua contagem no texto e depois responda:
o Existe alguma característica que se sobressai em relação as categorias
gramaticais dos primeiros colocados na lista ordenada?'''

dicRadicais = {}

for i in listaRadicais:
    if i in dicRadicais:
        dicRadicais[i]= dicRadicais[i]+1
    else:
        dicRadicais[i] = 1
listaRadicaisOrdenados = []
listaFrequenciaDoRadical = []
for item in sorted(dicRadicais, key=dicRadicais.get):
    listaRadicaisOrdenados.append(item)
    listaFrequenciaDoRadical.append(dicRadicais[item])

plt.barh(listaRadicaisOrdenados[len(listaRadicaisOrdenados)-10:], listaFrequenciaDoRadical[len(listaRadicaisOrdenados)-10:], color='red')
plt.ylabel('Radical das palavras ')
plt.xlabel('Frequência dos  radicais')
plt.title('OS 10 Radicais que mais aparecem.')
plt.show()
