import re

from modelos.jogo import Jogo
from parse import parse_jogos


if __name__ == '__main__':
    jogos = parse_jogos('games.log')
    #jogo4 = jogos[4]
    #jogo4.Mostrar_linhas()
    #jogo4.mostrar_players()
    #jogo4.mostrar_toltal_kills()
    #jogo1.mostrar_players()
    for j in jogos:
        print(j)

    

    
    


    
        
