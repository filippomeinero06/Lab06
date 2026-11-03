import flet as ft
from UI.view import View
from model.model import DepositoStrumenti

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: DepositoStrumenti):
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
    def mostra_strumenti(self, e):
        self._view.lista_strumenti.controls.clear()

        strumenti = self._model.get_strumenti()   # restituisce una lista di oggetti di tipo Strumento

        if strumenti is not None:
            for s in strumenti:
                self._view.lista_strumenti.controls.append(ft.Text(f"{s}"))

        else:
            self._view.show_alert("Non sono presenti strumenti nel database")

    def cerca_strumento_tipo(self, e):
        self._view.lista_strumenti_ricerca.controls.clear()

        tipo = self._view.input_tipo_strumento.value.strip()

        if not tipo:
            self._view.show_alert("Inserisci il tipo di strumento")
            return

        # controllo che il tipo di strumento non sia un intero, altrimento mostro l'alert
        try:
            _ = int(tipo)
            self._view.show_alert("❌ Il tipo da ricercare deve essere una stringa")
            return

        except ValueError:
            strumenti = self._model.cerca_strumenti_per_tipo(tipo) # restituisce una lista di oggetti di tipo Strumento

            if strumenti is not None:
                for s in strumenti:
                    self._view.lista_strumenti_ricerca.controls.append(ft.Text(f"{s}"))
            else:
                self._view.show_alert(f"Non sono presenti strumenti di tipo: '{tipo}'")


