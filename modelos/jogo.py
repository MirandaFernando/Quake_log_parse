import re
import operator


from modelos.jogador import Jogador
from modelos.mortes import Mortes

class Jogo:

    
    def __init__(self, linhas_do_jogo, game):
        self.linhas_do_jogo =linhas_do_jogo
        self.game = game
        self.total_de_kills = 0
        self.players = []
        self.kills = {}
        self.tipo_mortes ={}
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
                if world_morte[0].find("world") != -1:
                    #print("entrou")
                    player_morto = re.findall(morreu, linha)
                    self.sub_morte(player_morto)
                else:
                    #print("entrou")
                    player_matou = re.findall(matou, linha)
                    self.somar_morte(player_matou)
        self.atualizar_dicionario()
         

    def somar_morte(self, player_morto_matou):
        for p in self.players:
            if player_morto_matou[0].find(p.nome_jogador)!=-1:
                p.kills = p.kills + 1

    def sub_morte(self, player_morto_matou):
        for p in self.players:
            if p.nome_jogador == player_morto_matou[0]:
                p.kills = p.kills - 1

    def verificando_nick(self, nick):
        for p in self.players:
            if nick == p.nome_jogador:
                return True

        return False

    def atualizar_dicionario(self):
        for p in self.players:
            self.kills[p.nome_jogador] = p.kills
    
    def ranking_game(self):
        #print sorted(dic.items(), key=itemgetter(1), reverse=True)
        ranking ={}
        sortedDict = sorted(self.kills.items(), key=operator.itemgetter(1), reverse=True)
        for key in sortedDict:
            ranking[key[0]] = key[1]
        print("raking de kills{")
        for key in ranking:
            print("\t",key,":",ranking[key])
        print("}")

    def atualizar_causa_morte(self):
        kill = ':\s([^:]+)\skilled\s(.*?)\sby\s[a-zA-Z_]+'
        causa_da_morte = '(?<=by\s)(.*?)(?=$)'
        for linha in self.linhas_do_jogo:
            if re.findall(kill, linha):
                key = re.findall(causa_da_morte, linha)
                if key[0] in self.tipo_mortes:
                    self.tipo_mortes[key[0]] = self.tipo_mortes[key[0]] + 1
                else:
                    self.tipo_mortes[key[0]] = 1       
        ranking ={}
        sortedDict = sorted(self.tipo_mortes.items(), key=operator.itemgetter(1), reverse=True)
        for key in sortedDict:
            ranking[key[0]] = key[1]
        print("kills_by_means:{")
        for key in ranking:
            print("\t",key,":",ranking[key])
        print("}")
    




    def __str__(self):
        return 'jogo%s:{\n total_kills: %d;\n %s' % (self.game, self.total_de_kills, self.kills)