from modelos.Entidad_Base import IEntidadAcademica

class Paralelo(IEntidadAcademica):
    def __init__(self, nombre):
        self.__nombre = nombre
        # Lista privada para almacenar objetos de la clase Materia
        self.__materias_asignadas = []

    @property
    def nombre(self):
        return self.__nombre

    @property
    def materias(self):
        return list(self.__materias_asignadas)


    # 📗 Cohesión: El paralelo es el responsable de agregar materias a su propia lista
    def agregar_materia(self, materia):
        if materia not in self.__materias_asignadas:
            self.__materias_asignadas.append(materia)
            return True
        return False

    def obtener_total_horas(self):
        # Suma la carga horaria de todas las materias en este paralelo
        total = sum(materia.carga_horaria for materia in self.__materias_asignadas)
        return total

    # 📙 Polimorfismo
    def mostrar_info(self):
        info = f"Paralelo: {self.__nombre} | Total de materias: {len(self.__materias_asignadas)}"
        info += f" | Carga horaria total: {self.obtener_total_horas()}h"
        return info
