import unittest

from modelos.jogo import Jogo
from parse import parse_jogos


class TestJogo(unittest.TestCase):
    def setUp(self):
        self.jogos = parse_jogos('teste.log')

    def test_ranking_kills_game(self):
        jogo1 = self.jogos[0]
        jogo2 = self.jogos[1]
        result = jogo1.ranking_kills_game()
        dict_test = {'Mocinha': 0, 'Isgalamido': -5}
        dict_test2 = {'Isgalamido': 1, 'Dono da Bola': -1, 'Zeh': -2}
        self.assertDictEqual(result, dict_test)
        result = jogo2.ranking_kills_game()
        self.assertDictEqual(result, dict_test2)
        #self.assertDictEqual(result, dict_test)
        

    def test_mortes_list(self):
        jogo1 = self.jogos[0]
        jogo2 = self.jogos[1]
        result = jogo1.mortes_list()
        dict_test = {'MOD_TRIGGER_HURT': 7, 'MOD_ROCKET_SPLASH': 3, 'MOD_FALLING': 1}
        dict_test2 = {'MOD_TRIGGER_HURT': 2, 'MOD_ROCKET': 1, 'MOD_FALLING': 1}
        self.assertDictEqual(result, dict_test)
        result = jogo2.mortes_list()
        self.assertDictEqual(result, dict_test2)
        #self.assertDictEqual(result, dict_test)
    
    def test_jogo_id(self):
        jogo1 = self.jogos[0]
        jogo2 = self.jogos[1]
        self.assertEqual(jogo1.jogo_id(), 1)
        self.assertEqual(jogo2.jogo_id(), 2)
    
    def test_quant_kills(self):
        jogo1 = self.jogos[0]
        jogo2 = self.jogos[1]
        self.assertEqual(jogo1.quant_kills(), 11)
        self.assertEqual(jogo2.quant_kills(), 4)


if __name__ == '__main__':
    unittest.main()