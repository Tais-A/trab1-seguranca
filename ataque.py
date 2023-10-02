import re

def remove_caracteres(mensagem):
    return re.compile('[^a-z]').sub('', mensagem.lower())

def encontrar_trigramas(cifra):
    trigramas = []
    tamanho_cifra = len(cifra)
    
    for i in range(tamanho_cifra - 2):
        trigrama = cifra[i:i+3]
        if trigrama in cifra[i+1:]:
            distancia = cifra[i+1:].index(trigrama) + 1
            trigramas.append(distancia)
    
    return list(set(trigramas))

def analisar_frequencias(trigramas):
    frequencias = [0] * 19
    
    for trigrama in trigramas:
        for k in range(2, 20):
            if trigrama % k == 0:
                frequencias[k - 2] += 1
                
    return frequencias

def tamanho_chave(cifra):
    cifra = remove_caracteres(cifra)
    trigramas = encontrar_trigramas(cifra)
    frequencias = analisar_frequencias(trigramas)
    
    possibilidade = []

    for i, freq in enumerate(frequencias):
        if freq > 0:
            possibilidade.append([i+2, freq])

    possibilidades_ordenadas = sorted(possibilidade, key=lambda x: x[1], reverse=True)
    primeiros_elementos = [sublista[0] for sublista in possibilidades_ordenadas]

    try:
    
        multiplicador = primeiros_elementos[0]
        tamanho = primeiros_elementos[0]

        try: 
            valor = possibilidades_ordenadas[1][1] - possibilidades_ordenadas[0][1] 
        except:
            valor = 0 

        for i in range(len(primeiros_elementos)):
            if primeiros_elementos[i] * multiplicador == primeiros_elementos[i+ 1]:
                aux = valor
                valor = possibilidades_ordenadas[i+1][1] - possibilidades_ordenadas[i][1]
                if valor == aux or valor == 0:
                    tamanho = primeiros_elementos[i] * multiplicador

            else:
                break

    except:
        print()
        print("----------- ERRO!! -----------")
        print("Tamanho da cifra insuficiente")
        print("------------------------------")
        tamanho = 1

    return tamanho

def calcular_diferenca(freqCifra, linguagem):
    diferenca_min = float('inf')
    melhor_letra = ''

    portugues = {
        'a': 14.63, 'b': 1.04, 'c': 3.88, 'd': 4.99, 'e': 12.57,'f': 1.02, 'g': 1.30, 'h': 1.28, 'i': 6.18,  'j': 0.4,  'k': 0.02, 'l': 2.78, 'm': 4.74, 'n': 5.05, 'o': 10.73,'p': 2.52, 
        'q': 1.20,  'r': 6.53, 's': 7.81, 't': 4.34, 'u': 4.63, 'v': 1.67, 'w': 0.01, 'x': 0.21, 
        'y': 0.01, 'z': 0.47
        }

    ingles = {
        'a': 8.167, 'b': 1.492, 'c': 2.782, 'd': 4.253, 'e': 12.702, 'f': 2.228, 'g': 2.015, 
        'h': 6.094, 'i': 6.966, 'j': 0.153, 'k': 0.772, 'l':  4.025, 'm': 2.406, 'n': 6.749, 
        'o': 7.507, 'p': 1.929, 'q': 0.095, 'r': 5.987, 's':  6.327, 't': 9.056, 'u': 2.758,
        'v': 0.978, 'w': 2.36,  'x': 0.15,  'y': 1.974, 'z': 0.074
        }
    
    referencia = portugues if linguagem == '1' else ingles

    for deslocamento in range(26):
        diferenca = 0
        for letra in range(97, 123):  # ASCII de 'a' a 'z'
            letra_deslocada = (letra - 97 + deslocamento) % 26 + 97
            diferenca += abs(referencia[chr(letra)] - freqCifra[chr(letra_deslocada)])

        if diferenca < diferenca_min:
            diferenca_min = diferenca
            melhor_letra = chr(97 + deslocamento)  # ASCII para letra

    return melhor_letra


def ataque(mensagem, linguagem):
    
    tamanho_da_chave = tamanho_chave(mensagem)

    cifra = remove_caracteres(mensagem)

    freqCifra = {i: 0 for i in range(97, 123)}

    segmentos = len(cifra) // tamanho_da_chave
    freqPercentual = 100 / float(segmentos)


    chave = ''

    for i in range(tamanho_da_chave):
        freqCifra = {chr(j): 0 for j in range(97, 123)}

        for j in range(segmentos):
            caracter = cifra[j * tamanho_da_chave + i]
            freqCifra[caracter] += freqPercentual

        chave += calcular_diferenca(freqCifra, linguagem)


    print()
    print("----------- CHAVE -----------")
    print(chave)
    print()
    return chave
