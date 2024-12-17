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
    
class Agenda:
    def __init__(self, capacity: int):
        self.registro = [None] * capacity  
        self.no_reg = 0  

    def agregar(self, u: Usuario) -> bool:
        if self.buscar(u.id) != -1:
            return False  

        if self.no_reg < len(self.registro):
            self.registro[self.no_reg] = u
            self.no_reg += 1
            return True

        return False  

    def buscar(self, id: int) -> int:
        for i in range(self.no_reg):
            if self.registro[i].id == id:
                return i
        return -1

    def eliminar(self, id: int) -> bool:
        pos = self.buscar(id)
        if pos == -1:
            return False 
        
        for i in range(pos, self.no_reg - 1):
            self.registro[i] = self.registro[i + 1]

        self.registro[self.no_reg - 1] = None  
        self.no_reg -= 1
        return True

    def toFile(self, filename: str = "agenda.txt"):
        with open(filename, "w") as file:
            for i in range(self.no_reg):
                u = self.registro[i]
                file.write(f"{u.id},{u.nombre},{u.fecha_nacimiento},{u.ciudad_nacimiento},{u.tel},{u.email},{u.dir}\n")

    def import_(self, filename: str = "agenda.txt"):
        with open(filename, "r") as file:
            for line in file:
                data = line.strip().split(",")
                u = Usuario(
                    id=int(data[0]),
                    nombre=data[1],
                    fecha_nacimiento=data[2], 
                    ciudad_nacimiento=data[3],
                    tel=int(data[4]),
                    email=data[5],
                    dir=data[6],  
                )
                self.agregar(u)

class BuscarUsuario(Programa):
    def ejecutar(self):
        usuario1 = Usuario("Carolina", 1, "1996-08-29", "Pasto", 1234567890, "carolina@gmail.com", "Carrera 1 # 1 - 5")
        usuario2 = Usuario("Alvaro", 2, "1995-08-17", "Medellin", 2345678901, "alvaroj@gmail.com", "Calle 2 # 16 - 5")
        usuario3 = Usuario("Juan", 3, "1996-02-03", "Neiva", 3456789012, "juan96@gmail.com", "Carrera 3 # 45 - 5")
        usuario4 = Usuario("Karyme", 4, "2001-02-19", "Pasto", 4567890123, "juli@gmail.com", "Calle 4 # 67 - 5")
        usuario5 = Usuario("Diana", 5, "1985-04-10", "Pasto", 5678901234, "dianicre@gmail.com", "Carrera 5 # 16 - 5")
        agenda = Agenda(5)  
        agenda.agregar(usuario1)
        agenda.agregar(usuario2)
        agenda.agregar(usuario3)
        agenda.agregar(usuario4)
        agenda.agregar(usuario5)
        agenda.toFile("Agenda.txt")
        
        id_to_search = int(input("Ingrese el ID que desea buscar: "))
        pos = agenda.buscar(id_to_search)
        if pos != -1:
            print(f"\nUsuario con ID {id_to_search} está en la posición: {pos}")
        else:
            print(f"\nUsuario con ID {id_to_search} no encontrado: {pos}")
        
        agenda.toFile("Agenda.txt")

class EliminarUsuario(Programa):
    def ejecutar(self):
        agenda2 = Agenda(5) 
        agenda2.import_("Agenda.txt")

        print("Usuarios importados:")
        for i in range(agenda2.no_reg):
            print(f"\n------- Registros de Usuarios {i} -------")
            print(agenda2.registro[i])
        
        id_to_delete = int(input("\nIngrese el ID que desea eliminar: "))
        if agenda2.eliminar(id_to_delete):
            print(f"Usuario con ID {id_to_delete} eliminado.")
        else:
            print(f"Usuario con ID {id_to_delete} no encontrado.")

        agenda2.toFile("Agenda2.txt")
class Menu:
    
    def __init__(self):
        self.programas = {
            "1": BuscarUsuario(),
            "2": EliminarUsuario()
        }

    def mostrar_menu(self):
        while True:
            print("\n--- Menú Principal ---")
            print("1. Buscar usuario por ID")
            print("2. Eliminar usuario por ID")
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