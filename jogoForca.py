from os import system as sy
from colorama import init
from colorama import Fore as cor 

init(autoreset=True)

def palavraSec():
    palavraSec = input(cor.BLUE + 'Digite a palavra secreta: ').lower()
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

while True:
    sy('clear')
    erro = 7
    palavra = palavraSec()
    palavraEsc = ocultarPalavra(palavra)
    while erro > 0:
        print(cor.GREEN + f'\nVocê tem {erro} tentativas')
        letra = input('Qual a letra da palavra: ').lower()

        acertou = verificaTentativa(palavra, palavraEsc, letra)
        
        if (acertou!=True): 
            print(cor. RED + '\nEssa letra não está na palavra\n')
            erro -= 1
        
        venceu = comparaPalavra(palavra, palavraEsc)
        
        if venceu == True:
            print(palavraEsc)
            print( cor.GREEN + 'Você acertou a palavra, parabéns')
            break

        print(palavraEsc)
        
        if erro == 0: 
            print(cor.RED + 'Suas tenativas acabaram, mais sorte na próxima vez')
            break
    
    jogar = input('Deseja jogar novamente?\nR:').lower()
    if jogar != 'sim':
        break

print(cor.CYAN + '\nFechando o programa, obrigado por jogar')