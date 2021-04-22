import re

from modelos.jogo import Jogo
from parse import parse_jogos


if __name__ == '__main__':
    jogos = parse_jogos('games.log')

    print("======================TASK 1 ===========================")
    for j in jogos:
        print(j)
    print("======================FIM DA TASK 2 ===========================")
    
    print("======================TASK 2 ===========================")
    for j in jogos:
        raking_kills = j.ranking_kills_game()
        print("jogo:",j.jogo_id())
        print("Raking de kills:{")
        for key in raking_kills:
           print("\t",key,":",raking_kills[key])
        print("}")
    print("======================FIM DA TASK 2 ===========================")

    print("======================TASK 3 ===========================")
    for j in jogos:
        lista_mortes = j.mortes_list()
        print("jogo:",j.jogo_id())
        print("kills_by_means:{")
        for key in lista_mortes:
           print("\t",key,":",lista_mortes[key])
        print("}")
    print("======================FIM DA TASK 2 ===========================")    
        

    

    
    


    
        
