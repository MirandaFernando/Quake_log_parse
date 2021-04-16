import re

from modelos.jogador import Jogador

class Jogo:

    
    def __init__(self, linhas_do_jogo, game):
        self.linhas_do_jogo =linhas_do_jogo
        self.game = game
        self.total_de_kills = 0
        self.players = []
        self.kills = {}
    
    def Mostrar_linhas(self):
        for linha in self.linhas_do_jogo:
            print(linha)
    
    def retornando_linhas(self):
        return self.linhas_do_jogo
    
   
    def info_game(self):

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

    def verificando_nick(self, nick):
        for p in self.players:
            if nick == p.nome_jogador:
                return True

        return False

    def mostrar_players(self):
        for p in self.players:
            print(p)