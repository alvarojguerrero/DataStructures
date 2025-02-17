from abc import ABC, abstractmethod
import random
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


class Node:
    def __init__ (self, data=None, next_node=None):
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
    def __init__(self):
        node = Node()
        self.head = node
        self.tail = node
        self.size = 0

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
    def __init__(self, data=None, next_node=None, prev_node=None):
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
    
    def __init__(self):
        self.head = DoubleNode()
        self.tail = DoubleNode()
        self.size = 0
        #node = DoubleNode(data)
        #self.head = node
        #self.tail = node
        #self.size = 1
        
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
        if self.isEmpty():
            self.head = node
            self.tail = node
        else:
            node.set_next(self.head)
            self.head.set_prev(node) 
            self.head = node
        self.size += 1
        return True

    def removeFirst(self):
        if self.isEmpty():
            return None        
        else:
            aux = self.head
            self.head = self.head.get_next()
            self.head.set_prev(None)
            aux.set_next(None)
            self.size -= 1        
            return aux.get_data()

    def addLast(self, data):
        node = DoubleNode(data)
        if self.isEmpty():
            self.head = node
            self.tail = node
        else:
            self.tail.set_next(node)
            node.set_prev(self.tail)
            self.tail = node
        self.size += 1
        return True

    def removeLast(self):
        if self.isEmpty():
            return None      
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

    def swap_node(self, aux1, aux2):
        
        if self.head == aux1:
            self.head = aux2
        elif self.head == aux2:
            self.head = aux1
        if self.tail == aux1:
            self.tail = aux2
        elif self.tail == aux2:
            self.tail = aux1
        
        temp = aux1.get_next()
        aux1.set_next(aux2.get_next())
        aux2.set_next(temp)

        if aux1.get_next() != None:
            aux1.get_next().set_prev(aux1)
        if aux2.get_next() != None:
            aux2.get_next().set_prev(aux2) 
     
        temp = aux2.get_prev()
        aux2.set_prev(aux1.get_prev())
        aux1.set_prev(temp)

        if aux1.get_prev() != None:
            aux1.get_prev().set_next(aux1)
        if aux2.get_prev() != None:
            aux2.get_prev().set_next(aux2) 
         
        return True
        
    def bubbleSort(self):
        for i in range(self.size):
            aux = self.head
            while aux != None:                
                if aux.get_next():
                    if aux.get_data > aux.get_next().get_data():
                        self.swap_node(aux, aux.get_next())
                        break                
                aux = aux.get_next()
        return True

class Ordenador:
    def __init__(self, limit):
        self.limit = limit
        self.A =  [random.randint(1, 100) for _ in range(self.limit)]

    def inicializar(self):
        self.A = [random.randint(1, 100) for _ in range(self.limit)]

    def ordenar_burbuja(self):
        for i in range(len(self.A)):
            for j in range(1, len(self.A) - i):
                if self.A[j - 1] > self.A[j]:
                    self.A[j - 1], self.A[j] = self.A[j], self.A[j - 1]

    def ordenar_seleccion(self):
        for i in range(len(self.A)):
            min_index = i
            for j in range(i + 1, len(self.A)):
                if self.A[j] < self.A[min_index]:
                    min_index = j
            self.A[i], self.A[min_index] = self.A[min_index], self.A[i]

    def ordenar_insercion(self):
        for i in range(1, len(self.A)):
            temp = self.A[i]
            j = i
            while j > 0 and self.A[j - 1] > temp:
                self.A[j] = self.A[j - 1]
                j -= 1
            self.A[j] = temp

    def ordenar_mergeSort(self):

        def merge(A, start, mid, end):

            # Subarreglos temporales
            left = A[start:mid + 1]
            right = A[mid + 1:end + 1]

            # Índices para recorrer los subarreglos
            i = j = 0
            k = start

            # Combinar elementos de left y right en A
            while i < len(left) and j < len(right):
                if left[i] <= right[j]:
                    A[k] = left[i]
                    i += 1
                else:
                    A[k] = right[j]
                    j += 1
                k += 1

            # Copiar elementos restantes de left
            while i < len(left):
                A[k] = left[i]
                i += 1
                k += 1

            # Copiar elementos restantes de right
            while j < len(right):
                A[k] = right[j]
                j += 1
                k += 1

        def merge_sort(A, start, end):

            if start < end:
                mid = (start + end) // 2

                merge_sort(A, start, mid)
                merge_sort(A, mid + 1, end)

                merge(A, start, mid, end)

        merge_sort(self.A, 0, len(self.A) - 1)

    def mostrar(self):
        print(self.A)

    def busqueda_binaria(self, valor):
        self.ordenar_burbuja()
        self.mostrar()  
        izquierda, derecha = 0, len(self.A) - 1
        while izquierda <= derecha:
            mid = (izquierda + derecha) // 2
            if self.A[mid] == valor:
                return mid
            elif self.A[mid] < valor:
                izquierda = mid + 1
            else:
                derecha = mid - 1
        return -1

class OrdenadorLista:
    def __init__(self):
        self.L = SimpleList()

    def inicializar(self, num_elements):
        for _ in range(num_elements):
            self.agregar(random.randint(1, 100))

    def agregar(self, data):
        self.L.addLast(data)

    def ordenar(self):
        if self.L.isEmpty() or self.L.head.get_next() is None:
            return

        current = self.L.head
        while current is not None:
            min_node = current
            aux = current.get_next()
            while aux is not None:
                if aux.get_data() < min_node.get_data():
                    min_node = aux
                aux = aux.get_next()

            # Intercambia los datos de los nodos
            if min_node != current:
                current.data, min_node.data = min_node.data, current.data

            current = current.get_next()        

    def mostrar(self, end=""):
        aux = self.L.head
        while aux:
            print(aux.get_data(),end=end)
            aux = aux.get_next()
        print("None")



