
import tkinter as tk
from tkinter import messagebox
import os
import datetime


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
    def __init__(self, calle: str = "", nomenclatura: str = "", barrio: str = "", ciudad: str = "", edificio: str = "", apto: str = ""):
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
        return f"{self.calle} # {self.nomenclatura}, Edificio: {self.edificio}, Apto {self.apto}, Barrio: {self.barrio} - {self.ciudad}." 

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
        if aux.data.getId() == data:
           return self.removeFirst()
        if self.tail.data.getId() == data:
            return self.removeLast()
        else:            
            while aux:                
                if aux.data.getId() == data:
                    aux.get_next().set_prev(aux.get_prev())
                    aux.get_prev().set_next(aux.get_next())
                    aux.set_next(None)
                    aux.set_prev(None)
                    return aux
                else:
                    aux = aux.get_next()
            return None

    def _remove(self, data):
        aux = self.head
        if aux.data.getPlaca() == data:
           return self.removeFirst()
        if self.tail.data.getPlaca() == data:
            return self.removeLast()
        else:            
            while aux:                
                if aux.data.getPlaca() == data:
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
        # for i in range(self.size):
        #     aux = self.head
        #     while aux != None:                
        #         if aux.get_next():
        #             print("aqui",aux.get_data().placa, aux.get_next().get_data().placa)
        #             if aux.get_data().placa > aux.get_next().get_data().placa:
        #                 self.swap_node(aux, aux.get_next())
        #                 break                
        #         aux = aux.get_next()
        for i in range(self.size):
            aux = self.head
            while aux is not None:
                if aux.get_next():
                    current_data = aux.get_data()
                    next_data = aux.get_next().get_data()
                    if (current_data.nombre > next_data.nombre) or (current_data.nombre == next_data.nombre and current_data.placa > next_data.placa):
                        self.swap_node(aux, aux.get_next())
                        break
                aux = aux.get_next()
        return True
    
    def search_by_id(self, _id):
        aux = self.head
        while aux:
            if aux.get_data().getId() == _id:
                return aux.get_data()
            aux = aux.get_next()
        return None

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
    
    def __iter__(self):
        current = self.head
        while current:
            yield current.get_data()  # Devolvemos el dato de cada nodo
            current = current.get_next()

class Equipo:
    def __init__(self, nombre:str, placa:int, fecha_compra:Fecha, valor:int):
        self.nombre = nombre
        self.placa = placa
        self.fecha_compra = fecha_compra
        self.valor = valor
    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre

    def getPlaca(self):
        return self.placa

    def setPlaca(self, placa):
        self.placa = placa

    def getFechaCompra(self):
        return self.fecha_compra

    def setFechaCompra(self, fecha_compra):
        self.fecha_compra = fecha_compra

    def getValor(self):
        return self.valor

    def setValor(self, valor):
        self.valor = valor
    
    def __str__(self):
        return (f"Equipo: {self.nombre}\n"
                f"Placa: {self.placa}\n"
                f"Fecha de Compra: {self.fecha_compra}\n"
                f"Valor: {self.valor}\n")

