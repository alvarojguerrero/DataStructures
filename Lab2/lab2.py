from abc import ABC, abstractmethod

class Programa(ABC):
    @abstractmethod
    def ejecutar(self):
        pass

class Fecha:
    def __init__(self, dd: int = 0, mm: int = 0, aa: int = 0):
        self.dd = dd
        self.mm = mm
        self.aa = aa

    def setDia(self, dd: int):
        self.dd = dd

    def setMes(self, mm: int):
        self.mm = mm

    def setA(self, aa: int):
        self.aa = aa

    def getDia(self) -> int:
        return self.dd

    def getMes(self) -> int:
        return self.mm

    def getA(self) -> int:
        return self.aa

    def __str__(self):
        return f"{self.dd}-{self.mm}-{self.aa}"

class Direccion:
    def __init__(self, ciudad: str = "", edificio: str = "", apto: str = "", calle: str = "", nomenclatura: str = "", barrio: str = ""):
        self.calle = calle
        self.nomenclatura = nomenclatura
        self.barrio = barrio
        self.ciudad = ciudad
        self.edificio = edificio
        self.apto = apto

    def getCalle(self) -> str:
        return self.calle
        
    def setCalle(self, calle: str):
        self.calle = calle

    def setNomenclatura(self, nomenclatura: str):
        self.nomenclatura = nomenclatura

    def setBarrio(self, barrio: str):
        self.barrio = barrio

    def setCiudad(self, ciudad: str):
        self.ciudad = ciudad

    def setEdificio(self, edificio: str):
        self.edificio = edificio

    def setApto(self, apto: str):
        self.apto = apto

    def getNomenclatura(self) -> str:
        return self.nomenclatura

    def getBarrio(self) -> str:
        return self.barrio

    def getCiudad(self) -> str:
        return self.ciudad

    def getEdificio(self) -> str:
        return self.edificio

    def getApto(self) -> str:
        return self.apto

    def __str__(self):
        return f"Calle {self.calle} # {self.nomenclatura}, Edificio: {self.edificio}: Apto {self.apto}, Barrio: {self.barrio}, {self.ciudad}." 

class Usuario:
    def __init__(self, nombre: str = "", id: int = 0, fecha_nacimiento: Fecha = None, ciudad_nacimiento: str = "", tel: int = 0, email: str = "", dir: Direccion = None):
        self.nombre = nombre
        self.id = id
        self.fecha_nacimiento = fecha_nacimiento
        self.ciudad_nacimiento = ciudad_nacimiento
        self.tel = tel
        self.email = email
        self.dir = dir

    def setNombre(self, nombre: str):
        self.nombre = nombre

    def setId(self, id: int):
        self.id = id

    def setFecha_nacimiento(self, fecha_nacimiento: Fecha):
        self.fecha_nacimiento = fecha_nacimiento

    def setCiudad_nacimiento(self, ciudad_nacimiento: str):
        self.ciudad_nacimiento = ciudad_nacimiento

    def setTel(self, tel: int):
        self.tel = tel

    def setEmail(self, email: str):
        self.email = email

    def setDir(self, dir: Direccion):
        self.dir = dir

    def getNombre(self) -> str:
        return self.nombre

    def getId(self) -> int:
        return self.id

    def getFecha_nacimiento(self) -> Fecha:
        return self.fecha_nacimiento

    def getCiudad_nacimiento(self) -> str:
        return self.ciudad_nacimiento

    def getTel(self) -> int:
        return self.tel

    def getEmail(self) -> str:
        return self.email

    def getDir(self) -> Direccion:
        return self.dir

    def __str__(self) -> str:
        return (f"Nombre: {self.nombre}\n"
                f"ID: {self.id}\n"
                f"Fecha de Nacimiento: {self.fecha_nacimiento}\n"
                f"Ciudad de Nacimiento: {self.ciudad_nacimiento}\n"
                f"Teléfono: {self.tel}\n"
                f"Email: {self.email}\n"
                f"Dirección: {str(self.dir)}")
    
class ObjetoFijo(Programa):
    def ejecutar(self):
        """Crea y retorna objetos con información fija para demostración."""
        fecha_nacimiento = Fecha(17, 8, 1995)
        direccion = Direccion(
            "Medellín", 
            "Turin", 
            "909", 
            "56A", 
            "61-24", 
            "El Chagualo")
        usuario = Usuario(
            "Alvaro Guerrero",
            1085322974,
            fecha_nacimiento,
            "Pasto",
            3045299539,
            "ajguerrero@unal.edu.co",
            direccion
        )
        print("\n******* Información del Usuario Fijo ********")
        print("\nFecha de Nacimiento:", fecha_nacimiento)
        print("\nDirección de Residencia:", direccion)
        print("\nUsuario:\n",usuario)
    
class UsuarioConsola(Programa):
    def ejecutar(self):
        
        print("\nIngrese la información del usuario:")
        nombre = input("Nombre: ")
        id_usuario = int(input("ID: "))
        dia = int(input("Día de nacimiento DD: "))
        mes = int(input("Mes de nacimiento MM: "))
        anio = int(input("Año de nacimiento AAAA: "))
        ciudad_nac = input("Ciudad de nacimiento: ")
        tel = int(input("Teléfono: "))
        email = input("Email: ")
        calle = input("Calle: ")
        nomenclatura = input("Nomenclatura: ")
        edificio = input("Edificio: ")
        apto = input("Apto: ")
        barrio = input("Barrio: ")
        ciudad = input("Ciudad: ")
        fecha_nac = Fecha(dia, mes, anio)
        direccion = Direccion(ciudad, edificio, apto, calle, nomenclatura, barrio)
        usuario = Usuario(nombre, id_usuario, fecha_nac, ciudad_nac, tel, email, direccion)
        print("\n---------- Usuario Ingresado ----------")
        print(usuario)

class Menu:
    
    def __init__(self):
        self.programas = {
            "1": ObjetoFijo(),
            "2": UsuarioConsola()
        }

    def mostrar_menu(self):
        while True:
            print("\n--- Menú Principal ---")
            print("1. Mostrar usuario Fijo")
            print("2. Crear usuario por consola")
            print("0. Salir")
            
            opcion = input("Seleccione el programa que desea ejecutar (0-2): ")
            
            if opcion == "0":
                print("Saliendo del programa.")
                break
            elif opcion in self.programas:
                self.programas[opcion].ejecutar()
            else:
                print("Opción no válida. Por favor, seleccione una opción del 0 al 2.")

if __name__ == "__main__":
    menu = Menu()
    menu.mostrar_menu()
