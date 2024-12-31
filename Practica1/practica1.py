import tkinter as tk
from tkinter import messagebox

# Asumimos que tienes las clases Programa1, Programa2, Programa3 definidas en otro archivo
class Programa1:
    def ejecutar(self):
        print("Ejecutando Programa 1")

class Programa2:
    def ejecutar(self):
        print("Ejecutando Programa 2")

class Programa3:
    def ejecutar(self):
        print("Ejecutando Programa 3")

class Menu:
    def __init__(self, root):
        self.root = root
        self.root.title("Menú Principal")
        
        # Inicializamos los programas
        self.programas = {
            "1": Programa1(),
            "2": Programa2(),
            "3": Programa3()
        }

        # Crear widgets para el formulario de login
        self.etiqueta_rol = tk.Label(root, text="Seleccione su rol:", font=("Arial", 14))
        self.etiqueta_rol.pack(pady=20)

        # Botones para seleccionar el rol
        self.boton_admin = tk.Button(root, text="Administrador", width=20, height=2, command=self.seleccionar_admin)
        self.boton_admin.pack(pady=10)

        self.boton_inv = tk.Button(root, text="Investigador", width=20, height=2, command=self.seleccionar_investigador)
        self.boton_inv.pack(pady=10)

    def seleccionar_admin(self):
        self.mostrar_menu("Administrador")

    def seleccionar_investigador(self):
        self.mostrar_menu("Investigador")

    def mostrar_menu(self, rol):
        # Limpiar la ventana
        for widget in self.root.winfo_children():
            widget.destroy()

        # Mostrar el menú según el rol seleccionado
        if rol == "Administrador":
            self.mostrar_menu_admin()
        elif rol == "Investigador":
            self.mostrar_menu_investigador()

    def mostrar_menu_admin(self):
        tk.Label(self.root, text="Menú Administrador", font=("Arial", 16)).pack(pady=20)

        # Opciones para Administrador
        boton_ordenador = tk.Button(self.root, text="Probar clase Ordenador", command=self.ejecutar_programa_1)
        boton_ordenador.pack(pady=10)

        boton_ordenador_lista = tk.Button(self.root, text="Probar clase Ordenador Lista", command=self.ejecutar_programa_2)
        boton_ordenador_lista.pack(pady=10)

        boton_ordenador_agenda = tk.Button(self.root, text="Probar clase Ordenador Agenda", command=self.ejecutar_programa_3)
        boton_ordenador_agenda.pack(pady=10)

        boton_salir = tk.Button(self.root, text="Cerrar Sesión", command=self.cerrar_sesion)
        boton_salir.pack(pady=10)

    def mostrar_menu_investigador(self):
        tk.Label(self.root, text="Menú Investigador", font=("Arial", 16)).pack(pady=20)

        # Opciones para Investigador (limitadas)
        boton_ordenador = tk.Button(self.root, text="Probar clase Ordenador", command=self.ejecutar_programa_1)
        boton_ordenador.pack(pady=10)

        boton_salir = tk.Button(self.root, text="Cerrar Sesión", command=self.cerrar_sesion)
        boton_salir.pack(pady=10)

    def ejecutar_programa_1(self):
        self.programas["1"].ejecutar()

    def ejecutar_programa_2(self):
        self.programas["2"].ejecutar()

    def ejecutar_programa_3(self):
        self.programas["3"].ejecutar()

    def cerrar_sesion(self):
        # Limpiar la ventana y mostrar la pantalla de login de nuevo
        for widget in self.root.winfo_children():
            widget.destroy()
        # Crear los botones de login nuevamente
        self.__init__(self.root)  # Re-inicializa el login


# Función principal que configura la ventana de Tkinter
def main():
    root = tk.Tk()
    menu = Menu(root)
    root.mainloop()

# Llamamos a la función principal
if __name__ == "__main__":
    main()
