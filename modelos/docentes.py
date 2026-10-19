from modelos.entidad_base import IEntidadAcademica

#Crear clase / Herencia: Docente hereda de IEnt, caragaidadAcademica
#Programacion Orientada a Objetos: Modelamos algo de la vida real en codigo 
class Docente(IEntidadAcademica):

  #Tipos de metodos: Atributo estatico/de clase
  total_docentes = 0

  def_init_(self, nombre, carga_maxima):
    #Encapsulamiento: El doble guion bajo (__) hace que el atributo sea privado
    self.__nombre = nombre
    self.__carga_maxima = carga_maxima
    Docente.total_docentes += 1

  #Decorador Property: Permite acceder a un atributo privado como si fuera publico (Getter)
  @property
  def nombre(self):
    return self.__nombre

  #Setter del decorador property: Controla como se modifica el atributo privado 
  @nombre.setter
  def nombre(self, nuevo_nombre):
    if nuevo_nombre:
      self.__nombre = nuevo_nombre

  #Tipos de metodos: Metodo de clase (classmethod)
  @classmethod
  def obtener_total_docentes(cls):
    return cls.total_docentes

  #Polimorfismo: Sobreescribimos el metodo de la clase abstracta a nuestra manera
  def mostrar_info(self):
    return f"Docente: {self._nombre} | Carga Max: {self._carga_maxima} horas"




