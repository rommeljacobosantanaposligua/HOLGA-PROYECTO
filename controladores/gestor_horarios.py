from controladores.validador import Validador

class GestorHorarios:
    def __init__(self):
        self.asignaciones = []

    # 📗 Acoplamiento: Hay BAJO acoplamiento porque no creamos al 'docente' o 'aula' aquí adentro,
    # sino que los recibimos como parámetros (inyección de dependencias). Si Docente cambia, Gestor no se rompe.
    def asignar_clase(self, docente, aula, cantidad_estudiantes):
        # Usamos el validador estático
        if Validador.verificar_capacidad(aula, cantidad_estudiantes):
            # Guardamos el registro
            self.asignaciones.append(f"{docente.nombre} dará clases a {cantidad_estudiantes} alumnos en el aula {aula.mostrar_info()}")
            return True
        else:
            return False
