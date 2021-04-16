import re

from modelos.jogo import Jogo
from parse import parse_jogos




if __name__ == '__main__':
    jogos = parse_jogos()
    jogo1 = jogos[1]
    #jogo1.Mostrar_linhas()
    #linhas = jogo1.retornando_linhas()
    jogo1.info_game()

    jogo1.mostrar_players()


    
        
