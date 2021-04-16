class Jogador:

    def __init__(self, nome_jogador):
        self.nome_jogador = nome_jogador
        self.kills = 0
    
    def __str__(self):
        return 'Nick:%s, kills:%d' % (self.nome_jogador, self.kills)
    
    
 