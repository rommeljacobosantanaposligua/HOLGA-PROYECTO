from modelos.entidad_base import IEntidadAcademica

# 📗 Crear clase / 📙 Herencia
class Materia(IEntidadAcademica):
    def __init__(self, nombre, carga_horaria, nivel):
        # 📗 Encapsulamiento: Atributos privados
        self.__nombre = nombre
        self.__carga_horaria = carga_horaria
        self.__nivel = nivel

    # 📙 Decorador Property (Getters)
    @property
    def nombre(self):
        return self.__nombre

    @property
    def carga_horaria(self):
        return self.__carga_horaria

    @property
    def nivel(self):
        return self.__nivel

    # Setters para proteger la modificación de los datos
    @carga_horaria.setter
    def carga_horaria(self, horas):
        if horas > 0:
            self.__carga_horaria = horas
        else:
            raise ValueError("La carga horaria debe ser mayor a 0")

    # 📙 Polimorfismo: Adaptamos el método abstracto a esta clase
    def mostrar_info(self):
        return f"Materia: {self.__nombre} | Nivel: {self.__nivel} | Carga Horaria: {self.__carga_horaria}h"
