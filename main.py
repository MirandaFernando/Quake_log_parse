import re

from modelos.jogo import Jogo
from parse import parse_jogos


if __name__ == '__main__':
    jogos = parse_jogos('games.log')
    print("=======================TASK 1=======================")
    for j in jogos:
        j.mortes_list()

    print("=======================FIM TASK 1=======================")
        

    

    
    


    
        
