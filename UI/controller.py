import flet as ft
from UI.view import View
from model.model import Autonoleggio

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view : View, model : Autonoleggio):
        self._model = model
        self._view = view

    def get_nome(self):
        return self._model.nome

    def get_responsabile(self):
        return self._model.responsabile

    def set_responsabile(self, responsabile):
        self._model.responsabile = responsabile

    def conferma_responsabile(self, e):
        self._model.responsabile = self._view.input_responsabile.value
        self._view.txt_responsabile.value = f"Responsabile: {self._model.responsabile}"
        self._view.update()

# Altre Funzioni Event Handler
    def handlerMostra(self, e):

        if self._model.get_automobili() is None:
            self._view.show_alert("⚠️ Impossibile stabilire connessione con il Database")
            exit("Impossibile connettersi al Database")

        for auto in self._model.get_automobili():
            self._view.lista_auto.controls.append(ft.Text(f'{auto}'))
        self._view.update()

    def handlerCerca(self, e):
        # Svuota la listView della ricerca
        self._view.lista_auto_ricerca.controls.clear()

        # Legge il valore del textfield modello
        modello = self._view.input_modello_auto.value.strip()

        # Controllo input vuoto
        if modello == "":
            self._view.show_alert("Inserire un modello da cercare.")
            self._view.update()
            return

        # Chiamata al modello
        automobili = self._model.cerca_automobili_per_modello(modello)

        # Nessun risultato
        if automobili is None or len(automobili) == 0:
            self._view.show_alert(f"Nessuna automobile trovata con modello '{modello}'.")
            self._view.update()
            return

        # Mostra i risultati
        for auto in automobili:
            self._view.lista_auto_ricerca.controls.append(
                ft.Text(f"{auto.codice} - {auto.marca} {auto.modello} ({auto.anno}) - Posti: {auto.posti}")
            )

        # Aggiorna la view
        self._view.update()