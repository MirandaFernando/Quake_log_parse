import re

from modelos.jogador import Jogador
from modelos.mortes import Mortes

class Jogo:

    
    def __init__(self, linhas_do_jogo, game):
        self.linhas_do_jogo =linhas_do_jogo
        self.game = game
        self.total_de_kills = 0
        self.players = []
        self.kills = {}
        self.atualizando_info_game()
    
    def Mostrar_linhas(self):
        for linha in self.linhas_do_jogo:
            print(linha)
    
    def retornando_linhas(self):
        return self.linhas_do_jogo
    
   
    def atualizando_info_game(self):
        kill = ':\s([^:]+)\skilled\s(.*?)\sby\s[a-zA-Z_]+'
        matou = '(?<=:\s)(.*?)(?=\skilled)'
        morreu = '(?<=killed\s)(.*?)(?=\sby)'
        for linha in self.linhas_do_jogo:
            
            if linha.find('ClientUserinfoChanged:')!= -1:
                inicio_nick = linha.find('n\\')
                fim_nick = linha.find('\\t')
                cont = inicio_nick + 2
                nick_list = []
                while(cont < fim_nick):
                    nick_list.append(linha[cont])
                    cont = cont + 1
                nick = ''.join(nick_list)
                if self.verificando_nick(nick):
                    pass
                else:
                    player = Jogador(nick)
                    self.players.append(player)
            
            if re.findall(kill, linha):
                self.total_de_kills = self.total_de_kills +1
                world_morte = re.findall(matou, linha)
                #print(world_morte[0])
                if world_morte[0] == "1022 2 22: <world>":
                    player_morto = re.findall(morreu, linha)
                    #print(str(player_morto))
                    self.atualizar_kills_player(player_morto, -1)
                else:
                    player_matou = re.findall(matou, linha)
                    #print(str(player_matou))
                    self.atualizar_kills_player(player_matou, 1)
        self.atualizar_dicionario()

            

    def atualizar_kills_player(self, player_morto_matou, x):
        for p in self.players:
            if p.nome_jogador == player_morto_matou[0]:
                p.kills = p.kills + x

    def verificando_nick(self, nick):
        for p in self.players:
            if nick == p.nome_jogador:
                return True

        return False

    def mostrar_players(self):
        for p in self.players:
            print(p)
    
    def mostrar_toltal_kills(self):
        print(self.total_de_kills)
    
    def atualizar_dicionario(self):
        for p in self.players:
            self.kills[p.nome_jogador] = p.kills

    def dicionario(self):
        print(self.kills)

    def __str__(self):
        return 'jogo%s:{\n total_kills: %d;\n %s' % (self.game, self.total_de_kills, self.kills)