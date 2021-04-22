import re
import operator


from modelos.jogador import Jogador

class Jogo:
   
    def __init__(self, linhas_do_jogo, game):
        self.linhas_do_jogo =linhas_do_jogo
        self.game = game
        self.total_de_kills = 0
        self.players = []
        self.kills = {}
        self.tipo_mortes ={}
        self.atualizando_info_game()
    
    def atualizando_info_game(self):
        #expressões para encontrar palavras
        kill = ':\s([^:]+)\skilled\s(.*?)\sby\s[a-zA-Z_]+'
        matou = '(?<=:\s)(.*?)(?=\skilled)'
        morreu = '(?<=killed\s)(.*?)(?=\sby)'
        regex_id = '[\d+]'
        regex_id_kill = '(?<=:\s)(.*?)(?=\skilled)'
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
                id_player = linha[inicio_nick-2]
                #Verifica se o player ja foi cadastrado com outro id                
                if self.verificando_id(id_player):   
                    for p in self.players:
                        if id_player == p.id:
                            p.nome_jogador = nick
                else:
                    player = Jogador(nick, id_player)
                    self.players.append(player)
            #verifica se alguem morreu ou matou na linha e vai somar ou subtrair de acordo com as regras
            if re.findall(kill, linha):
                self.total_de_kills = self.total_de_kills +1
                world_morte = re.findall(matou, linha)
                if world_morte[0].find("world") != -1:
                    index_id = re.findall(regex_id_kill, linha)
                    id_morreu = index_id[0]
                    self.sub_morte(id_morreu[5])
                else:
                    index_id = re.findall(regex_id_kill, linha)
                    id_matou = index_id[0]
                    self.somar_morte(id_matou[0])
        self.atualizar_raking_kills()
         

    def somar_morte(self, id_player):
        for p in self.players:
            if id_player == p.id:
                p.kills = p.kills + 1

    def sub_morte(self, id_player):
        for p in self.players:
            if p.id == id_player:
                p.kills = p.kills - 1

    def verificando_id(self, id):
        for p in self.players:
            if id == p.id:
                return True

        return False

    def atualizar_raking_kills(self):
        for p in self.players:
            self.kills[p.nome_jogador] = p.kills
    
    def ranking_kills_game(self):
        ranking ={}
        sortedDict = sorted(self.kills.items(), key=operator.itemgetter(1), reverse=True)
        for key in sortedDict:
            ranking[key[0]] = key[1]

        return ranking

    def mortes_list(self):
        #expressões para encontrar palavras relacionada as kills
        kill = ':\s([^:]+)\skilled\s(.*?)\sby\s[a-zA-Z_]+'
        causa_da_morte = '(?<=by\s)(.*?)(?=$)'
        
        for linha in self.linhas_do_jogo:
            if re.findall(kill, linha):
                key = re.findall(causa_da_morte, linha)
                if key[0] in self.tipo_mortes:
                    self.tipo_mortes[key[0]] = self.tipo_mortes[key[0]] + 1
                else:
                    self.tipo_mortes[key[0]] = 1       
        ranking_mortes ={}
        sortedDict = sorted(self.tipo_mortes.items(), key=operator.itemgetter(1), reverse=True)
        for key in sortedDict:
            ranking_mortes[key[0]] = key[1]
        
        return ranking_mortes
    
    def jogo_id(self):
        return self.game
    
    def quant_kills(self):
        return self.total_de_kills 
    
    def __str__(self):
        return 'jogo%s:{\n total_kills: %d;\n %s' % (self.game, self.total_de_kills, self.kills)