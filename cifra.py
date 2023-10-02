from unidecode import unidecode

def vingenere(text, chave, entrada):

    if (len(chave) >= len(text)): #adaptar o tamanho da chave ao tamanho da mensagem
        return chave
    else:
        temp = len(text) - len(chave)
        for i in range(temp):
            chave+=chave[i]
    
    

    if(entrada == '1'): #CIFRADOR
        text = unidecode(text)
        cifra = ''
        j = 0
        for i in range(len(text)):
        
            if 'a' <= text[i].lower() <= 'z': #intervalo de A a Z - função lower pra converter em minúsculas
                aux = chr(((ord(text[i].lower()) - ord('a') + ord(chave[i-j].lower()) - ord('a')) % 26) + ord('a'))
                cifra += aux
            else:
                j += 1
                cifra += text[i]

        return cifra    
    

    
    elif(entrada == '2'): #DECIFRADOR
 
        textDecifrado = ''
        j = 0
        for i in range(len(text)):
            if 'a' <= text[i] <= 'z': #intervalo de A a Z - função lower pra converter em letras minúsculas
                aux = chr(((ord(text[i].lower()) - ord(chave[i-j].lower()) + 26) % 26) + ord('a'))
                textDecifrado += aux
            else:
                j += 1
                textDecifrado += text[i]

        return textDecifrado