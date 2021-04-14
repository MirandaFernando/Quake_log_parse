import re


def parse_jogos(arquivo = 'games.log'):
    with open(arquivo) as f:
        linhas = f.readlines()
    regexp = 'InitGame'
    regexp2 = '--------+'

    inicio = 0
    fim = 0
    for i, linha in enumerate(linhas):
        
        if re.findall(regexp, linha):
            inicio = i 
            print(inicio)
        elif re.findall(regexp2, linhas[i+1]):
            print(i)
            break
            #lista[i] = linha[0].split()


if __name__ == '__main__':
    parse_jogos()