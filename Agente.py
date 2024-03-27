import random

class Agente():
    def __init__(self, localizacao):
        self.desempenho = 0
        self.localizacao = localizacao

    def programa(self, acoes):
        return random.choice(acoes)
    
    def programa_tabela_2(self, percepcao):
        percepcoes = []
        A, B, C = 'A', 'B', 'C'
        tabela = {
            ((A, 'cheio'),): 'direita',
            ((A, 'vazio'),): 'encher',
            ((B, 'cheio'),): 'esquerda',
            ((B, 'vazio'),): 'encher',
            ((C, 'cheio'),): 'esquerda',
            ((C, 'vazio'),): 'encher',
            ((A, 'vazio'), (A, 'cheio')): 'esquerda',
            ((A, 'cheio'), (B, 'vazio')): 'encher',
            ((B, 'cheio'), (A, 'vazio')): 'encher',
            ((B, 'vazio'), (B, 'cheio')): 'encher',
            ((A, 'vazio'), (A, 'cheio'), (B, 'vazio')): 'encher',
            ((B, 'vazio'), (B, 'cheio'), (A, 'vazio')): 'encher',
            ((A, 'vazio'), (B, 'vazio'), (C, 'cheio')): 'encher',
            ((B, 'vazio'), (C, 'vazio'), (A, 'cheio')): 'encher'
        }
        percepcoes.append(percepcao)
        return tabela.get(tuple(percepcoes))

percepcoes = []
A, B, C = 'A', 'B', 'C'
