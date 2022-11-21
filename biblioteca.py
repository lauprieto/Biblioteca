import datetime
class Usuario ():
  def __init__(self):
    self.__Nombre=""
    self.__Cedula=""
    self.__Direccion=""
    self.__Telefono=""

  def GetNombre(self):
    return self.__Nombre

  def SetNombre(self, nombre):
    self.__Nombre=nombre
  
  def GetCedula(self):
    return self.__Cedula

  def SetCedula(self, cedula):
    self.__Cedula =cedula

  def GetDireccion(self):
    return self.__Direccion

  def SetDireccion(self, direccion):
    self.__Direccion=direccion

  def GetTelefono(self):
    return self.__Telefono

  def SetTelefono(self, telefono):
    self.__Telefono=telefono

bibliot=Usuario()
print("REGISTRO DE USUARIO EN BIBLIOTECA MUNICIPAL ")
bibliot.SetNombre(input("NOMBRE:\n"))
bibliot.SetCedula(input("CEDULA:\n"))
bibliot.SetDireccion(input("DIRECCION:\n"))
bibliot.SetTelefono(input("TELEFONO:\n"))

class Libro(Usuario):
  def __init__(self):
    self.__Titulo= ""
    self.__Autor=""

  def GetTitulo(self):
    return self.__Titulo

  def SetTitulo(self, titulo):
    self.__Titulo=titulo
  
  def GetAutor(self):
    return self.__Autor

  def SetAutor(self, autor):
    self.__Autor =autor

libro=Libro()
print("BIENVENIDO A LA BIBLIOTECA MUNICIPAL ")
libro.SetTitulo(input("TITULO:\n"))
libro.SetAutor(input("AUTOR:\n"))

class Persona(Libro):
  def __init__(self):
    self.__Isbn=""
    self.__Paginas=""
    self.__Edicion=""
    self.__Editorial=""
    self.__Lugar=""
    
  def GetIsbn(self):
   return self.__Isbn
  def SetIsbn(self,isbn):
    self.__Isbn =isbn

  def GetPaginas(self):
    return self.__Paginas
    
  def SetPaginas(self, paginas):
    self.__Paginas=paginas
    
  def GetEdicion(self):
    return self.__Edicion
  
  def SetEdicion(self,edicion):
    self.__Edicion=edicion

  def GetEditorial(self):
    return self.__Editorial
  def SetEditorial(self,editorial):
    self.__Editorial=editorial
  def GetLugar(self):
    return self.__Lugar
  def SetLugar(self,lugar):
    self.__Lugar=lugar

persona=Persona()
persona.SetIsbn(input("ISBN:"))
persona.SetPaginas(input("PAGINAS:"))
persona.SetEdicion(input("EDICION:"))
persona.SetEditorial(input("EDITORIAL:"))
persona.SetLugar(input("LUGAR :"))

class Fecha(Persona):
  def __init__(self):
    self.__Fechaedicion=""
  def GetFechaedicion(self):
    return self.__Fechaedicion
  def SetFechaedicion(self,fechaedicion):
    self.__Fechaedicion=fechaedicion

fecha=Fecha()
fecha.SetFechaedicion(input("FECHA DE EDICION:"))

class Prestar(Libro,Usuario):
  def datos (self):
        print("DESEAS PRESTAR UN LIBRO")
        print("1= si")
        print("2=no")
        libro= int(input("DIGITA LA OPCION DESEADA:"))

        if libro== 1:
            dep=(input("NOMBRE DEL LIBRO: "))
            actual =datetime.datetime.now()
            hora =datetime.datetime.now().hour
            min =datetime.datetime.now().minute
            seg =datetime.datetime.now().second
            print("FECHA DE ENTREGA: {}/{}/{}".format(actual.day,actual.month,actual.year))
            print("HORA DE ENTREGA: {}:{}:{}".format(actual.hour,actual.minute,actual.second))
            print("NOMBRE Y APELLIDOS:"(bibliot.GetNombre()))
            print("TELEFONO:"(bibliot.GetTelefono()))
            print("")
        else:
             if libro==2:
                print("FUE UN GUSTO PARA NOSOTROS ATENDERTE ATT:BIBLIOTECA")
                self.datos()

prestar=Prestar()
prestar.datos()