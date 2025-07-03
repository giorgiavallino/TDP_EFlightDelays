import networkx as nx
from database.DAO import DAO

class Model:

    def __init__(self):
        self._graph = nx.Graph()
        self._idMapAirports = {}
        self._airports = DAO.getAllAirports()
        for airport in self._airports:
            self._idMapAirports[airport.ID] = airport

    def buildGraph(self, nMin):
        nodes = DAO.getAllNodes(nMin, self._idMapAirports)
        self._graph.add_nodes_from(nodes)
        self.addEdges_02()
        print(f"Numero nodi: {len(self._graph.nodes)}, numero archi: {len(self._graph.edges)}")

    def addEdges_01(self):
        allEdges = DAO.getAllEdges_01(self._idMapAirports)
        for edge in allEdges:
            if edge.aeroportoP in self._graph and edge.aeroportoA in self._graph:
                if self._graph.has_edge(edge.aeroportoP, edge.aeroportoA):
                    self._graph[edge.aeroportoP][edge.aeroportoA]["weight"] += edge.peso
                else:
                    self._graph.add_edge(edge.aeroportoP, edge.aeroportoA, weight=edge.peso)

    def addEdges_02(self):
        allEdges = DAO.getAllEdges_02(self._idMapAirports)
        for edge in allEdges:
            if edge.aeroportoP in self._graph and edge.aeroportoA in self._graph:
                self._graph.add_edge(edge.aeroportoP, edge.aeroportoA, weight=edge.peso)

    def getGraphDetails(self):
        return self._graph.number_of_nodes(), self._graph.number_of_edges()

    def getAllNodes(self):
        nodes = list(self._graph.nodes)
        nodes.sort(key=lambda x: x.IATA_CODE)
        return nodes

    def getSortedNeighbors(self, node):
        neighbors = self._graph.neighbors(node) # equivalente a self._graph[node]
        neighbTuples = []
        for neighbor in neighbors:
            neighbTuples.append((neighbor, self._graph[node][neighbor]["weight"]))
        neighbTuples.sort(key=lambda x: x[1], reverse=True)
        return neighbTuples

    def getPath(self, nodoIniziale, nodoFinale):
        path = nx.dijkstra_path(self._graph, nodoIniziale, nodoFinale) # si può aggiungere l'attributo weight=None
        # per ottenere il percorso più corto
        # Si possono usare anche altri metodi come nx.shortest_path(self._graph, nodoIniziale, nodoFinale),...
        return path