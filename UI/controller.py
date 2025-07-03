import flet as ft

class Controller:

    def __init__(self, view, model):
        # The view, with the graphical elements of the UI
        self._view = view
        # The model, which implements the logic of the program and holds the data
        self._model = model
        # Altro
        self._choiceDDPartenza = None
        self._choiceDDArrivo = None

    def handleAnalizza(self, e):
        nMinTxt = self._view._txtCompMinime.value
        if nMinTxt == "":
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text("Inserire un valore numerico!"))
            self._view.update_page()
            return
        try:
            nMin = int(nMinTxt)
        except ValueError:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text("Inserire un valore numerico!"))
            self._view.update_page()
            return
        if nMin <= 0:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text("Inserire un valore numerico positivo!"))
            self._view.update_page()
            return
        self._model.buildGraph(nMin)
        allNodes = self._model.getAllNodes()
        self._fillDD(allNodes)
        nNodes, nEdges = self._model.getGraphDetails()
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text(f"Grafo correttamente creato."))
        self._view.txt_result.controls.append(ft.Text(f"Numero di nodi: {nNodes}."))
        self._view.txt_result.controls.append(ft.Text(f"Numero di archi: {nEdges}."))
        self._view.update_page()
        return

    def _fillDD(self, allNodes):
        for node in allNodes:
            self._view._ddAeroportoP.options.append(ft.dropdown.Option(key=node.IATA_CODE,
                                                                       data=node,
                                                                       on_click=self.pickDDPartenza))
            self._view._ddAeroportoA.options.append(ft.dropdown.Option(key=node.IATA_CODE,
                                                                       data=node,
                                                                       on_click=self.pickDDArrivo))

    def pickDDPartenza(self, e):
        self._choiceDDPartenza = e.control.data

    def pickDDArrivo(self, e):
        self._choiceDDArrivo = e.control.data

    def handleConnessi(self, e):
        if self._choiceDDPartenza == None:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text("Selezionare un aeroporto di partenza!"))
            self._view.update_page()
            return
        vicini = self._model.getSortedNeighbors(self._choiceDDPartenza)
        self._view.txt_result.controls.clear()
        self._view.txt_result.controls.append(ft.Text(f"Di seguito i vicini din {self._choiceDDPartenza}:"))
        for vicino in vicini:
            self._view.txt_result.controls.append(ft.Text(f"{vicino[0]}, peso: {vicino[1]}"))
        self._view.update_page()

    def handlePercorso(self, e):
        if self._choiceDDPartenza == None:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text("Selezionare un aeroporto di partenza!"))
            self._view.update_page()
            return
        if self._choiceDDArrivo == None:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text("Selezionare un aeroporto di arrivo!"))
            self._view.update_page()
            return
        path = self._model.getPath(self._choiceDDPartenza, self._choiceDDArrivo)
        if len(path) == 0:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text(f"Cammino fra {self._choiceDDPartenza} e {self._choiceDDArrivo} non trovato!"))
            self._view.update_page()
        else:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text(f"Cammino fra {self._choiceDDPartenza} e {self._choiceDDArrivo} trovato, di seguito i nodi:"))
            for p in path:
                self._view.txt_result.controls.append(ft.Text(f"{p}"))
            self._view.update_page()
        self._view.update_page()

    def handleCerca(self, e):
        pass