class Administrador:
    def __init__(self, cedula, nombre, empleados, contrasenas):
        self.nombre = nombre
        self.cedula = cedula
        self.solicitudes_agregar = SimpleList()
        self.solicitudes_eliminar = SimpleList()
        self.empleados = empleados
        self.contrasenas = contrasenas
        self.inventario = DoubleList()

    def generar_archivo_solicitudes_pendientes(self):
        try:
            with open("Solicitudes_pendientes_agregar.txt", "w") as archivo_pendientes:
                with open("Solicitudes_agregar.txt", "r") as archivo:
                    for line in archivo:
                        datos = line.strip().split(" ")
                        if datos[8] == "Pendiente":
                            archivo_pendientes.write(f"{datos[0]} {datos[1]} {datos[2]} {datos[3]} {datos[4]} {datos[5]} {datos[6]} {datos[7]} {datos[8]}\n")
            messagebox.showinfo("Éxito", f"El archivo Solicitudes_pendientes_agregar.txt ha sido generado con éxito")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo generar el archivo: Solicitudes_pendientes_agregar.txt")
    
    def generar_archivo_solicitudes_pendientes_eliminar(self):
        try:
            with open("Solicitudes_pendientes_eliminar.txt", "w") as archivo_pendientes:
                with open("Solicitudes_eliminar.txt", "r") as archivo:
                    for line in archivo:
                        datos = line.strip().split(" ")
                        if datos[4] == "Pendiente":
                            archivo_pendientes.write(f"{datos[0]} {datos[1]} {datos[2]} {datos[3]} {datos[4]}\n")
            messagebox.showinfo("Éxito", f"El archivo Solicitudes_pendientes_eliminar.txt ha sido generado con éxito")
        except Exception as e:
            messagebox.showerror("Error", f"No se pudo generar el archivo: Solicitudes_pendientes_eliminar.txt")
    def registrar_usuario(self, usuario, passwords, rol):
        with open("Empleados.txt", "a") as f:
            f.write(f"{usuario.nombre} {usuario.id} {usuario.fecha_nacimiento.getDia()} {usuario.fecha_nacimiento.getMes()} {usuario.fecha_nacimiento.getA()} {usuario.ciudad_nacimiento} {usuario.tel} {usuario.email} {usuario.dir.getCalle()} {usuario.dir.getNomenclatura()} {usuario.dir.getBarrio()} {usuario.dir.getCiudad()} {usuario.dir.getEdificio()} {usuario.dir.getApto()}\n")
        with open("Password.txt", "a") as f:
            f.write(f"{usuario.getId()} {passwords} {rol}\n")


    def eliminar_usuario(self, empleados, passwords, _id):
        temp_contra = {}
        self.empleados.remove(_id)

        with open("Empleados.txt", "w") as f:
            aux = empleados.head
            while aux:
                usuario = aux.get_data()
                f.write(f"{usuario.nombre} {usuario.id} {usuario.fecha_nacimiento.getDia()} {usuario.fecha_nacimiento.getMes()} {usuario.fecha_nacimiento.getA()} {usuario.ciudad_nacimiento} {usuario.tel} {usuario.email} {usuario.dir.getCalle()} {usuario.dir.getNomenclatura()} {usuario.dir.getBarrio()} {usuario.dir.getCiudad()} {usuario.dir.getEdificio()} {usuario.dir.getApto()}\n")
                aux = aux.get_next()
        passwords.pop(str(_id))
        with open("Password.txt", "w") as f:
            for key, value in passwords.items():
                f.write(f"{key} {value['password']} {value['rol']}\n")
                temp_contra[key] = {"password": value['password'], "rol": value['rol']}
        self.contrasenas = temp_contra
    
    def cambiar_password(self, passwords, _id, password):
        passwords[str(_id)]["password"] = password
        with open("Password.txt", "w") as f:
            for key, value in passwords.items():
                f.write(f"{key} {value['password']} {value['rol']}\n")
        return True

    def responder_solicitudes_agregar(self):
        try:    
            solicitud = ""
            with open("Solicitudes_agregar.txt", "r") as f:
                for line in f:
                    datos = line.strip().split(" ")
                    print("datos", datos)
                    if datos[8] == "Pendiente":
                        solicitud += f"¿Desea agregar el equipo {datos[2]} con placa {datos[3]} al inventario de {datos[0]}?\n"
                        break
            return solicitud,datos,line
        except FileNotFoundError:
            print("El archivo 'Solicitudes_agregar.txt' no se encontró.")
            return None
 

    def responder_solicitudes_eliminar(self):
        solicitud = ""
        with open("Solicitudes_eliminar.txt", "r") as f:
            for line in f:
                datos = line.strip().split(" ")
                print("datos", datos)
                if datos[4] == "Pendiente":
                    solicitud += f"¿Desea eliminar el equipo con placa {datos[2]}\nJufstificacion: {datos[3]}?\n"
                    break
        print("solicitud", solicitud)
        return solicitud,datos,line



    def registrar_control_de_cambio(self, investigador_id, placa, tipo_cambio):
        with open("Control_de_cambio.txt", "a") as f:
            fecha_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"{investigador_id} {placa} {tipo_cambio} {fecha_hora}\n")

    def actualizar_inventario(self, new_registro):
        update_inventario = DoubleList()
        try:
            with open("InventarioGeneral.txt", "r") as archivo:
                for linea in archivo:
                    datos = linea.strip().split(" ")
                    nombre = datos[0]
                    id_investigador = int(datos[1])
                    fecha_compra = Fecha(int(datos[4]), int(datos[5]), int(datos[6]))
                    equipo = Equipo(datos[2], int(datos[3]), fecha_compra, int(datos[7]))
                    registros = Inventario(nombre, id_investigador, equipo.getNombre(), equipo.getPlaca(), equipo.getFechaCompra(), equipo.getValor())
                    update_inventario.addLast(registros)
        except FileNotFoundError:
            print("El archivo 'InventarioGeneral.txt' no se encontró.")
        update_inventario.addLast(new_registro)
        update_inventario.bubbleSort()
        with open("InventarioGeneral.txt", "w") as archivo:
            aux = update_inventario.head
            while aux:
                registro = aux.get_data()
                archivo.write(f"{registro.getNombre()} {registro.getId()} {registro.getEquipo()} {registro.getPlaca()} {registro.getFecha().getDia()} {registro.getFecha().getMes()} {registro.getFecha().getA()} {registro.getValor()}\n")
                aux = aux.get_next()    
    
    def actualizar_inventario_eliminar(self, placa):
        update_inventario = DoubleList()
        try:
            with open("InventarioGeneral.txt", "r") as archivo:
                for linea in archivo:
                    datos = linea.strip().split(" ")
                    nombre = datos[0]
                    id_investigador = int(datos[1])
                    fecha_compra = Fecha(int(datos[4]), int(datos[5]), int(datos[6]))
                    equipo = Equipo(datos[2], int(datos[3]), fecha_compra, int(datos[7]))
                    registros = Inventario(nombre, id_investigador, equipo.getNombre(), equipo.getPlaca(), equipo.getFechaCompra(), equipo.getValor())
                    update_inventario.addLast(registros)
        except FileNotFoundError:
            print("El archivo 'InventarioGeneral.txt' no se encontró.")
        update_inventario.print_list("\n")
        update_inventario._remove(int(placa))
        update_inventario.bubbleSort()
        update_inventario.print_list("\n")
        with open("InventarioGeneral.txt", "w") as archivo:
            aux = update_inventario.head
            while aux:
                registro = aux.get_data()
                archivo.write(f"{registro.getNombre()} {registro.getId()} {registro.getEquipo()} {registro.getPlaca()} {registro.getFecha().getDia()} {registro.getFecha().getMes()} {registro.getFecha().getA()} {registro.getValor()}\n")
                aux = aux.get_next()

    def actualizar_estado_solicitud(self, archivo, linea, estado):
        if estado == "Aceptada":
            linea_invetario = linea.strip().split(" ")
            add_invetario = Inventario(linea_invetario[0], linea_invetario[1], linea_invetario[2], int(linea_invetario[3]), Fecha(linea_invetario[4], linea_invetario[5], linea_invetario[6]), linea_invetario[7])
            self.inventario.addFirst(add_invetario)
            self.actualizar_inventario(add_invetario)

        with open(archivo, "r") as f:
            lineas = f.readlines()
        with open(archivo, "w") as f:
            for l in lineas:
                if l.strip() == linea.strip():
                    datos = l.strip().split(" ")
                    datos[8] = estado
                    f.write(" ".join(datos) + "\n")
                else:
                    f.write(l)
    
    def actualizar_estado_solicitud_eliminar(self, archivo, linea, estado):
        self.actualizar_inventario_eliminar(linea.strip().split(" ")[2])
        with open(archivo, "r") as f:
            lineas = f.readlines()
        with open(archivo, "w") as f:
            for l in lineas:
                if l.strip() == linea.strip():
                    datos = l.strip().split(" ")
                    datos[4] = estado
                    f.write(" ".join(datos) + "\n")
                else:
                    f.write(l)

    def listar_equipos(self, _id):
        equipos_widget = ""
        equipos_txt = ""
        try:
            with open("InventarioGeneral.txt", "r") as archivo:
                for linea in archivo:
                    datos = linea.strip().split(" ")
                    if datos[1] == str(_id):
                        fecha_compra = Fecha(datos[4], datos[5], datos[6])
                        equipo = Equipo(datos[2], datos[3], fecha_compra, datos[7])
                        #self.equipos.addLast(equipo)
                        
                        equipos_widget += f"Equipo: {equipo.nombre} | Placa: {equipo.placa} | Fecha Compra: {equipo.fecha_compra} | Valor: {equipo.valor} \n"
                        equipos_txt += f"{equipo.nombre} {equipo.placa} {equipo.fecha_compra} {equipo.valor} \n"

        except FileNotFoundError:
            print("Error", "El archivo 'InventarioGeneral.txt' no se encontró.")
        
        return equipos_widget, equipos_txt 
    
    def consultar_control_de_cambio(self):
        control_de_cambio = ""
        try:
            with open("Control_de_cambios.txt", "r") as archivo:
                for linea in archivo:
                    datos = linea.strip().split(" ")
                    #print("datos", datos)
                    control_de_cambio += f"{datos[0]} {datos[1]} {datos[2]} {datos[3]} \n"
        except FileNotFoundError:
            print("El archivo 'Control_de_cambio.txt' no se encontró.")
        return control_de_cambio
    
    def generar_archivo_control_de_cambio(self):
        contol_cambios = self.consultar_control_de_cambio()
        
        nombre_archivo = f"Control_de_cambios.txt"
        
        try:
            with open(nombre_archivo, "w") as archivo:
                archivo.write(contol_cambios)
                messagebox.showinfo("Éxito", f"El archivo '{nombre_archivo}' ha sido generado con éxito.")
            return nombre_archivo  
        except Exception as e:
            messagebox.showinfo("Fallo", f"El archivo '{nombre_archivo}' no se ha generado con éxito.")
            return str(e)  

    def registrar_control_de_cambio(self, cedula, placa, tipo):
        with open("Control_de_cambios.txt", "a") as f:
            f.write(f"{cedula} {placa} {tipo} {datetime.datetime.now().strftime('%d-%m-%Y %H:%M')}\n")

    def obtener_inventario_investigador(self, identificacion_investigador):

        equipos_inve = ""
        inventario_investigador = DoubleList()
        try:
            with open("InventarioGeneral.txt", "r") as archivo:
                for linea in archivo:
                    datos = linea.strip().split(" ")
                    if int(datos[1]) == int(identificacion_investigador):
                        nombre = datos[0]
                        fecha_compra = Fecha(int(datos[4]), int(datos[5]), int(datos[6]))
                        equipo = Equipo(datos[2], int(datos[3]), fecha_compra, int(datos[7]))
                        registro = Inventario(nombre, identificacion_investigador, equipo.getNombre(), equipo.getPlaca(), equipo.getFechaCompra(), equipo.getValor())
                        inventario_investigador.addFirst(registro)
        except FileNotFoundError:
            print("El archivo 'InventarioGeneral.txt' no se encontró.")
        inventario_investigador.bubbleSort()
        equipos_inve = ""
        aux = inventario_investigador.head
        while aux:
            registro = aux.get_data()
            equipos_inve += f"{registro.equipo} {registro.placa} {registro.fecha} {equipo.valor} \n"
            aux = aux.get_next()
        if equipos_inve != "":
            nombre_archivo = f"{nombre} {identificacion_investigador}.txt"
            with open(nombre_archivo, "w") as f:
                f.write(equipos_inve)

        return equipos_inve
 
    def cargar_inventario(self):
        inventario = DoubleList()
        try:
            with open("InventarioGeneral.txt", "r") as archivo:
                for linea in archivo:
                    datos = linea.strip().split(" ")
                    nombre = datos[0]
                    id_investigador = int(datos[1])
                    fecha_compra = Fecha(int(datos[4]), int(datos[5]), int(datos[6]))
                    equipo = Equipo(datos[2], int(datos[3]), fecha_compra, int(datos[7]))
                    registro = Inventario(nombre, id_investigador, equipo.getNombre(), equipo.getPlaca(), equipo.getFechaCompra(), equipo.getValor())
                    inventario.addLast(registro)
                    inventario.bubbleSort()
                inventario.bubbleSort()
                with open("InventarioGeneral.txt", "w") as archivo_w:
                    aux = inventario.head
                    while aux:
                        registro = aux.get_data()
                        archivo_w.write(f"{registro.getNombre()} {registro.getId()} {registro.getEquipo()} {registro.getPlaca()} {registro.getFecha().getDia()} {registro.getFecha().getMes()} {registro.getFecha().getA()} {registro.getValor()}\n")
                        aux = aux.get_next()
        except FileNotFoundError:
            if self.inventario.size > 1:
                self.inventario.bubbleSort()
                with open("InventarioGeneral.txt", "w") as archivo:
                    aux = self.inventario.head
                    while aux:
                        registro = aux.get_data()
                        archivo.write(f"{registro.getNombre()} {registro.getId()} {registro.getEquipo()} {registro.getPlaca()} {registro.getFecha().getDia()} {registro.getFecha().getMes()} {registro.getFecha().getA()} {registro.getValor()}\n")
                        aux = aux.get_next()
                    
        self.inventario = inventario
        return inventario

