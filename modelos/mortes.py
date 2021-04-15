class Mortes:

    def __init__(self, matou, morreu, causa_morte):
        self.matou = matou
        self.morreu = morreu
        self.causa_morte = causa_morte
    
    def __str__(self):
        print(self.matou, self.morreu, self.causa_morte)