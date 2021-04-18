import re

from modelos.jogo import Jogo


def parse_jogos(arquivo):
    with open(arquivo) as f:
        linhas = f.readlines()
    regexp = 'InitGame'
    regexp2 = '--------+'
    jogos = []
    inicio = 0
    fim = 0
    for i, linha in enumerate(linhas):        
        if re.findall(regexp, linha):
            inicio = i
        elif i == 0:
            pass
        elif (fim+1) == i:
            pass
        elif re.findall(regexp2, linhas[i]):
            fim = i
            array_linhas_jogo = retornando_jogos(inicio,fim,linhas)
            game = len(jogos)+1
            jogo = Jogo(array_linhas_jogo,game)
            jogos.append(jogo)                            
    return jogos

def retornando_jogos(inicio,fim,linhas):
    linhas_jogo = []
    for i, linha in enumerate(linhas):
        if i >= inicio:
            linhas_jogo.append(linha)
        if i == fim:
            break
    return linhas_jogo
    

