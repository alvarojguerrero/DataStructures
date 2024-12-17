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




class Node:
    def __init__ (self, data, next_node=None):
        self.data = data
        self.next_node = next_node

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next_node

    def set_data(self, data):
        self.data = data

    def set_next(self, next_node):
        self.next_node = next_node

class SimpleList:
    def __init__(self, data):
        node = Node(data)
        self.head = node
        self.tail = node
        self.size = 1

    def size(self):
        return self.size

    def isEmpty(self):
        if self.size == 0:
            return True
        else:
            return False
    
    def setSize(self, new_size):
        self.size = new_size

    def first(self):
        return self.head

    def last(self):
        return self.tail

    def addFirst(self, data):
        node = Node(data)
        if self.isEmpty():
            self.head = node
            self.tail = node
        else:
            node.next_node = self.head
            self.head = node
        self.size += 1

    def addLast(self, data):
        node = Node(data)
        if self.isEmpty():
            self.head = node
            self.tail = node
        else:
            node.next_node = None
            self.tail.next_node = node
            self.tail = node
        self.size += 1

    def removeFirst(self):
        if self.isEmpty():
            return None
        else:
            removed_data = self.head
            self.head = self.head.get_next()
            removed_data.next_node = None
            self.size -= 1
            if self.size == 0:  
                self.tail = None
            return removed_data.data

    def print_list(self,end=""):
        aux = self.head
        while aux:            
            print(aux.get_data(),end=end)
            aux = aux.get_next()
        print("None")


class DoubleNode:
    def __init__(self, data, next_node=None, prev_node=None):
        self.data = data
        self.next_node = next_node
        self.prev_node = prev_node

    def get_data(self):
        return self.data

    def set_data(self, data):
        self.data = data

    def get_next(self):
        return self.next_node

    def set_next(self, next_node):
        self.next_node = next_node

    def get_prev(self):
        return self.prev_node

    def set_prev(self, prev_node):
        self.prev_node = prev_node

class DoubleList:
    
    def __init__(self, data):
        node = DoubleNode(data)
        self.head = node
        self.tail = node
        self.size = 1
        
    def size(self):
        return self.size

    def isEmpty(self):
        if self.size == 0:
            return True
        else:
            return False
    
    def setSize(self, new_size):
        self.size = new_size

    def first(self):
        return self.head

    def last(self):
        return self.tail

    def print_list(self, end=""):
        aux = self.head
        while aux:
            print(aux.get_data(),end=end)
            aux = aux.get_next()
        print("None")

    def addFirst(self, data):
        node = DoubleNode(data)
        if self.size == 0:
            self.head = node
            self.tail = node
        else:
            node.set_next(self.head)
            self.head.set_prev(node) 
            self.head = node
        self.size += 1
        return True

    def removeFirst(self):
        if self.size == 0:
            return None        
        if self.size == 1:
            self.head = None
            self.tail = None
        else:
            aux = self.head
            self.head = self.head.get_next()
            self.head.set_prev(None)
            aux.set_next(None)
        self.size -= 1        
        return aux.get_data()

    def addLast(self, data):
        node = DoubleNode(data)
        if self.size == 0:
            self.head = node
            self.tail = node
        else:
            self.tail.set_next(node)
            node.set_prev(self.tail) 
            self.tail = node
        self.size += 1
        return True

    def removeLast(self):
        if self.size == 0:
            return None        
        if self.size == 1:
            self.head = None
            self.tail = None
        else:
            aux = self.tail
            self.tail = self.tail.get_prev()
            self.tail.set_next(None)
            aux.set_prev(None)
        self.size -= 1        
        return aux.get_data()

    def remove(self, data):
        aux = self.head
        if aux.get_data() == data:
           return self.removeFirst()
        if self.tail.get_data() == data:
            return self.removeLast()
        else:            
            while aux:                
                if aux.get_data() == data:
                    aux.get_next().set_prev(aux.get_prev())
                    aux.get_prev().set_next(aux.get_next())
                    aux.set_next(None)
                    aux.set_prev(None)
                    return aux
                else:
                    aux = aux.get_next()
            return None

    def addAfter(self, node, data):
        if node is None:
            raise ValueError("Nodo invalido")
        new_node = DoubleNode(data)
        new_node.set_prev(node)
        new_node.set_next(node.get_next())
        if node.get_next() is None:  
            self.tail = new_node
        else:
            node.get_next().set_prev(new_node)
        node.set_next(new_node)
        self.size += 1

    def addBefore(self, node, data):
        if node is None:
            raise ValueError("Nodo invalido")
        new_node = DoubleNode(data)
        new_node.set_next(node)
        new_node.set_prev(node.get_prev())
        if node.prev is None: 
            self.head = new_node
        else:
            node.get_prev().set_next(new_node)
        node.set_prev(new_node)
        self.size += 1

