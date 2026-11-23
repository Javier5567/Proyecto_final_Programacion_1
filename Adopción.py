# Clase base (Padre)
class Animal:
    def __init__(self, id_mascota, nombre, edad, descripcion):
        self.id_mascota = id_mascota
        self.nombre = nombre
        self.edad = edad
        self.descripcion = descripcion

    def hacer_sonido(self):
        return "Sonido general"

    def mostrar_perfil(self):
        return f"[{self.id_mascota}] {self.nombre} ({self.edad} años) - {self.descripcion}"


# Clases derivadas (Hijas) aplicando Herencia
class Perro(Animal):
    def __init__(self, id_mascota, nombre, edad, descripcion, raza):
        super().__init__(id_mascota, nombre, edad, descripcion)
        self.raza = raza

    def hacer_sonido(self):
        return "¡Guau, guau!"

    def mostrar_perfil(self):
        base = super().mostrar_perfil()
        return f"{base} | Especie: Perro ({self.raza})"


class Gato(Animal):
    def __init__(self, id_mascota, nombre, edad, descripcion, color_pelaje):
        super().__init__(id_mascota, nombre, edad, descripcion)
        self.color_pelaje = color_pelaje

    def hacer_sonido(self):
        return "¡Miau!"

    def mostrar_perfil(self):
        base = super().mostrar_perfil()
        return f"{base} | Especie: Gato (Pelaje {self.color_pelaje})"


# --- Datos iniciales del catálogo ---
catalogo = [
    Perro(1, "Max", 2, "Muy juguetón y amigable con niños", "Labrador"),
    Gato(2, "Luna", 1, "Tranquila, ideal para apartamento", "Blanco y negro"),
    Perro(3, "Rocky", 4, "Protector y leal, ya está entrenado", "Pastor Alemán"),
    Gato(4, "Simba", 3, "Curioso y le encanta dormir al sol", "Naranja")
]

favoritos = []


# --- Menú interactivo ---
def menu():
    while True:
        print("\n--- CATÁLOGO DE ADOPCIÓN RESPONSABLE ---")
        print("1. Explorar todas las mascotas")
        print("2. Guardar mascota en favoritas")
        print("3. Ver mis mascotas favoritas")
        print("4. Salir")
        
        opcion = input("Elige una opción: ")

        if opcion == "1":
            print("\n--- MASCOTAS DISPONIBLES ---")
            for mascota in catalogo:
                # Aquí se aplica el polimorfismo al llamar los métodos
                print(mascota.mostrar_perfil())
                print(f"   Dice: {mascota.hacer_sonido()}\n")

        elif opcion == "2":
            try:
                id_buscado = int(input("\nIngresa el ID de la mascota que te gustó: "))
                encontrada = False
                for mascota in catalogo:
                    if mascota.id_mascota == id_buscado:
                        if mascota not in favoritos:
                            favoritos.append(mascota)
                            print(f"¡{mascota.nombre} fue agregada a tus favoritas!")
                        else:
                            print(f"{mascota.nombre} ya está en tu lista de favoritas.")
                        encontrada = True
                        break
                if not encontrada:
                    print("No se encontró ninguna mascota con ese ID.")
            except ValueError:
                print("Por favor, ingresa un número válido.")

        elif opcion == "3":
            print("\n--- MIS MASCOTAS FAVORITAS ---")
            if len(favoritos) == 0:
                print("Aún no tienes mascotas guardadas en favoritas.")
            else:
                for fav in favoritos:
                    print(fav.mostrar_perfil())

        elif opcion == "4":
            print("¡Gracias por apoyar la adopción responsable!")
            break
        else:
            print("Opción no válida. Intenta de nuevo.")

# Ejecutar el programa
if __name__ == "__main__":
    menu()
