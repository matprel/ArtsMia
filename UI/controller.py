import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handleAnalizzaOggetti(self, e):
        self._view.txt_result.controls.clear()
        self._model.buildGraph()
        self._view.txt_result.controls.append(ft.Text("Grafo creato correttamente!"))
        self._view.txt_result.controls.append(ft.Text(f"Il grafo ha {self._model.getNumNodes()} nodi."))
        self._view.txt_result.controls.append(ft.Text(f"Il grafo ha {self._model.getNumEdges()} archi."))
        self._view.update_page()

    def handleCompConnessa(self,e):
        idAggiunto = self._view._txtIdOggetto.value
        try:
            intId = int(idAggiunto)
        except ValueError:
            self._view.txt_result.controls.clear()
            self._view.txt_result.controls.append(ft.Text(f"Il valore inserito non è un intero."))
            self._view.update_page()
            return

        if self._model.verificaID(intId):
            self._view.txt_result.controls.append(ft.Text(f"L'oggetto {intId} è presente nel grafo."))
        else:
            self._view.txt_result.controls.append(ft.Text(f"L'oggetto {intId} non è presente nel grafo."))

        numConnessa = self._model.cercaConnessa(intId)
        self._view.txt_result.controls.append(ft.Text(f"La componente connessa che contiene {intId} ha dimensione {numConnessa}."))
        self._view.update_page()

