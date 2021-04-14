import re

from jogo import Jogo


def parse_jogos(arquivo = 'games.log'):
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
        elif re.findall(regexp2, linhas[i+1]):
            fim = i
            array_linhas_jogo = retornando_jogos(inicio,fim,linhas)
            jogo = Jogo(array_linhas_jogo)
            jogos.append(jogo)
            for jogo in jogos:
                jogo.Mostrar_linhas()
                break
            break
            #lista[i] = linha[0].split()

def retornando_jogos(inicio,fim,linhas):
    linhas_jogo = []
    for i, linha in enumerate(linhas):
        if i >= inicio:
            linhas_jogo.append(linha)
        if i == fim:
            break
    return linhas_jogo
    

if __name__ == '__main__':
    parse_jogos()