"""
    * Thiago Lourenço C. Bezerra.
    * Algoritmos Genéticos - Caixeiro viajante.
    * Universidade de Pernambuco - Computação Natural.
"""

import random
import math
import heapq


""" Um vértice é o caminho entre duas cidade, representada por um número.
    Além disso, tem um coordenada X e Y p/ calcular a distância."""
class Vertice:

    def __init__(self, numero, coordX, coordY):
        self.numero = numero
        self.coordX = coordX
        self.coordY = coordY

listaVertice = [
    Vertice(1, 565.0, 575.0),
    Vertice(2, 25.0, 185.0),
    Vertice(3, 345.0, 750.0),
    Vertice(4, 945.0, 685.0),
    Vertice(5, 845.0, 655.0),
    Vertice(6, 880.0, 660.0),
    Vertice(7, 25.0, 230.0),
    Vertice(8, 525.0, 1000.0),
    Vertice(9, 580.0, 1175.0),
    Vertice(10, 650.0, 1130.0),
    Vertice(11, 1605.0, 620.0),
    Vertice(12, 1220.0, 580.0),
    Vertice(13, 1465.0, 200.0),
    Vertice(14, 1530.0, 5.0),
    Vertice(15, 845.0, 680.0),
    Vertice(16, 725.0, 370.0),
    Vertice(17, 145.0, 665.0),
    Vertice(18, 415.0, 635.0),
    Vertice(19, 510.0, 875.0),
    Vertice(20, 560.0, 365.0),
    Vertice(21, 300.0, 465.0),
    Vertice(22, 520.0, 585.0),
    Vertice(23, 480.0, 415.0),
    Vertice(24, 835.0, 625.0),
    Vertice(25, 975.0, 580.0),
    Vertice(26, 1215.0, 245.0),
    Vertice(27, 1320.0, 315.0),
    Vertice(28, 1250.0, 400.0),
    Vertice(29, 660.0, 180.0),
    Vertice(30, 410.0, 250.0),
    Vertice(31, 420.0, 555.0),
    Vertice(32, 575.0, 665.0),
    Vertice(33, 1150.0, 1160.0),
    Vertice(34, 700.0, 580.0),
    Vertice(35, 685.0, 595.0),
    Vertice(36, 685.0, 610.0),
    Vertice(37, 770.0, 610.0),
    Vertice(38, 795.0, 645.0),
    Vertice(39, 720.0, 635.0),
    Vertice(40, 760.0, 650.0),
    Vertice(41, 475.0, 960.0),
    Vertice(42, 95.0, 260.0),
    Vertice(43, 875.0, 920.0),
    Vertice(44, 700.0, 500.0),
    Vertice(45, 555.0, 815.0),
    Vertice(46, 830.0, 485.0),
    Vertice(47, 1170.0, 65.0),
    Vertice(48, 830.0, 610.0),
    Vertice(49, 605.0, 625.0),
    Vertice(50, 595.0, 360.0),
    Vertice(51, 1340.0, 725.0),
    Vertice(52, 1740.0, 245.0)
]

tamanhoDaListaDeVertices = len(listaVertice)

#Possível solução.
class Cromossomo:

    caminho = [] #O caminho é o conjunto de genes. E cada gene é uma cidade/vértice.
    valorFitness = -1

    #Método de comparação rica, ao fazer x < y ele chama esse método.
    def __lt__(self, other):
        return self.calculaFitness() < other.calculaFitness()

    #Obs.: Nesse caso o menor valor é o melhor fitness, pois estamos calculando a distãncia.
    def calculaFitness(self):
        global listaVertice
        global tamanhoDaListaDeVertices

        if(self.valorFitness == -1):
            soma = 0
            for x in range(tamanhoDaListaDeVertices - 1):
                verticeUmDaVez = listaVertice[self.caminho[x] - 1]       #Menos um porque volta pra origem.
                verticeDoisDaVez = listaVertice[self.caminho[x+1] - 1]   #Menos um porque volta pra origem.
                soma += math.sqrt(((verticeUmDaVez.coordX - verticeDoisDaVez.coordX) ** 2) + ((verticeUmDaVez.coordY - verticeDoisDaVez.coordY) ** 2))

            verticeUmDaVezVoltandoAOrigem = listaVertice[self.caminho[0] - 1]
            verticeDoisDaVezVoltandoAOrigem = listaVertice[self.caminho[tamanhoDaListaDeVertices - 1] - 1]
            soma += math.sqrt(((verticeUmDaVezVoltandoAOrigem.coordX - verticeDoisDaVezVoltandoAOrigem.coordX) ** 2) + ((verticeUmDaVezVoltandoAOrigem.coordY - verticeDoisDaVezVoltandoAOrigem.coordY) ** 2))

            self.valorFitness = round(soma, 4)

        return self.valorFitness

