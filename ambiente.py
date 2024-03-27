import random
from agente import Agente

class Ambiente:
    def __init__(self):
        self.estado = {'A': random.choice(['cheio', 'vazio']),
                       'B': random.choice(['cheio', 'vazio'])}
        self.accao = ['encher', 'esquerda', 'direita']

    def percepcao(self, agente):
        return (agente.localizacao, self.estado[agente.localizacao])

    def localizacaodefault(self):
        return random.choice(['A', 'B'])

    def executarAccao(self, agente, accao):
        if accao == 'esquerda':
            agente.desempenho -= 1
        elif accao == 'direita':
            agente.desempenho -= 1
        elif accao == 'encher':
            agente.desempenho += 10
            self.estado[agente.localizacao] = "cheio"

    def busca_em_largura(self, agente):
        frontier = [agente.localizacao]
        while frontier:
            current_location = frontier.pop(0)
            percepcao = self.percepcao(agente)
            accao = self.programa(percepcao)
            self.executarAccao(agente, accao)
            if accao == 'direita':
                agente.localizacao = 'B' if agente.localizacao == 'A' else 'A'
            print("Percepção:", percepcao)
            print("Ação:", accao)
            print("Estado do ambiente:", self.estado)
            print("Desempenho do agente:", agente.desempenho)

    def busca_em_profundidade(self, agente):
        frontier = [agente.localizacao]
        while frontier:
            current_location = frontier.pop()
            percepcao = self.percepcao(agente)
            accao = self.programa(percepcao)
            self.executarAccao(agente, accao)
            if accao == 'direita':
                agente.localizacao = 'B' if agente.localizacao == 'A' else 'A'
            print("Percepção:", percepcao)
            print("Ação:", accao)
            print("Estado do ambiente:", self.estado)
            print("Desempenho do agente:", agente.desempenho)

    def programa(self, percepcao):
        localizacao, estado = percepcao
        if estado == 'vazio':
            return 'encher'
        elif localizacao == 'A':
            return 'direita'
        elif localizacao == 'B':
            return 'direita'

ambiente = Ambiente()
print("Estado do ambiente:", ambiente.estado)
agente = Agente(ambiente.localizacaodefault())

print("\nBusca em Largura:")
ambiente.busca_em_largura(agente)

# Reset environment
agente = Agente(ambiente.localizacaodefault())
ambiente = Ambiente()

print("\nBusca em Profundidade:")
ambiente.busca_em_profundidade(agente)