class Investigador:
    def __init__(self, cedula, nombre):
        self.nombre = nombre
        self.cedula = cedula
        self.solicitudes = SimpleList()
        self.equipos = SimpleList()


    def listar_equipos(self, _id):
        equipos_widget = ""
        equipos_txt = ""
        try:
            with open("InventarioGeneral.txt", "r") as archivo:
                for linea in archivo:
                    datos = linea.strip().split(" ")
                    if datos[1] == str(_id):
                        fecha_compra = Fecha(datos[4], datos[5], datos[6])
                        equipo = Equipo(datos[2], datos[3], fecha_compra, datos[7])
                        self.equipos.addLast(equipo)
                        
                        equipos_widget += f"Equipo: {equipo.nombre} | Placa: {equipo.placa} | Fecha Compra: {equipo.fecha_compra} | Valor: {equipo.valor} \n"
                        equipos_txt += f"{equipo.nombre} {equipo.placa} {equipo.fecha_compra} {equipo.valor} \n"

        except FileNotFoundError:
            print("Error", "El archivo 'InventarioGeneral.txt' no se encontró.")
        
        return equipos_widget, equipos_txt 


    def generar_archivo(self):
        _, equipos_lista = self.listar_equipos(self.cedula)
        
        nombre_archivo = f"{self.nombre} {self.cedula}.txt"
        
        try:
            with open(nombre_archivo, "w") as archivo:
                archivo.write(equipos_lista)
            return nombre_archivo  
        except Exception as e:
            return str(e)  

    def generar_archivo_solicitudes(self):
        equipos_lista = self.consultar_estado_solicitudes()
        
        nombre_archivo = f"Solicitudes {self.nombre} {self.cedula}.txt"
        
        try:
            with open(nombre_archivo, "w") as archivo:
                archivo.write(equipos_lista)
            return nombre_archivo  
        except Exception as e:
            return str(e)  

    def solicitar_agregar_equipo(self, nombre, placa, fecha_compra, valor):
        equipo = Equipo(nombre, placa, fecha_compra, valor)
        with open("Solicitudes_agregar.txt", "a") as f:
            f.write(f"{self.nombre} {self.cedula} {equipo.nombre} {equipo.placa} {equipo.fecha_compra.getDia()} {equipo.fecha_compra.getMes()} {equipo.fecha_compra.getA()} {equipo.valor} {'Pendiente'}\n")
        self.solicitudes.addFirst(Solicitud("Agregar",self.nombre, self.cedula, equipo.nombre, equipo.valor, fecha_compra, "Pendiente"))

    def solicitar_eliminar_equipo(self, placa, justificacion):
        with open("Solicitudes_eliminar.txt", "a") as f:
            justificacion = justificacion.replace(" ", "_")
            f.write(f"{self.nombre} {self.cedula} {placa} {justificacion} {'Pendiente'}\n")
        self.solicitudes.addFirst(SolicitudEliminar("Eliminar",self.nombre, self.cedula, placa, justificacion, "Pendiente"))


    def consultar_estado_solicitudes(self):
        sol = ""
        solicitudes_previas = self.leer_solicitudes_archivo(self.cedula)
        
        print(f"Consultando solicitudes para el ID {self.cedula}...")

        aux = self.solicitudes.head.get_data()
        print("aux", aux)
        if aux == None:
            pass
        else:
            aux = self.solicitudes.head
            while aux:
                if aux.get_data().id_investigador == self.cedula:
                    print(f"Solicitud actual: {aux.get_data()}")
                    sol += f"Solicitud actual: {aux.get_data()}\n"
                aux = aux.get_next()

        for solicitud in solicitudes_previas:
            print(f"Solicitud previa desde archivo: {solicitud}")
            sol += f"Solicitud previa: {solicitud}\n"

        return sol 
    
    def leer_solicitudes_archivo(self,id_investigador):
        solicitudes = SimpleList()
        try:
            with open("Solicitudes_agregar.txt", "r") as file:
                for line in file:
                    parts = line.strip().split()
                    
                    if len(parts) >= 7:  
                        nombre = parts[0]
                        id_solicitud = parts[1]
                        apellido = parts[2]
                        monto = parts[3]
                        fecha = " ".join(parts[4:8])  
                        estado = parts[8]

                        # Filtramos por ID de investigador
                        if id_solicitud == str(id_investigador):
                            solicitud = Solicitud("Agregar",nombre, id_solicitud, apellido, monto, fecha, estado)
                            solicitudes.addFirst(solicitud)
        except FileNotFoundError:
            print("El archivo 'Solicitudes_agregar.txt' no fue encontrado.")

        try:
            with open("Solicitudes_eliminar.txt", "r") as file:
                for line in file:
                    parts = line.strip().split()
                    
                    if len(parts) >= 5:  
                        nombre = parts[0]
                        id_solicitud = parts[1]
                        placa = parts[2]
                        justificacion = parts[3]
                        estado = parts[4]

                        # Filtramos por ID de investigador
                        if id_solicitud == str(id_investigador):
                            solicitud = SolicitudEliminar("Eliminar",nombre, id_solicitud, placa, justificacion, estado)
                            solicitudes.addFirst(solicitud)
        except FileNotFoundError:
            print("El archivo 'Solicitudes_eliminar.txt' no fue encontrado.")
        return solicitudes