inicializadorDaPopulacao = []

#Cria um vetor de 1 até a quantidade de vértices/cidades.
for x in range(1, tamanhoDaListaDeVertices + 1):
    inicializadorDaPopulacao.append(x)

"""TESTANDO OS VALORES GERADOS.
print(inicializadorDaPopulacao)
populacao = []
tamanhoDaPopulacao = 5

for x in range(tamanhoDaPopulacao):
    cromossomo = Cromossomo()
    cromossomo.caminho = inicializadorDaPopulacao[:]
    random.shuffle(cromossomo.caminho)  # Embaralho a ordem dos valores.
    heapq.heappush(populacao, cromossomo)  # Adiciono o cromossomo(indivíduo) na pilha

print("\n",populacao)
print(len(populacao))
"""

populacao = []
tamanhoDaPopulacao = 50


"""Método cria os cromossomos iniciais.
   Para cada indivíduo adiciona no caminho(individuo) as cidades(genes).
   Depois embaralha essas cidades, gerando individuos diferentes e por  
   último coloca na população. Faz isso até o número máximo de individuos. 
   """
def geraPopulacao():
    global populacao

    for x in range(tamanhoDaPopulacao):
        cromossomo = Cromossomo()
        cromossomo.caminho = inicializadorDaPopulacao[:]
        random.shuffle(cromossomo.caminho) #Embaralho a ordem dos valores.
        heapq.heappush(populacao, cromossomo) #Adiciono o cromossomo(indivíduo) na pilha
    return populacao

