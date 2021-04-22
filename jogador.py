class Jogador:

    def __init__(self, nome_jogador, id_player):
        self.nome_jogador = nome_jogador
        self.kills = 0
        self.id = id_player
    
    def __str__(self):
        return 'Nick:%s, kills:%d, id:%s' % (self.nome_jogador, self.kills, self.id)
    
    

    
 