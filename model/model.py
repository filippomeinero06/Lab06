from database.DB_connect import get_connection
from model.strumento import Strumento
from model.prestito import Prestito

'''
    MODELLO:
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Interagisce con il database
'''

class DepositoStrumenti:
    def __init__(self, nome, responsabile):
        self._nome = nome
        self._responsabile = responsabile

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    @property
    def responsabile(self):
        return self._responsabile

    @responsabile.setter
    def responsabile(self, responsabile):
        self._responsabile = responsabile

    def get_strumenti(self) -> list[Strumento] | None:
        """
            Funzione che legge tutti gli strumenti nel database
            :return: una lista con tutti gli strumenti presenti oppure None
        """
        lista_strumenti = []

        conn = get_connection()
        cursor = conn.cursor()
        query = "SELECT * FROM strumento;"
        cursor.execute(query)
        righe = cursor.fetchall()
        conn.close()

        if len(righe) > 0:
            for riga in righe:
                codice = riga[0]
                tipo = riga[1]
                marca = riga[2]
                anno_acquisto = riga[3]
                valore = riga[4]
                disponibile = int(riga[5])
                if disponibile == 1:
                    disponibile = False
                else:
                    disponibile = True
                lista_strumenti.append(Strumento(codice, tipo, marca, anno_acquisto, valore, disponibile))
        else:
            lista_strumenti = None

        return lista_strumenti


    def cerca_strumenti_per_tipo(self, tipo) -> list[Strumento] | None:
        """
            Funzione che recupera una lista con tutti gli strumenti presenti nel database di un certo tipo
            :param tipo: il tipo dello strumento (es. "Chitarra")
            :return: una lista con tutti gli strumenti del tipo indicato oppure None
        """
        # TODO