class Solicitud:
    def __init__(self, tipo, nombre, id_investigador, equipo, monto, fecha, estado):
        self.tipo = tipo
        self.nombre = nombre
        self.id_investigador = id_investigador
        self.equipo = equipo
        self.monto = monto
        self.fecha = fecha
        self.estado = estado

    def __str__(self):
        return f"{self.tipo} {self.id_investigador} {self.nombre} {self.equipo} {self.monto} {self.fecha} {self.estado}"

class SolicitudEliminar:
    def __init__(self, tipo, nombre, id_investigador, placa, justificacion, estado):
        self.tipo = tipo
        self.nombre = nombre
        self.id_investigador = id_investigador
        self.placa = placa
        self.justificacion = justificacion
        self.estado = estado
       
    def getTipo(self):
        return self.tipo

    def setTipo(self, tipo):
        self.tipo = tipo

    def getNombre(self):
        return self.nombre

    def setNombre(self, nombre):
        self.nombre = nombre

    def getIdInvestigador(self):
        return self.id_investigador

    def setIdInvestigador(self, id_investigador):
        self.id_investigador = id_investigador

    def getPlaca(self):
        return self.placa

    def setPlaca(self, placa):
        self.placa = placa

    def getJustificacion(self):
        return self.justificacion

    def setJustificacion(self, justificacion):
        self.justificacion = justificacion

    def getEstado(self):
        return self.estado

    def setEstado(self, estado):
        self.estado = estado

    def __str__(self):
        return f"{self.tipo} {self.id_investigador} {self.nombre} {self.placa} {self.justificacion} {self.estado}"

class Inventario:
    def __init__(self, nombre: str = "", _id: int =0, equipo:str = "", placa: int =0, fecha: Fecha=None, valor: int =0):
        self.nombre = nombre
        self._id = _id
        self.equipo = equipo
        self.placa = placa
        self.fecha = fecha
        self.valor = valor
    def setNombre(self, nombre):
        self.nombre = nombre

    def getNombre(self):
        return self.nombre

    def setId(self, _id):
        self._id = _id

    def getId(self):
        return self._id

    def setEquipo(self, equipo):
        self.equipo = equipo

    def getEquipo(self):
        return self.equipo

    def setPlaca(self, placa: int):
        self.placa = placa

    def getPlaca(self) -> int:
        return self.placa

    def setFecha(self, fecha):
        self.fecha = fecha

    def getFecha(self):
        return self.fecha

    def setValor(self, valor):
        self.valor = valor

    def getValor(self):
        return self.valor
    
    def __str__(self):
        return (f"{self.nombre} {self._id} {self.equipo} {self.placa} {self.fecha} {self.valor}\n")