""" TORNEIO: Seleciona um número K de indivíduos randomicamente e depois pega os dois de melhor fitness 
    para fazer o cruzamento e gerar um filho.
"""
def selecaoIndividuo(parametroPopulacao):
    valorRandomUm = random.randrange(tamanhoDaPopulacao//2) #Pega a primeira parte do vetor população. O // para arredondar o valor resultante da divisão.
    valorRandomDois = random.randrange(tamanhoDaPopulacao//2, tamanhoDaPopulacao) #Pega a segunda parte da população(vetor).

    #valorRandomTrês = random.randrange(tamanhoDaPopulacao//2, tamanhoDaPopulacao)
    #valorRandomQuatro = random.randrange(tamanhoDaPopulacao//2, tamanhoDaPopulacao)

    if parametroPopulacao[valorRandomUm].calculaFitness() < parametroPopulacao[valorRandomDois].calculaFitness():
        return parametroPopulacao[valorRandomUm]
    else:
        return parametroPopulacao[valorRandomDois]

""" OX1: A partir do primeiro pai pega-se uma parte do vetor(parte do gene) e coloca diretamnete no filho.
    Depois pegue um seguemento do segundo pai e coloco apenas os números que ainda não estão no filho e se faltar veja quais faltam.
        pai 1 -> 012|3456|789  : Filho -> 281|3456|970. 
        pai 2 -> 970|2814|356  :
"""
def crossoverIndividuo(individuoUm, individuoDois):
    global tamanhoDaPopulacao
    global tamanhoDaListaDeVertices

    listaNovosIndividuos = []
    contador = 0

    qtdGeracao = 20 #Número de interações.
    tamanhoCorte = int(tamanhoDaListaDeVertices * 0.95) #3

    """TESTES/TENTATIVAS DE MELHORAR 
    #posicaoCorteUm = random.randrange(0, (tamanhoDaPopulacao - 1) // 2)  # Primeira parte
    #posicaoCorteDois = random.randrange(((tamanhoDaPopulacao - 1) // 2) + 1, tamanhoDaPopulacao - 1)  # segunda parte
    #tamanhoCorte = (posicaoCorteDois - posicaoCorteUm)"""

    while contador < qtdGeracao :
        qtdGenesAdicionados = 0
        geneDosPaisParaFilho = individuoUm.caminho[:tamanhoCorte] #Pega de 0 até o tamanhoCorte

        #Vai adicionar os valores do segundo pai que n estão no filho ainda.
        for x in individuoDois.caminho:
            if (qtdGenesAdicionados == (tamanhoDaListaDeVertices - tamanhoCorte)):
                break
            if x not in geneDosPaisParaFilho:
                geneDosPaisParaFilho.append(x)
                qtdGenesAdicionados += 1

        """Poderia colocar a mutação separado, mas teri q fazer ela para todos os indivíduos da lista de curzamento."""
        geneDosPaisParaFilho = mutacaoIndividuo(geneDosPaisParaFilho)# Mutação pra que gere indivíduos diferentes e mantenha a diversidade

        novoIndividuo = Cromossomo()
        novoIndividuo.caminho = geneDosPaisParaFilho

        listaNovosIndividuos.append(novoIndividuo)

        contador += 1

    return listaNovosIndividuos

""" SWAP MUTATION: Escolhemos dois genes de um cromossomo e trocamos eles de lugares.
        1"2"345"6"78 -> 1"6"345"2"789
"""
def mutacaoIndividuo(caminhoDoNovoFilhoGerado):

    geneUm = random.randrange(tamanhoDaListaDeVertices - 1)
    geneDois = random.randrange(geneUm, tamanhoDaListaDeVertices - 1)

    caminhoDoNovoFilhoGerado[geneUm], caminhoDoNovoFilhoGerado[geneDois] = caminhoDoNovoFilhoGerado[geneDois], caminhoDoNovoFilhoGerado[geneUm]

    return caminhoDoNovoFilhoGerado

melhorSolucao = True
numeroTentativas = 0

""" ELITISMO: Eu pego os melhores indivíduos da nova lista e coloco no
    lugar dos piores da população.
"""
def atualizaPopulacao(parametroPopulacao, parametroListaDeNovosIndividuos):
    global melhorSolucao
    global numeroTentativas

    for x in parametroListaDeNovosIndividuos:
        individuoMaiorFitness = heapq.nlargest(1, parametroPopulacao)[0] #pego o pior fitness, nesse caso o maior.
        menor = parametroPopulacao[0]

        xFitness = x.calculaFitness()
        if(xFitness < individuoMaiorFitness.calculaFitness()):
            parametroPopulacao.remove(individuoMaiorFitness)
            heapq.heappush(parametroPopulacao, x)
            heapq.heapify(parametroPopulacao)

            if xFitness < menor.calculaFitness():
                numeroTentativas = 0 #Controla o número de vezes q o algoritmo vai rodar. Se eu ficar gerendo filhos piores ele para.
            else:
                numeroTentativas += 1
        else:
            numeroTentativas += 1

        if numeroTentativas == 700:
            melhorSolucao = False

    return parametroPopulacao

def obtemMenor(parametroPopulacao):
    return parametroPopulacao[0]

#---------------------------- ALGORITMO DE AG PROPRIAMENTE DITO ------------------------------------#

#Inicialiso a população
populacao = geraPopulacao()

while(melhorSolucao):

    #Avalio os indivíduos e faço a seleção.
    individuoUm = selecaoIndividuo(populacao)
    individuoDois = selecaoIndividuo(populacao)

    #Cruzamentos entre os individuos escolhidos. E no mesmo método faço a mutação do filho gerado
    #No método crossover eu gero um lista de novos indivíduos.
    novosIndividuosGerados = crossoverIndividuo(individuoUm, individuoDois)

    #Faço a avaliação do novo indivíduo e se valer a pena adiciono ele na população.
    populacao = atualizaPopulacao(populacao, novosIndividuosGerados)

aux = 1
for x in populacao:
    print(aux,"ª indivíduo:", x.caminho, " | Fitness:", x.calculaFitness(), "\n")
    aux = aux + 1

print("Melhor indivíduo:(Menor distância)", obtemMenor(populacao).calculaFitness())