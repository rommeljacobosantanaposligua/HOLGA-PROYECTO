from modelos.Entidad_Base import IEntidadAcademica

# 📗 Crear clase / Herencia: Docente hereda de IEntidadAcademica
# Programación Orientada a Objetos: Modelamos algo de la vida real en código 
class Docente(IEntidadAcademica):

    # Tipos de métodos: Atributo estático / de clase
    total_docentes = 0

    def __init__(self, nombre, carga_maxima):
        # 📗 Encapsulamiento: El doble guion bajo (__) hace que el atributo sea privado
        self.__nombre = nombre
        self.__carga_maxima = carga_maxima
        Docente.total_docentes += 1

    # 📙 Decorador Property: Permite acceder a un atributo privado como si fuera público (Getter)
    @property
    def nombre(self):
        return self.__nombre

    # Setter del decorador property: Controla cómo se modifica el atributo privado 
    @nombre.setter
    def nombre(self, nuevo_nombre):
        if nuevo_nombre:
            self.__nombre = nuevo_nombre

    @property
    def carga_maxima(self):
        return self.__carga_maxima

    @carga_maxima.setter
    def carga_maxima(self, nueva_carga):
        if nueva_carga > 0:
            self.__carga_maxima = nueva_carga

    # Tipos de métodos: Método de clase (classmethod)
    @classmethod
    def obtener_total_docentes(cls):
        return cls.total_docentes

    # 📙 Polimorfismo: Sobreescribimos el método de la clase abstracta a nuestra manera
    def mostrar_info(self):
        return f"Docente: {self.__nombre} | Carga Max: {self.__carga_maxima} horas"





