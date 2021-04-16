import re

from modelos.jogo import Jogo
from parse import parse_jogos


if __name__ == '__main__':
    jogos = parse_jogos()
    jogo16 = jogos[16]
    #jogo16.Mostrar_linhas()
    jogo16.mostrar_players()
    jogo16.mostrar_toltal_kills()
    #jogo1.mostrar_players()

    

    
    


    
        
