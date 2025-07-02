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
        self.addEdges_01()
        print(f"Numero nodi: {len(self._graph.nodes)}, numero archi: {len(self._graph.edges)}")

    def addEdges_01(self):
        allEdges = DAO.getAllEdges_01(self._idMapAirports)
        for edge in allEdges:
            if edge.aeroportoP in self._graph and edge.aeroportoA in self._graph:
                if self._graph.has_edge(edge.aeroportoP, edge.aeroportoA):
                    self._graph[edge.aeroportoP][edge.aeroportoA]["weight"] += edge.peso
                else:
                    self._graph.add_edge(edge.aeroportoP, edge.aeroportoA, weight=edge.peso)