from abc import ABC, abstractmethod

class Programa(ABC):
    @abstractmethod
    def ejecutar(self):
        """Este método debe ser implementado por las subclases."""
        pass

class Programa1(Programa):
    """Programa 1: Variables, expresiones y estructuras de control."""

    def _max(self, numeros):
        max_val = numeros[0]
        for num in numeros:
            if num > max_val:
                max_val = num
        return max_val

    def _min(self, numeros):
        min_val = numeros[0]
        for num in numeros:
            if num < min_val:
                min_val = num
        return min_val

    def _suma(self, numeros):
        total = 0
        for num in numeros:
            total += num
        return total

    def _promedio(self, numeros):
        suma = self._suma(numeros)
        return suma / len(numeros) if len(numeros) > 0 else 0

    def ejecutar(self):
        print("\nPrograma 1 - Variables, expresiones y estructuras de control")
        try:
            n = int(input("Ingrese la cantidad de números que desea ingresar: "))
            numeros = []
            for i in range(n):
                num = int(input(f"Ingrese el número {i + 1}: "))
                numeros.append(num)
            
            max_val = self._max(numeros)
            min_val = self._min(numeros)
            suma = self._suma(numeros)
            promedio = self._promedio(numeros)
            
            print(f"Valor máximo: {max_val}")
            print(f"Valor mínimo: {min_val}")
            print(f"Suma: {suma}")
            print(f"Promedio: {promedio:.2f}")
        except ValueError:
            print("Por favor, ingrese valores válidos.")


class Programa2(Programa):
    """Programa 2: Archivos y cadenas."""

    def contar_palabra(self, texto, palabra):
        """Cuenta las apariciones exactas de una palabra en el texto."""
        palabras = texto.lower().split()  # Divide el texto en palabras y pasa a minúsculas
        contador = 0
        for palabra_actual in palabras:
            # Comparar palabra actual eliminando posibles signos de puntuación
            palabra_limpia = palabra_actual.strip(".,:;!?()[]{}\"'")
            if palabra_limpia == palabra:
                contador += 1
        return contador
    
    def ejecutar(self):
        print("\nPrograma 2 - Archivos y cadenas")
        palabra = str(input("Ingrese la palabra a buscar: "))
        try:
            archivo = "./test_pr2.txt"
            with open(archivo, "r", encoding="utf-8") as f:
                contenido = f.read()

            repeticiones = self.contar_palabra(contenido, palabra)
            
            print(f"La palabra '{palabra}' se repite {repeticiones} veces en el archivo.")
        except FileNotFoundError:
            print("No se encontró el archivo test_pr2.txt. Asegúrese de colocarlo en el mismo directorio que este programa.")


class Programa3(Programa):
    """Programa 3: Tablas y diccionarios."""

    def ejecutar(self):
        print("\nPrograma 3 - Tablas y diccionarios")
        usuarios = {
            "Juan1223": "J12an*.",
            "Maria2345": "M23a*.",
            "Pablo1459": "P14o*.",
            "Ana3456": "A34a*."
        }
        intentos = 0
        while intentos < 3:
            print(f"\nTiene {3 - intentos} intentos")
            usuario = input("Ingrese su nombre de usuario: ")
            contrasena = input("Ingrese su contraseña: ")
            if usuario in usuarios and usuarios[usuario] == contrasena:
                print("Acceso permitido")
                return
            else:
                intentos += 1
                print("\nDatos incorrectos")
        
        print("\n ** Lo siento, su acceso no es permitido **")


class Menu:
    """Clase para manejar el menú principal."""

    def __init__(self):
        self.programas = {
            "1": Programa1(),
            "2": Programa2(),
            "3": Programa3()
        }

    def mostrar_menu(self):
        while True:
            print("\n--- Menú Principal ---")
            print("1. Programa 1 - Variables, expresiones y estructuras de control")
            print("2. Programa 2 - Archivos y cadenas")
            print("3. Programa 3 - Tablas y diccionarios")
            print("0. Salir")
            
            opcion = input("Seleccione el programa que desea ejecutar (0-3): ")
            
            if opcion == "0":
                print("Saliendo del programa.")
                break
            elif opcion in self.programas:
                self.programas[opcion].ejecutar()
            else:
                print("Opción no válida. Por favor, seleccione una opción del 0 al 3.")


# Iniciar el programa
if __name__ == "__main__":
    menu = Menu()
    menu.mostrar_menu()