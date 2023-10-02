from cifra import vingenere
from ataque import ataque, tamanho_chave

entrada = str

while entrada != 'E' and entrada != 'e':
    print("-------------------")
    print(" ESCOLHA UMA OPÇÃO ")
    print("-------------------")
    print("\nCifrar (digite 1)") 
    print("Decifrar (digite 2)")
    print("Ataque (digite 3)")
    print("\nEncerrar (digite E)")
    
    entrada = str(input())
    
    if entrada == '1': #cifrar
        print("---------------------------------")
        mensagem = input("CIFRAR\nInforme a mensagem a ser cifrada: ")
        chave = input("Informe a chave desejada: ")
        cifra = vingenere(mensagem, chave, entrada)
        print(f'\nO TEXTO CIFRADO É:\n{cifra}\n')
        
        entrada = input("Deseja fazer outra operação?\nSIM (digite S) ou NÃO (digite N): ")
        print("\n")
        if entrada == 'N' or entrada == 'n':
            break
        
    elif entrada == '2': #decifrar
        print("---------------------------------")
        mensagemCifrada = input("DECIFRAR\nInforme a mensagem a ser decifrada: ")
        chave = input("Informe a chave: ")
        mensagemDecifrada = vingenere(mensagemCifrada, chave, entrada)
        print(f'\nO TEXTO DECIFRADO É:\n{mensagemDecifrada}\n')
        
        entrada = input("Deseja fazer outra operação? SIM (digite S) NÃO (digite N): ")
        if entrada == 'N' or entrada == 'n':
            break

        
    elif entrada == '3': #ataque
        print("---------------------------------")
        mensagem = input("ATAQUE\nInforme a mensagem a ser decifrada: ")
        idiomaAtaque = input("\nEscolha o idioma:\nPortuguês (digite 1) ou Inglês (digite 2): ")
        chave = ataque(mensagem, idiomaAtaque)
        resposta = vingenere(mensagem, chave, '2')

        print("---------- MENSAGEM ----------")
        print(resposta)
        print("------------------------------")

        print("\n")
        
    
    elif entrada == 'E' or entrada == 'e' or entrada == 'N' or entrada == 'n':
        break
    
    else:
        print("\nOpção incorreta!\n")
        
print("\nEXECUÇÃO ENCERRADA.")