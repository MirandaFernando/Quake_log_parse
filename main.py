import re

from modelos.jogo import Jogo
from parse import parse_jogos


if __name__ == '__main__':
    jogos = parse_jogos('teste.log')
    print("=======================TASK 1=======================")
    for j in jogos:
        print(j)

    print("=======================FIM TASK 1=======================")
        

    

    
    


    
        
