'''
1. Criar uma classe "no" para criar objetos com informacoes como o no-pai, posicao e custo
2. Definir uma funcao rota que retorne o caminho do Inicio ao Objetivo
3.1. Inicializar variaveis
3.2. Adicionar no de Inicio a lista de vizinhos-nao-visitados. Definir uma condicao de parada. Definir movimento em termos de posicao relativa
3.3. Procurar pelo no de menor custo na lista. Esse no se torna o no atual. Checar se chegou ao limite de iteracoes.
3.4. Checar se o no atual e o mesmo no Objetivo.
3.5. Usar o no atual e checar 4 nos adjacentes para atualizar nos-filhos. Se for imovel ou ja visitado, ignorar.
Senao, criar no novo com o pai como o no atual e atualizar posicao do no.
3.6. Checar todos os nos-filhos para saber:
    - Se nao estiver na lista de "vizinhos nao-visitados" adicionar a essa lista. Tornar o no atual o pai desse no. Gravar o f, g e h do no.
    - Se estiver na lista "vizinhos nao-visitados" checar se a rota ate aquele no e melhor usando g como medida. Um g menor indica rota melhor.
    Se "sim", mudar o pai do no para o no atual e recalcular g e f daquele no.
4. Programa principal:
'''
#import cv2
import numpy as np

class No:
    def __init__(self, pai=None, posicao=None): #inicia um no com seus atributos
        self.pai = pai
        self.pos = posicao

        self.g = 0
        self.h = 0
        self.f = 0
    def __igual__(self, outro): #verifica se um no e igual a outro
        return(self.pos == outro.pos)

def retornar_rota(no_atual,labirinto):
    rota = []
    nLinhas, nColunas = np.shape(labirinto) #cria matriz nas dimensoes definidas no labirinto
    #cria labirinto resultante com -1 em cada posicao
    result = [[-1 for i in range(nColunas)] for j in range(nLinhas)]
    atual = no_atual
    while atual is not None:
        rota.append(atual.pos)
        atual = atual.pai
    #retorna rota inversa ja que precisamos dela do inicio ao obj
    rota = rota[::-1]
    vInicio = 0
    #atualiza a rota do inicio ao objetivo encontrada pela busca A* com cada passo +1
    for i in range(len(rota)):
        result[rota[i][0]][rota[i][1]] = vInicio
        vInicio+=1
    return(result)

    #Retorna uma lista de tuplas do inicio ao objetivo no labirinto informados
def busca(labirinto, custo, inicio, fim):
    #inicializa nos de inicio e objetivo com 0 em g, h e f
    no_inicio = No(None, tuple(inicio))
    no_inicio.g = no_inicio.h = no_inicio.f = 0
    no_obj = No(None,tuple(fim))
    no_obj.g = no_obj.h = no_obj.f = 0

    vizinhos_nv = []    #lista de nos vizinhos nao visitados
    visitados = []
    vizinhos_nv.append(no_inicio)

    #cria condicao de parada.
    iteracoes = 0
    max_iter = (len(labirinto)//2) **10 #metade do tamanho do labirinto elevado a 10

    #busca nos 4 nos vizinhos (acima, a esq, abaixo e a dir)
    mover = [[-1,0],    #pra cima
            [0,-1],     #pra esq
            [1,0],      #pra baixo
            [0,1]]      #pra dir

    #usa o no atual para comparar todos os f e selecionar o menor. Checa iteracao maxima
    #descobre quantas linhas e colunas o labirinto tem
    nLinhas, nColunas = np.shape(labirinto)

    while(len(vizinhos_nv)>0):
        iteracoes += 1

        no_atual = vizinhos_nv[0]
        indAtual = 0
        for ind, item in enumerate(vizinhos_nv):
            if item.f < no_atual.f:
                no_atual = item
                indAtual = ind
        if iteracoes > max_iter:
            print("alcancado limite de iteracoes!")
            return(retornar_rota(no_atual,labirinto))

        vizinhos_nv.pop(indAtual)
        visitados.append(no_atual)

        if no_atual == no_obj:
            return(retornar_rota(no_atual,labirinto))

    filhos = []

    for nova in mover:
        posNo = (no_atual.pos[0] + nova[0], no_atual.pos[1] + nova[1])

        if(posNo[0] > (nLinhas-1) or
            posNo[0] < 0 or
            posNo[1] > (nColunas-1) or
            posNo[1] < 0):
            continue
        if labirinto[posNo[0]][posNo[1]] != 0:
            continue
        novoNo = No(no_atual, posNo)

        filhos.append(novoNo)

    for filho in filhos:
        if len([filho_vis for filho_vis in visitados if filho_vis == filho]) > 0:
            continue

        filho.g = no_atual.g + custo
        filho.h = (((filho.pos[0] - no_obj.pos[0])**2)+
                    ((filho.pos[1] - no_obj.pos[1])**2))
        filho.f = filho.g + filho.h

        if len([i for i in vizinhos_nv if filho == i and filho.g > i.g]) > 0:
            continue
        vizinhos_nv.append(filho)

if __name__ == '__main__':
    labirinto = [[0,1,0,0,0,0],
                [0,0,0,0,0,0],
                [0,1,0,1,0,0],
                [0,1,0,0,1,0],
                [0,0,0,0,1,0]]

    inicio = [0,0]
    obj = [4,5]
    custo = 1

    rota = busca(labirinto,custo,inicio,obj)
    print(rota)
