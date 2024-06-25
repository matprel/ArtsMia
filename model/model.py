import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self._allOggetti = DAO.getAllOggetti()
        self._idMap ={}
        for o in self._allOggetti:
            self._idMap[o.object_id] = o


    def buildGraph(self):
        self._grafo = nx.Graph()
        self._grafo.add_nodes_from(self._allOggetti)
        edges = DAO.getEdges(self._idMap)
        for e in edges:
            print(e)
            self._grafo.add_edge(e.o1, e.o2, weight=e.peso)


    def cercaConnessa(self, idOggetto):
        nodoSorgente = self._idMap[idOggetto]
        connessi = nx.node_connected_component(self._grafo, nodoSorgente)
        num = len(connessi)
        return num

    def verificaID(self, idOggetto):
        return idOggetto in self._idMap

    def getNumNodes(self):
        return len(self._allOggetti)

    def getNumEdges(self):
        return len(self._grafo.edges)
