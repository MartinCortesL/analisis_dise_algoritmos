#dijkstra
import heapq
import time

#clase grafo
class Grafo:
    # constructor
    def __init__(self):
        self.grafo={}
    # agregar vertice  
    def agregar_vertice(self,vertice):
        if self.grafo == None:
            self.grafo[vertice]={}
        else:
            if vertice not in self.grafo:
                self.grafo[vertice]={}
            else:
               print(f'{vertice} es un vertice repetido')
            
    #agregar peso a las aristas
    def agregar_arista(self,inicio,final,peso):
        if inicio and final not in self.grafo:
            self.agregar_vertice(inicio)
            self.agregar_vertice(final)
            self.grafo[inicio][final]=peso
        else:
            self.grafo[inicio][final]=peso
            
def diji (graph, ini):
    distancias = {vertice: 9999 for vertice in graph} 
    distancias[ini]=0
    cola=[(0,ini)]
    while cola:
        dActual, vActual = heapq.heappop(cola)
        if dActual > distancias[vActual] and distancias[vActual] != 9999:
            continue
        for vecino, peso in graph[vActual].items():
            distancia = dActual + peso
            if distancias[vecino] == 9999 or distancia < distancias[vecino]:
                distancias[vecino] = distancia
                heapq.heappush(cola, (distancia, vecino))

    return distancias

def tiempos(f):
    start=time.time()
    funcion=f
    end=time.time()
    ejecucion=end-start
    return ejecucion
     
               
          
g = Grafo()
g.agregar_vertice("a")
g.agregar_vertice("b")
g.agregar_vertice("c")
g.agregar_vertice("d")
g.agregar_vertice("e")
g.agregar_arista("a","b",10)
g.agregar_arista("a","c",3)
g.agregar_arista("b","c",1)
g.agregar_arista("b","d",2)
g.agregar_arista("c","b",4)
g.agregar_arista("c","d",8)
g.agregar_arista("c","e",2)
g.agregar_arista("d","e",7)
g.agregar_arista("e","d",9)

print(g.grafo)
inicio="a"
d=diji(g.grafo,inicio)
print(f"distancias minimas desde {inicio}")
for vertice, distancia in d.items():
    print(f"{vertice}: {distancia}")
print('Tiempo de ejecucion: ',tiempos(d))