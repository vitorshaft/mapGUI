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
import cv2
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
    result = [[-1 for i in range(nColunas)] for j in range(nLinhas)]
    atual = no_atual
    while atual is not None:
        rota.append(atual.pos)
        atual = atual.pai
    rota = rota[::-1]
    vInicio = 0
    for i in range(len(rota)):
        result[rota[i][0]][rota[i][1]] = vInicio
        vInicio+=1
    return(result)
def busca(labirinto, custo, inicio, fim):
    
