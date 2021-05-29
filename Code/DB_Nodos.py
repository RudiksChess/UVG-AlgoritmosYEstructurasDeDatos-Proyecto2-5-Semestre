def creador_nodos_individuales(ID, categoria):
    comando: str = f"({ID.lower()}:{categoria.capitalize()} {{nombre:\"{ID.lower()}\"}})"
    return comando


def lista_nodos(lista, categoria):
    nodos = []
    for elemento in lista:
        nodos.append(creador_nodos_individuales(elemento, categoria))
    return nodos


def crear_relacion(usuario, categoria, relacion, nodo):
    query = f"MATCH ({usuario}:User {{nombre:\"{usuario}\"}}), ({nodo}:{categoria} {{nombre:\"{nodo}\"}}) CREATE ({usuario})-[:{relacion}]->({nodo})"
    return query


class Nodos:
    def __init__(self):
        self.nodos = []
        self.USERS = ["user001", "user002", "user003", "user004", "user005", "user006", "user007", "user008", "user009",
                      "user010",
                      "user011", "user012", "user013", "user014", "user015", "user016", "user017", "user018", "user019",
                      "user020",
                      "user021", "user022", "user023", "user024"]
        self.NIVEL = ["Principiante", "Intermedio", "Avanzado"]
        self.PLATAFORMA = ["Chess", "Lichess", "Chess24"]
        self.APERTURA = ["Italiana_Espanola", "Inglesa", "Sistema_Londres", "Fianchetto"]
        self.DEFENSA = ["Eslava", "Francesa", "Caro_Kann", "Siciliana"]
        self.PARTE_FAVORITA = ["Apertura", "Medio", "Final"]
        self.CATEGORIAS = ["User", "Nivel", "Plataforma", "Apertura", "Defensa", "Favorito"]
        self.RELACIONES = ["NIVEL_BLITZ", "NIVEL_RAPIDAS", "PARTE_FAVORITA", "PLATAFORMA", "APERTURA",
                           "DEFENSA"]
    def creador_nodos(self):
        nodos_user = lista_nodos(self.USERS, self.CATEGORIAS[0])
        nodos_nivel = lista_nodos(self.NIVEL, self.CATEGORIAS[1])
        nodos_plataforma = lista_nodos(self.PLATAFORMA, self.CATEGORIAS[2])
        nodos_apertura = lista_nodos(self.APERTURA, self.CATEGORIAS[3])
        nodos_defensa = lista_nodos(self.DEFENSA, self.CATEGORIAS[4])
        nodos_favorito = lista_nodos(self.PARTE_FAVORITA, self.CATEGORIAS[5])

        self.nodos.append(nodos_user)
        self.nodos.append(nodos_nivel)
        self.nodos.append(nodos_plataforma)
        self.nodos.append(nodos_apertura)
        self.nodos.append(nodos_defensa)
        self.nodos.append(nodos_favorito)

        comando_nodos: str = "CREATE \n"

        for lista in self.nodos:
            for elemento in lista:
                comando_nodos += elemento + ",\n"
        return comando_nodos[:-2]

    def crear_relacion_individual(self, lista):
        lista = lista.split(",")
        nuevo = []
        for elemento in lista:
            l = elemento.lower()
            nuevo.append(l)
        lista = nuevo

        # user003,Principiante,Principiante,Final,Chess,Italiana_Espanola,Francesa
        match_nivel_blitz = crear_relacion(lista[0], self.CATEGORIAS[1], self.RELACIONES[0], lista[1])
        match_nivel_rapidas = crear_relacion(lista[0], self.CATEGORIAS[1], self.RELACIONES[1], lista[2])
        match_parte_favorita = crear_relacion(lista[0], self.CATEGORIAS[5], self.RELACIONES[2], lista[3])
        match_plataforma = crear_relacion(lista[0], self.CATEGORIAS[2], self.RELACIONES[3], lista[4])
        match_apertura = crear_relacion(lista[0], self.CATEGORIAS[3], self.RELACIONES[4], lista[5])
        match_defensa = crear_relacion(lista[0], self.CATEGORIAS[4], self.RELACIONES[5], lista[6])
        relaciones = [match_nivel_blitz, match_nivel_rapidas, match_parte_favorita, match_plataforma, match_apertura, match_defensa]
        return relaciones


    def relacions_DB_total(self):
        with open("Datos.csv") as DB:
            lista = [linea.split() for linea in DB]
            lista.pop(0)

            relaciones = []
            for lista_inside in lista:
                for strings in lista_inside:
                    relaciones.append(self.crear_relacion_individual(strings))

        return relaciones

