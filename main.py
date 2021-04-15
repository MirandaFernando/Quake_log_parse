import re

from modelos.jogo import Jogo
from parse import parse_jogos




if __name__ == '__main__':
    teste = 'Kill: 1022 2 22: <world> killed Isgalamido by MOD_TRIGGER_HURT'
    teste2 = ''
    #apresenta quem matou e quem morreu
    kill_regra =':\s([^:]+)\skilled\s(.*?)\sby\s[a-zA-Z_]+'

    matou = '(?<=:\s)(.*?)(?=\skilled)'

    morreu = '(?<=killed\s)(.*?)(?=\sby)'

    causa_morte = '(?<=by\s)(.*?)(?=$)'
    print(re.findall(kill_regra, teste))
    print(re.findall(matou,teste))
    print(re.findall(morreu,teste))