class OrdenadorAgenda():
    def __init__(self):
        self.L = DoubleList()

    def agregar_usuario(self, usuario):
        self.L.addLast(usuario)

    def swap_node(self, aux1, aux2):
        if self.L.head == aux1:
            self.L.head = aux2
        elif self.L.head == aux2:
            self.L.head = aux1

        if self.L.tail == aux1:
            self.L.tail = aux2
        elif self.L.tail == aux2:
            self.L.tail = aux1

        # Intercambio de referencias next
        temp = aux1.get_next()
        aux1.set_next(aux2.get_next())
        aux2.set_next(temp)

        if aux1.get_next() is not None:
            aux1.get_next().set_prev(aux1)
        if aux2.get_next() is not None:
            aux2.get_next().set_prev(aux2)

        # Intercambio de referencias prev
        temp = aux2.get_prev()
        aux2.set_prev(aux1.get_prev())
        aux1.set_prev(temp)

        if aux1.get_prev() is not None:
            aux1.get_prev().set_next(aux1)
        if aux2.get_prev() is not None:
            aux2.get_prev().set_next(aux2)

    def ordenar(self):
        if self.L.size < 2: 
            return

        for _ in range(self.L.size):  
            swapped = False
            aux = self.L.head

            while aux and aux.get_next(): 
                
                if aux.data.getId() > aux.get_next().data.getId():
                    self.swap_node(aux, aux.get_next())
                    swapped = True  
                else:
                    aux = aux.get_next()

            
            if not swapped:
                break        

    def mostrar(self, end=""):
        aux = self.L.head
        while aux:
            print(aux.get_data(),end=end)
            aux = aux.get_next()
        print("None")

class Programa1(Programa):
    def ejecutar(self):
        print("\nArreglo Inicial Aleatorios:")
        ordenador = Ordenador(10)
        ordenador.mostrar()
        print("\nOrdenando con burbuja:")
        ordenador.ordenar_burbuja()
        ordenador.mostrar()
        print("-"*40)
        print("\nArreglo Valores Aleatorios:")
        ordenador.inicializar()
        ordenador.mostrar()
        print("\nOrdenando con selección:")
        ordenador.ordenar_seleccion()
        ordenador.mostrar()
        print("-"*40)
        print("\nArreglo Valores Aleatorios:")
        ordenador.inicializar()
        ordenador.mostrar()
        print("\nOrdenando con inserción:")
        ordenador.ordenar_insercion()
        ordenador.mostrar()
        print("-"*40)
        print("\nArreglo Valores Aleatorios:")
        ordenador.inicializar()
        ordenador.mostrar()
        print("\nOrdenando con merge sort:")
        ordenador.ordenar_mergeSort()
        ordenador.mostrar()
        print("-"*40)
        print("\nBusqueda Binaria:")
        ordenador.inicializar()
        ordenador.mostrar()
        num = int(input("Ingrese el valor que desea buscar: "))
        print(f"El valor esta en el indice: {ordenador.busqueda_binaria(num)}")
        print("-"*40)



class Programa2(Programa):
    def ejecutar(self):
        ordenador_lista = OrdenadorLista()
        ordenador_lista.inicializar(12)
        print("Lista inicial:")
        ordenador_lista.mostrar(end=" -> ")
        print("\nOrdenando la lista:")
        ordenador_lista.ordenar()
        print("Lista después de ordenar:")
        ordenador_lista.mostrar(end=" -> ")

class Programa3(Programa):
    def ejecutar(self):
        ordenador_agenda = OrdenadorAgenda()
        #ordenador_agenda.mostrar()
        #print("_____________")
        print("\nAgregando usuarios:")
        with open("usuarios.txt", "r") as file:
            for line in file:
                datos = line.strip().split(",")
                cedula = int(datos[0])
                nombre = datos[1]
                fecha_nacimiento = Fecha(int(datos[2].split("-")[2]), int(datos[2].split("-")[1]), int(datos[2].split("-")[0]))
                ciudad_nacimiento = datos[3]
                tel = int(datos[4])
                email = datos[5]
                direccion = Direccion(datos[6], ciudad_nacimiento)
                usuario = Usuario(nombre, cedula, fecha_nacimiento, ciudad_nacimiento, tel, email, direccion)
                ordenador_agenda.agregar_usuario(usuario)
        print("\nUsuario de la agenda en la lista doble:")
        ordenador_agenda.mostrar(end="\n <-> \n")
        print("-"*40)
        print("\nOrdenando la agenda por cedula:")
        ordenador_agenda.ordenar()
        ordenador_agenda.mostrar(end="\n <-> \n")


class Menu:
    
    def __init__(self):
        self.programas = {
            "1": Programa1(),
            "2": Programa2(),
            "3": Programa3()
        }

    def mostrar_menu(self):
        while True:
            print("\n--- Menú Principal ---")
            print("1. Probar clase Ordenador")
            print("2. Probar clase Ordenador Lista")
            print("3. Probar clase Ordenador Agenda")
            print("0. Salir")
            
            opcion = input("Seleccione el programa que desea ejecutar (0-3): ")
            
            if opcion == "0":
                print("Saliendo del programa.")
                break
            elif opcion in self.programas:
                self.programas[opcion].ejecutar()
            else:
                print("Opción no válida. Por favor, seleccione una opción del 0 al 3.")

if __name__ == "__main__":
    menu = Menu()
    menu.mostrar_menu()
