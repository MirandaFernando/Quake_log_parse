import re

from modelos.jogo import Jogo
from parse import parse_jogos


if __name__ == '__main__':
    jogos = parse_jogos('games.log')
    
    for j in jogos:
        print(j)
    

        

    

    
    


    
        