# Clase principal del menú
class Menu:
    def __init__(self, root):
        self.root = root
        self.root.title("SGI Centro de Investigaciones")
        self.usuarios = self.cargar_usuarios()
        self.passwords = self.cargar_passwords()
        self.pantalla_login()

    def cargar_usuarios(self):
        usuarios = DoubleList()
        try:
            with open("Empleados.txt", "r") as archivo:
                for line in archivo:
                    datos = line.strip().split(" ")
                    nombre = datos[0]
                    cedula = int(datos[1])
                    fecha_nacimiento = Fecha(int(datos[2]), int(datos[3]), int(datos[4]))
                    ciudad_nacimiento = datos[5]
                    tel = int(datos[6])
                    email = datos[7]
                    direccion = Direccion(datos[8], datos[9], datos[10], datos[11], datos[12], datos[13])
                    usuario = Usuario(nombre, cedula, fecha_nacimiento, ciudad_nacimiento, tel, email, direccion)  
                    usuarios.addLast(usuario)
        except FileNotFoundError:
            messagebox.showerror("Error", "El archivo 'Empleados.txt' no se encontró.")
        return usuarios

    def cargar_passwords(self):
        passwords = {}
        try:
            with open("Password.txt", "r") as archivo:
                for linea in archivo:
                    id_usuario, password, rol = linea.strip().split(" ")
                    passwords[id_usuario] = {"password": password, "rol": rol}
            print(f"Passwords de la def cargar_passwords: {passwords}\n")
        except FileNotFoundError:
            messagebox.showerror("Error", "El archivo 'Password.txt' no se encontró.")
        return passwords
    
    def pantalla_login(self):
        # Limpiar la ventana
        for widget in self.root.winfo_children():
            widget.destroy()

        # Widgets de login
        tk.Label(self.root, text="Inicio de Sesión", font=("Arial", 16)).pack(pady=20)

        tk.Label(self.root, text="ID Usuario:").pack()
        self.entry_id = tk.Entry(self.root)
        self.entry_id.pack()

        tk.Label(self.root, text="Contraseña:").pack()
        self.entry_password = tk.Entry(self.root, show="*")
        self.entry_password.pack()

        tk.Button(self.root, text="Iniciar Sesión", command=self.validar_login).pack(pady=10)

    def validar_login(self):
        id_usuario = self.entry_id.get()
        password = self.entry_password.get()

        if id_usuario in self.passwords and self.passwords[id_usuario]["password"] == password:
            rol = self.passwords[id_usuario]["rol"]
            self.mostrar_menu(rol, id_usuario)
        else:
            messagebox.showerror("Error", "ID o contraseña incorrectos.")

    def mostrar_menu(self, rol, id_usuario):
        # Limpiar la ventana
        for widget in self.root.winfo_children():
            widget.destroy()

        if rol == "administrador":
            nombre = self.usuarios.search_by_id(int(id_usuario)).getNombre()
            self.usuario = Administrador(id_usuario, nombre, self.usuarios, self.passwords)
            self.mostrar_menu_admin()
        elif rol == "investigador":
            nombre = self.usuarios.search_by_id(int(id_usuario)).getNombre()
            self.usuario = Investigador(id_usuario, nombre)
            self.mostrar_menu_investigador()

    def mostrar_menu_admin(self):
        tk.Label(self.root, text="Menú Administrador", font=("Arial", 16)).pack(pady=20)

        # Opciones para Administrador
        tk.Button(self.root, text="Registrar Usuario", command=self.ejecutar_programa_1).pack(pady=10)
        tk.Button(self.root, text="Eliminar Usuario", command=self.ejecutar_programa_2).pack(pady=10)
        tk.Button(self.root, text="Cambiar Contraseña", command=self.ejecutar_programa_3).pack(pady=10)
        tk.Button(self.root, text="Responder Solicitudes de nuevos equipos", command=self.ejecutar_programa_4).pack(pady=10)
        tk.Button(self.root, text="Responder Solicitudes de eliminar equipos", command=self.ejecutar_programa_12).pack(pady=10)
        tk.Button(self.root, text="Listar Equipos", command=self.ejecutar_programa_9).pack(pady=10)
        tk.Button(self.root, text="Inventario Investigador", command=self.ejecutar_programa_10).pack(pady=10)
        tk.Button(self.root, text="Inventario General", command=self.ejecutar_programa_11).pack(pady=10)
        tk.Button(self.root, text="Consultar Control de Cambios", command=self.ejecutar_programa_13).pack(pady=10)
        tk.Button(self.root, text="Cerrar Sesión", command=self.cerrar_sesion).pack(pady=10)

    def mostrar_menu_investigador(self):
        tk.Label(self.root, text="Menú Investigador", font=("Arial", 16)).pack(pady=20)

        # Opciones para Investigador
        tk.Button(self.root, text="Listar Equipos", command=self.ejecutar_programa_5).pack(pady=10)
        tk.Button(self.root, text="Adicionar equipo", command=self.ejecutar_programa_6).pack(pady=10)
        tk.Button(self.root, text="Eliminar equipo", command=self.ejecutar_programa_7).pack(pady=10)
        tk.Button(self.root, text="Consultar Estado de Solicitudes", command=self.ejecutar_programa_8).pack(pady=10)
        tk.Button(self.root, text="Cerrar Sesión", command=self.cerrar_sesion).pack(pady=10)

    def regresar_menu_investigador(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        self.mostrar_menu_investigador()

    def regresar_menu_admin(self):
        for widget in self.root.winfo_children():
            if isinstance(widget, tk.Frame) or isinstance(widget, tk.Canvas):
                widget.destroy() 
        for widget in self.root.winfo_children():
            widget.destroy()

        self.mostrar_menu_admin()

    #Registrar usuario
    def ejecutar_programa_1(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        # Crear un contenedor con scroll
        frame_con_scroll = tk.Frame(self.root)
        frame_con_scroll.pack(fill=tk.BOTH, expand=True)

        canvas = tk.Canvas(frame_con_scroll)
        scrollbar = tk.Scrollbar(frame_con_scroll, orient=tk.VERTICAL, command=canvas.yview)
        scrollable_frame = tk.Frame(canvas)

        scrollable_frame.bind(
            "<Configure>",
            lambda e: canvas.configure(scrollregion=canvas.bbox("all"))
        )

        canvas.create_window((0, 0), window=scrollable_frame, anchor="nw")
        canvas.configure(yscrollcommand=scrollbar.set)

        canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        # Crear los campos para el registro de usuario dentro del frame desplazable
        tk.Label(scrollable_frame, text="Registrar Usuario", font=("Arial", 16)).pack(pady=10)

        tk.Label(scrollable_frame, text="Nombre:").pack()
        entry_nombre = tk.Entry(scrollable_frame)
        entry_nombre.pack(pady=5)

        tk.Label(scrollable_frame, text="ID Usuario:").pack()
        entry_id = tk.Entry(scrollable_frame)
        entry_id.pack(pady=5)

        tk.Label(scrollable_frame, text="Día de nacimiento (DD):").pack()
        entry_dia = tk.Entry(scrollable_frame)
        entry_dia.pack(pady=5)

        tk.Label(scrollable_frame, text="Mes de nacimiento (MM):").pack()
        entry_mes = tk.Entry(scrollable_frame)
        entry_mes.pack(pady=5)

        tk.Label(scrollable_frame, text="Año de nacimiento (AAAA):").pack()
        entry_anio = tk.Entry(scrollable_frame)
        entry_anio.pack(pady=5)

        tk.Label(scrollable_frame, text="Ciudad de nacimiento:").pack()
        entry_ciudad_nac = tk.Entry(scrollable_frame)
        entry_ciudad_nac.pack(pady=5)

        tk.Label(scrollable_frame, text="Teléfono:").pack()
        entry_telefono = tk.Entry(scrollable_frame)
        entry_telefono.pack(pady=5)

        tk.Label(scrollable_frame, text="Email:").pack()
        entry_email = tk.Entry(scrollable_frame)
        entry_email.pack(pady=5)

        tk.Label(scrollable_frame, text="Calle:").pack()
        entry_calle = tk.Entry(scrollable_frame)
        entry_calle.pack(pady=5)

        tk.Label(scrollable_frame, text="Nomenclatura:").pack()
        entry_nomenclatura = tk.Entry(scrollable_frame)
        entry_nomenclatura.pack(pady=5)

        tk.Label(scrollable_frame, text="Edificio:").pack()
        entry_edificio = tk.Entry(scrollable_frame)
        entry_edificio.pack(pady=5)

        tk.Label(scrollable_frame, text="Apto:").pack()
        entry_apto = tk.Entry(scrollable_frame)
        entry_apto.pack(pady=5)

        tk.Label(scrollable_frame, text="Barrio:").pack()
        entry_barrio = tk.Entry(scrollable_frame)
        entry_barrio.pack(pady=5)

        tk.Label(scrollable_frame, text="Ciudad:").pack()
        entry_ciudad = tk.Entry(scrollable_frame)
        entry_ciudad.pack(pady=5)

        tk.Label(scrollable_frame, text="Contraseña:").pack()
        entry_password = tk.Entry(scrollable_frame, show="*")
        entry_password.pack(pady=5)

        tk.Label(scrollable_frame, text="Rol:").pack()
        entry_rol = tk.Entry(scrollable_frame)
        entry_rol.pack(pady=5)

        # Botón para registrar usuario
        def registrar_usuario():
            try:
                nombre = entry_nombre.get()
                id_usuario = int(entry_id.get())
                dia = int(entry_dia.get())
                mes = int(entry_mes.get())
                anio = int(entry_anio.get())
                ciudad_nac = entry_ciudad_nac.get()
                telefono = int(entry_telefono.get())
                email = entry_email.get()
                calle = entry_calle.get()
                nomenclatura = entry_nomenclatura.get()
                edificio = entry_edificio.get()
                apto = entry_apto.get()
                barrio = entry_barrio.get()
                ciudad = entry_ciudad.get()
                password = entry_password.get()
                rol = entry_rol.get()

                fecha_nacimiento = Fecha(dia, mes, anio)
                direccion = Direccion(calle, nomenclatura, edificio, apto, barrio, ciudad)
                usuario = Usuario(nombre, id_usuario, fecha_nacimiento, ciudad_nac, telefono, email, direccion)
                
                self.usuario.registrar_usuario(usuario, password, rol)
                messagebox.showinfo("Éxito", "Usuario registrado con éxito.")
            except Exception as e:
                messagebox.showerror("Error", f"Ha ocurrido un error: {e}")

        tk.Button(scrollable_frame, text="Registrar Usuario", command=registrar_usuario).pack(pady=20)

        tk.Button(scrollable_frame, text="Regresar al Menú", command=self.regresar_menu_admin).pack(pady=10)


    # Eliminar Usuario
    def ejecutar_programa_2(self):
        self.root.title("Eliminar Usuario")
        for widget in self.root.winfo_children():
            widget.destroy()
        
        tk.Label(self.root, text="Eliminar Usuario", font=("Helvetica", 16)).pack(pady=10)
        
        tk.Label(self.root, text="ID del usuario a eliminar:").pack()
        entry_id_eliminar = tk.Entry(self.root)
        entry_id_eliminar.pack(pady=5)
        
        label_status = tk.Label(self.root, text="", fg="red")
        label_status.pack(pady=5)
        
        def eliminar():
            user_id = entry_id_eliminar.get()
            print(f"Eliminando usuario con ID {str(user_id)}...\n")
            self.passwords = self.cargar_passwords()
            if user_id.isdigit():
                try:
                    self.usuario.eliminar_usuario(self.usuarios, self.passwords, int(user_id))
                    if str(user_id) not in self.usuario.contrasenas.keys():
                        label_status.config(text="Usuario eliminado con éxito", fg="green")
                except Exception as e:
                    label_status.config(text="Usuario no encontrado", fg="red")
                    messagebox.showerror("Error", "El usuario no existe.")
            else:
                label_status.config(text="Por favor, ingrese un ID válido", fg="red")
        
        tk.Button(
            self.root,
            text="Eliminar Usuario",
            command=eliminar,
            bg="red",
            #fg="white"
        ).pack(pady=10)
        
        tk.Button(self.root, text="Regresar al Menú", command=self.regresar_menu_admin).pack(pady=5)

    #Cambiar Contraseña
    def ejecutar_programa_3(self):
        self.root.title("Cambiar Contraseña")
        for widget in self.root.winfo_children():
            widget.destroy()
        
        tk.Label(self.root, text="Cambiar Contraseña", font=("Helvetica", 16)).pack(pady=10)
        
        tk.Label(self.root, text="ID del usuario:").pack()
        entry_id_cambiar = tk.Entry(self.root)
        entry_id_cambiar.pack(pady=5)
        
        tk.Label(self.root, text="Nueva Contraseña:").pack()
        entry_password = tk.Entry(self.root, show="*")
        entry_password.pack(pady=5)
        
        label_status = tk.Label(self.root, text="", fg="red")
        label_status.pack(pady=5)
        
        def cambiar_password():
            user_id = entry_id_cambiar.get()
            new_password = entry_password.get()
            
            if user_id.isdigit() and new_password:
                if str(user_id) in self.passwords:
                    self.usuario.cambiar_password(self.passwords, int(user_id), new_password)
                    label_status.config(text="Contraseña cambiada con éxito", fg="green")
                else:
                    label_status.config(text="Usuario no encontrado", fg="red")
            else:
                label_status.config(text="Por favor, complete todos los campos correctamente", fg="red")
        
        tk.Button(
            self.root,
            text="Cambiar Contraseña",
            command=cambiar_password,
            bg="blue",
            #fg="white"
        ).pack(pady=10)
        
        tk.Button(self.root, text="Regresar", command=self.regresar_menu_admin).pack(pady=5)
    
    #Responder Solicitudes de Agregar Equipos
    def ejecutar_programa_4(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.root.title("Responder Solicitudes de Agregar Equipos")

        tk.Label(self.root, text="Solicitudes de Agregar Equipos", font=("Helvetica", 16)).pack(pady=10)

        solicitudes, datos, line = self.usuario.responder_solicitudes_agregar()

        text_equipos = tk.Text(self.root, width=100, height=15)
        text_equipos.pack(pady=10)
        
        # Insertar la lista de equipos en el widget Text
        text_equipos.insert(tk.END, solicitudes)
        text_equipos.config(state=tk.DISABLED)        
        
        def aceptar_solicitud(datos=datos, line=line):
            self.usuario.registrar_control_de_cambio(datos[0], datos[3], "Agrega")
            self.usuario.actualizar_estado_solicitud("Solicitudes_agregar.txt", line, "Aceptada")
            messagebox.showinfo("Éxito", f"Solicitud para el equipo {datos[2]} aprobada.")
        
        def rechazar_solicitud(line=line):
            self.usuario.registrar_control_de_cambio(datos[0], datos[3], "Agrega")
            self.usuario.actualizar_estado_solicitud("Solicitudes_agregar.txt", line, "Rechazada")
            messagebox.showinfo("Información", "Solicitud rechazada.")


        tk.Button(self.root, text="Regresar al Menú", command=self.regresar_menu_admin).pack(pady=10)
        tk.Button(self.root, text="Aceptar", command=aceptar_solicitud, bg="green").pack(side=tk.LEFT, padx=10)
        tk.Button(self.root, text="Rechazar", command=rechazar_solicitud, bg="red").pack(side=tk.LEFT, padx=10)
        tk.Button(self.root, text="Generar archivo", command=self.usuario.generar_archivo_solicitudes_pendientes, bg="green").pack(side=tk.LEFT, padx=10)

    def ejecutar_programa_12(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        self.root.title("Responder Solicitudes de Eliminar Equipos")

        tk.Label(self.root, text="Solicitudes de Eliminar Equipos", font=("Helvetica", 16)).pack(pady=10)

        solicitudes, datos, line = self.usuario.responder_solicitudes_eliminar()

        text_equipos = tk.Text(self.root, width=100, height=15)
        text_equipos.pack(pady=10)
        
        # Insertar la lista de equipos en el widget Text
        text_equipos.insert(tk.END, solicitudes)
        text_equipos.config(state=tk.DISABLED)        
        
        def aceptar_solicitud(datos=datos, line=line):
            self.usuario.registrar_control_de_cambio(datos[0], datos[3], "Elimina Equipo")
            self.usuario.actualizar_estado_solicitud_eliminar("Solicitudes_eliminar.txt", line, "Aceptada")
            messagebox.showinfo("Éxito", f"Solicitud para el equipo {datos[2]} aprobada.")
        
        def rechazar_solicitud(line=line):
            self.usuario.registrar_control_de_cambio(datos[0], datos[3], "Elimina Equipo")
            self.usuario.actualizar_estado_solicitud_eliminar("Solicitudes_eliminar.txt", line, "Rechazada")
            messagebox.showinfo("Información", "Solicitud rechazada.")


        tk.Button(self.root, text="Regresar al Menú", command=self.regresar_menu_admin).pack(pady=10)
        tk.Button(self.root, text="Aceptar", command=aceptar_solicitud, bg="green").pack(side=tk.LEFT, padx=10)
        tk.Button(self.root, text="Rechazar", command=rechazar_solicitud, bg="red").pack(side=tk.LEFT, padx=10)
        tk.Button(self.root, text="Generar archivo", command=self.usuario.generar_archivo_solicitudes_pendientes_eliminar, bg="green").pack(side=tk.LEFT, padx=10)


    #Listar Equipos
    def ejecutar_programa_5(self):
        # Limpiar la ventana actual (el menú)
        for widget in self.root.winfo_children():
            widget.destroy()

        label_equipos = tk.Label(self.root, text="Listar Equipos:", font=("Arial", 14))
        label_equipos.pack(pady=10)
        
        # Obtener la lista de equipos del investigador
        id_investigador = self.usuario.cedula
        equipos_lista,_ = self.usuario.listar_equipos(id_investigador)
        
        text_equipos = tk.Text(self.root, width=100, height=15)
        text_equipos.pack(pady=10)
        
        text_equipos.insert(tk.END, equipos_lista)
        text_equipos.config(state=tk.DISABLED)  # Para que el usuario no pueda editar el texto

        btn_generar_archivo = tk.Button(self.root, text="Generar archivo de equipos", command=self.generar_archivo)
        btn_generar_archivo.pack(pady=10)

        btn_regresar = tk.Button(self.root, text="Regresar al Menú", command=self.regresar_menu_investigador)
        btn_regresar.pack(pady=10)

#
    def generar_archivo(self):
        archivo_generado = self.usuario.generar_archivo() 
        if archivo_generado.endswith(".txt"):
            messagebox.showinfo("Éxito", f"El archivo '{archivo_generado}' ha sido generado con éxito.")
        else:
            messagebox.showerror("Error", f"No se pudo generar el archivo: {archivo_generado}")

    def ejecutar_programa_13(self):
        # Limpiar la ventana actual (el menú)
        for widget in self.root.winfo_children():
            widget.destroy()

        label_equipos = tk.Label(self.root, text="Equipos Listados:", font=("Arial", 14))
        label_equipos.pack(pady=10)
        
        # Obtener la lista de equipos del investigador
        control_cambios = self.usuario.consultar_control_de_cambio()
        
        text_equipos = tk.Text(self.root, width=100, height=15)
        text_equipos.pack(pady=10)
        
        text_equipos.insert(tk.END, control_cambios)
        text_equipos.config(state=tk.DISABLED) 

        btn_generar_archivo = tk.Button(self.root, text="Generar archivo de Control de Cambios", command=self.usuario.generar_archivo_control_de_cambio)
        btn_generar_archivo.pack(pady=10)

        btn_regresar = tk.Button(self.root, text="Regresar al Menú", command=self.regresar_menu_admin)
        btn_regresar.pack(pady=10)


    #
    def ejecutar_programa_6(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Adicionar Equipo", font=("Arial", 16)).pack(pady=10)

        tk.Label(self.root, text="Nombre del Equipo:").pack()
        entry_nombre = tk.Entry(self.root)
        entry_nombre.pack(pady=5)

        tk.Label(self.root, text="Placa del Equipo:").pack()
        entry_placa = tk.Entry(self.root)
        entry_placa.pack(pady=5)

        tk.Label(self.root, text="Fecha de Compra (DD-MM-YYYY):").pack()
        entry_fecha = tk.Entry(self.root)
        entry_fecha.pack(pady=5)

        tk.Label(self.root, text="Valor del Equipo:").pack()
        entry_valor = tk.Entry(self.root)
        entry_valor.pack(pady=5)

        def enviar_solicitud():
            nombre = entry_nombre.get()
            placa = entry_placa.get()
            fecha_compra = entry_fecha.get()
            valor = int(entry_valor.get())
            dia, mes, año = map(int, fecha_compra.split("-"))
            fecha = Fecha(dia, mes, año)  

            self.usuario.solicitar_agregar_equipo(nombre, placa, fecha, valor)
            messagebox.showinfo("Éxito", "Solicitud de adicionar equipo enviada con éxito.")
            self.regresar_menu_investigador()

        tk.Button(self.root, text="Enviar Solicitud", command=enviar_solicitud).pack(pady=10)

        tk.Button(self.root, text="Regresar al Menú", command=self.regresar_menu_investigador).pack(pady=10)

    def ejecutar_programa_7(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Eliminar Equipo", font=("Arial", 16)).pack(pady=10)

        tk.Label(self.root, text="Placa del Equipo:").pack()
        entry_placa = tk.Entry(self.root)
        entry_placa.pack(pady=5)

        tk.Label(self.root, text="Justificación para Eliminar:").pack()
        entry_justificacion = tk.Entry(self.root)
        entry_justificacion.pack(pady=5)

        def enviar_solicitud():
            placa = entry_placa.get()
            justificacion = entry_justificacion.get()

            self.usuario.solicitar_eliminar_equipo(placa, justificacion)
            messagebox.showinfo("Éxito", "Solicitud de eliminar equipo enviada con éxito.")
            self.regresar_menu_investigador()

        tk.Button(self.root, text="Enviar Solicitud", command=enviar_solicitud).pack(pady=10)

        tk.Button(self.root, text="Regresar al Menú", command=self.regresar_menu_investigador).pack(pady=10)
    
    def ejecutar_programa_8(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        tk.Label(self.root, text="Solicitudes Realizadas", font=("Arial", 16)).pack(pady=20)

        solicitudes = self.usuario.consultar_estado_solicitudes()

        text_solicitudes = tk.Text(self.root, width=100, height=15)
        text_solicitudes.pack(pady=10)

        text_solicitudes.insert(tk.END, solicitudes)
        text_solicitudes.config(state=tk.DISABLED)  

        tk.Button(self.root, text="Regresar al Menú", command=self.regresar_menu_investigador).pack(pady=10)
        
        btn_generar_archivo = tk.Button(self.root, text="Generar archivo de solicitudes", command=self.usuario.generar_archivo_solicitudes)
        btn_generar_archivo.pack(pady=10)

    def ejecutar_programa_9(self):
        for widget in self.root.winfo_children():
            widget.destroy()

        label_equipos = tk.Label(self.root, text="Equipos Listados:", font=("Arial", 14))
        label_equipos.pack(pady=10)
        
        id_investigador = self.usuario.cedula
        equipos_lista,_ = self.usuario.listar_equipos(id_investigador)
        if equipos_lista == "":
            equipos_lista = "No hay equipos registrados."
        text_equipos = tk.Text(self.root, width=100, height=15)
        text_equipos.pack(pady=10)
        
        text_equipos.insert(tk.END, equipos_lista)
        text_equipos.config(state=tk.DISABLED) 

        btn_generar_archivo = tk.Button(self.root, text="Generar archivo de equipos", command=self.generar_archivo)
        btn_generar_archivo.pack(pady=10)

        btn_regresar = tk.Button(self.root, text="Regresar al Menú", command=self.regresar_menu_admin)
        btn_regresar.pack(pady=10)

    def ejecutar_programa_10(self):
        for widget in self.root.winfo_children():
            widget.destroy()
        
        tk.Label(self.root, text="Listar Inventario Investigador", font=("Arial", 16)).pack(pady=10)
        
        tk.Label(self.root, text="Id del Investigador:").pack()
        id_invetigador = tk.Entry(self.root)
        id_invetigador.pack(pady=5)
        
        label_status = tk.Label(self.root, text="", fg="red")
        label_status.pack(pady=5)

        
        # Botón para eliminar usuario
        def generar_inventario():
            user_id = id_invetigador.get()
            if user_id.isdigit():
                user_id = int(user_id)
                equipos_lista = self.usuario.obtener_inventario_investigador(user_id)
                if equipos_lista != "":
                    label_status.config(text="Inverario generado con exito para", fg="green")
                else:
                    label_status.config(text="No hay equipos registrados para el investigador.", fg="red")
            else:
                label_status.config(text="Por favor, ingrese un ID válido", fg="red")
        
        tk.Button(
            self.root,
            text="Generar Inventario",
            command=generar_inventario,
            bg="red",
            #fg="white"
        ).pack(pady=10)


        btn_regresar = tk.Button(self.root, text="Regresar al Menú", command=self.regresar_menu_admin)
        btn_regresar.pack(pady=10)

    def ejecutar_programa_11(self):
        # Limpiar la ventana actual (el menú)
        for widget in self.root.winfo_children():
            widget.destroy()
        
        tk.Label(self.root, text="Listar Inventario General", font=("Arial", 16)).pack(pady=10)
        
        label_status = tk.Label(self.root, text="", fg="red")
        label_status.pack(pady=5)

        
        # Botón para eliminar usuario
        def generar_inventario_general():

            equipos_lista = self.usuario.cargar_inventario()
            if equipos_lista.isEmpty():
                label_status.config(text="No registros en el inventario.", fg="red")
            else:
                label_status.config(text="Inverario generado con exito", fg="green")

        tk.Button(
            self.root,
            text="Generar Inventario General",
            command=generar_inventario_general,
            bg="red",
            #fg="white"
        ).pack(pady=10)


        btn_regresar = tk.Button(self.root, text="Regresar al Menú", command=self.regresar_menu_admin)
        btn_regresar.pack(pady=10)

    def cerrar_sesion(self):
        # Volver al login
        self.pantalla_login()


# Función principal que configura la ventana de Tkinter
def main():
    root = tk.Tk()
    menu = Menu(root)
    root.mainloop()


if __name__ == "__main__":
    main()
