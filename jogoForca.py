def palavraSec():
    palavraSec = input('Digite a palavra secreta: ').lower()
    palavraSecList = list(palavraSec)
    return palavraSecList

def ocultarPalavra(str1):
    palavraOculta = []
    for i in range(len(str1)):
        palavraOculta.append('*')
    return palavraOculta

def verificaTentativa(str1, str2, char1):
    a = 0
    for i in range(len(str1)):
        if char1 == str1[i]:
            a += 1
            str2[i] = letra
    if a > 0: return True
    else: return False

def comparaPalavra(str1, str2):
    if str2 == str1: return True
    else: return False

erro = 7
palavra = palavraSec()
palavraEsc = ocultarPalavra(palavra)

while erro > 0:
    print(f'\nVocê tem {erro} tentativas')
    letra = input('Qual a letra da palavra: ').lower()

    acertou = verificaTentativa(palavra, palavraEsc, letra)
    
    if (acertou!=True): 
        print('\nEssa letra não está na palavra\n')
        erro -= 1
    
    venceu = comparaPalavra(palavra, palavraEsc)
    
    if venceu == True:
        print(palavraEsc)
        print('Você acertou a palavra, parabéns')
        break

    print(palavraEsc)
    
    if erro == 0: 
        print('Suas tenativas acabaram, mais sorte na próxima vez')
        break

print('Fechando o programa, obrigado por jogar')