class Programa1(Programa):
    def ejecutar(self):
        print("\nValidacion Lista Simple")
        #simple_list = SimpleList()
        simple_list = SimpleList(1)
        for i in range(2, 21, 2):
            simple_list.addLast(i)
        
        simple_list.print_list(end=" -> ")

        for i in [1, 10, 20]:
            current_node = simple_list.head
            previous_node = None
            while current_node is not None:
                if current_node.data == i:
                    if previous_node is None:
                        simple_list.removeFirst()
                    else:
                        previous_node.next_node = current_node.next_node
                    if current_node.next_node is None:
                        simple_list.tail = previous_node
                    simple_list.size -= 1
                    break
                previous_node = current_node
                current_node = current_node.next_node
        
        print("\nLista simple despues de remover 1, 10 y 20")
        simple_list.print_list(end=" -> ")

        print("\nValidación Lista Doble")
        double_list= DoubleList(1)
        for i in range(2, 21, 2):
            double_list.addLast(i)
        
        double_list.print_list(end=" <-> ")

        for data in [1, 10, 20]:
            double_list.remove(data)
        
        print("\nLista Doble despues de remover 1, 10 y 20")
        double_list.print_list(end=" <-> ")


class Programa2(Programa):
    def ejecutar(self):
        agenda = Agenda(5) 
        agenda.import_("/Users/alvaroguerrero/Documents/EstructuraDatos/DataStructures/Lab3/Agenda.txt")
        usuario = Usuario("Carolina", 1, "1996-08-29", "Pasto", 1234567890, "carolina@gmail.com", "Carrera 1 # 1 - 5")
        user_simple_list = SimpleList(usuario)
        for i in range(1,agenda.no_reg):
            user_simple_list.addLast(agenda.registro[i])

        
        print("\n------Usuarios en la Lista Simple------")
        user_simple_list.print_list(end="\n->\n")
    
        print("\n------Ingrese la información del primer usuario para ser agregado a la lista Simple------")
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
        usuario1 = Usuario(nombre, id_usuario, fecha_nac, ciudad_nac, tel, email, direccion)

        print("\n------Ingrese la información del segundo usuario para ser agregado a la lista Simple------")
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
        usuario2 = Usuario(nombre, id_usuario, fecha_nac, ciudad_nac, tel, email, direccion)      
        
        user_simple_list.addFirst(usuario1)
        user_simple_list.addLast(usuario2)

        print("\n------Usuarios en la lista simple después de agregar dos nuevos usuarios------")
        user_simple_list.print_list(end="\n->\n")
        
        user_doble_list = DoubleList(usuario)
        print("\nn------Usuarios importados para Lista Doble------")
        for i in range(1,agenda.no_reg):
            user_doble_list.addLast(agenda.registro[i])
        
        user_doble_list.print_list(end="\n<->\n")

        print("\n------Ingrese la información del usuario para la lista Doble------")
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
        usuario3 = Usuario(nombre, id_usuario, fecha_nac, ciudad_nac, tel, email, direccion)
        
        tercer_nodo = user_doble_list.first().get_next().get_next()
        user_doble_list.addAfter(tercer_nodo, usuario3)
        
        print("\n------Usuarios en la lista doble después de agregar el nuevos nodo------")
        user_doble_list.print_list(end="\n<->\n")

class Menu:
    
    def __init__(self):
        self.programas = {
            "1": Programa1(),
            "2": Programa2()
        }

    def mostrar_menu(self):
        while True:
            print("\n--- Menú Principal ---")
            print("1. Programa 1, elementos en una lista simple y doblemente enlazada")
            print("2. Programa 2, usuarios en una lista simple y doblemente enlazada")
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