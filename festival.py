class Artista:
    def __init__(self, nombre, genero, popularidad):
        self.nombre = nombre
        self.genero = genero
        self.popularidad = popularidad

    def presentarse(self):
        print(f"Hola a todos, soy {self.nombre}, un artista de {self.genero} con una popularidad de {self.popularidad}/100.")

    def actuar(self):
        pass

    def despedirse(self):
        print(f"¡Muchas gracias por la energía, se despide {self.nombre}!")


class Cantante(Artista):
    def __init__(self, nombre, genero, popularidad, cancion_mas_popular):
        super().__init__(nombre, genero, popularidad)
        self.cancion_mas_popular = cancion_mas_popular

    def actuar(self):
        print(f"🎶 {self.nombre} canta su éxito {self.cancion_mas_popular} con gran energía.")


class DJ(Artista):
    def __init__(self, nombre, genero, popularidad, estilo):
        super().__init__(nombre, genero, popularidad)
        self.estilo = estilo

    def actuar(self):
        print(f"🎧 El DJ {self.nombre} mezcla temas de estilo {self.estilo}, haciendo vibrar al público.")


class Banda(Artista):
    def __init__(self, nombre, genero, popularidad, integrantes):
        super().__init__(nombre, genero, popularidad)
        self.integrantes = integrantes

    def actuar(self):
        print(f" La banda {self.nombre} con {self.integrantes} integrantes toca un poderoso solo de guitarra.")


def iniciar_festival(lista_artistas):
    print("\n" + "🎵" * 15 + " ¡COMIENZA EL FESTIVAL DE MÚSICA! " + "🎵" * 15 + "\n")
    
    for artista in lista_artistas:
        artista.presentarse()
        artista.actuar()
        artista.despedirse()
        print("\n Fin de la actuación \n" + "-" * 50)


def main():
    print("--- GESTOR DE FESTIVAL MUSICAL ---")
    
    try:
        cantidad = int(input("¿Cuántos artistas se presentarán en el festival? "))
    except ValueError:
        print("Error: Ingresa un número entero válido.")
        return

    lista_artistas = []

    for i in range(cantidad):
        print(f"\n--- Registro del Artista {i + 1} de {cantidad} ---")
        tipo = input("Tipo de artista (Cantante / DJ / Banda): ").strip().capitalize()
        nombre = input("Nombre: ").strip()
        genero = input("Género musical: ").strip()
        
        try:
            popularidad = int(input("Popularidad (entero del 1 al 100): "))
        except ValueError:
            popularidad = 50

        if tipo == "Cantante":
            cancion = input("Canción más popular: ").strip()
            artista = Cantante(nombre, genero, popularidad, cancion)
            lista_artistas.append(artista)
            
        elif tipo == "DJ":
            estilo = input("Estilo de mezcla: ").strip()
            artista = DJ(nombre, genero, popularidad, estilo)
            lista_artistas.append(artista)
            
        elif tipo == "Banda":
            try:
                integrantes = int(input("Número de integrantes: "))
            except ValueError:
                integrantes = 4
            artista = Banda(nombre, genero, popularidad, integrantes)
            lista_artistas.append(artista)
            
        else:
            print("Tipo de artista no reconocido. No se pudo agregar a este artista.")

    if lista_artistas:
        iniciar_festival(lista_artistas)
    else:
        print("\nNo hay artistas registrados para el festival.")

if __name__ == "__main__":
    main()