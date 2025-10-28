from database.DB_connect import get_connection
from model.automobile import Automobile
from model.noleggio import Noleggio
from UI.alert import AlertManager

'''
    MODELLO: 
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Interagisce con il database
'''

class Autonoleggio:
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

    def get_automobili(self) -> list[Automobile] | None:
        """
            Funzione che legge tutte le automobili nel database
            :return: una lista con tutte le automobili presenti oppure None
        """
        cnx = get_connection()
        if cnx is None:
            print("Database connection failed")
            return None

        cursor = cnx.cursor(dictionary=True)
        query = """SELECT * FROM automobile"""
        cursor.execute(query)
        lista_automobili = []
        row = cursor.fetchone()
        while row is not None:
            lista_automobili.append(Automobile(row['codice'],
                                        row['marca'],
                                        row['modello'],
                                        row['anno'],
                                        row['posti'],
                                        row["disponibile"]))
            row = cursor.fetchone()
        cursor.close()
        cnx.close()
        return lista_automobili


    def cerca_automobili_per_modello(self, modello) -> list[Automobile] | None:
        """
            Funzione che recupera una lista con tutte le automobili presenti nel database di una certa marca e modello
            :param modello: il modello dell'automobile
            :return: una lista con tutte le automobili di marca e modello indicato oppure None
        """
        cnx = get_connection()
        if cnx is None:
            print("Database connection failed")
            return None


        cursor = cnx.cursor(dictionary=True)
        query = """SELECT * 
                   FROM automobile
                   WHERE modello = %s"""
        cursor.execute(query, (modello,))
        lista_automobili_cercate = []
        row = cursor.fetchone()
        while row is not None:
            lista_automobili_cercate.append(Automobile(row['codice'],
                                               row['marca'],
                                               row['modello'],
                                               row['anno'],
                                               row['posti'],
                                               row["disponibile"]))
            row = cursor.fetchone()
        cursor.close()
        cnx.close()
        return lista_automobili_cercate
