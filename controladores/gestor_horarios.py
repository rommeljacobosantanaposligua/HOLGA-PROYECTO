from controladores.validador import Validador

class GestorHorarios:
    def __init__(self):
        # Almacena las asignaciones realizadas en el sistema
        self.asignaciones = []

    # 📗 Acoplamiento: Hay BAJO acoplamiento porque no creamos al 'docente' o 'aula' aquí adentro,
    # sino que los recibimos como parámetros (inyección de dependencias). Si Docente cambia, Gestor no se rompe.
    def asignar_clase(self, docente, aula, cantidad_estudiantes, materia=None, paralelo=None, franja_horaria=None):
        """
        Asigna una clase validando:
        1. Capacidad del aula vs cantidad de estudiantes.
        2. Cruce de horario del docente (no dictar dos clases a la misma hora).
        3. Cruce de horario del aula (no asignar dos clases al mismo espacio al mismo tiempo).
        4. Cruce de horario del paralelo (no programar dos materias simultáneas para el mismo curso).
        """
        # 1. Validación de capacidad
        if not Validador.verificar_capacidad(aula, cantidad_estudiantes):
            return False

        # 2. Validación de conflicto en franja horaria (si se proporciona)
        if franja_horaria:
            if Validador.verificar_conflicto_docente(self.asignaciones, docente, franja_horaria):
                return False
            if Validador.verificar_conflicto_aula(self.asignaciones, aula, franja_horaria):
                return False
            if paralelo and Validador.verificar_conflicto_paralelo(self.asignaciones, paralelo, franja_horaria):
                return False

        # Si el paralelo y la materia existen, asociamos la materia al paralelo
        if paralelo and materia:
            paralelo.agregar_materia(materia)

        # Guardamos el registro estructurado
        registro = {
            "docente": docente,
            "aula": aula,
            "cantidad_estudiantes": cantidad_estudiantes,
            "materia": materia,
            "paralelo": paralelo,
            "franja": franja_horaria,
            "detalle": (
                f"{docente.nombre} | {materia.nombre if materia else 'Clase general'} | "
                f"Paralelo: {paralelo.nombre if paralelo else 'N/A'} | "
                f"{aula.mostrar_info()} | "
                f"{franja_horaria.mostrar_info() if franja_horaria else 'Sin franja asignada'}"
            )
        }
        self.asignaciones.append(registro)
        return True

    # 📙 Consultas y filtros personalizados (Alcance del proyecto HOLGA)
    def consultar_por_docente(self, docente):
        """Filtra y retorna las asignaciones de un docente específico."""
        return [a for a in self.asignaciones if a.get("docente") == docente]

    def consultar_por_aula(self, aula):
        """Filtra y retorna las asignaciones en una aula específica."""
        return [a for a in self.asignaciones if a.get("aula") == aula]

    def consultar_por_paralelo(self, paralelo):
        """Filtra y retorna las asignaciones de un paralelo específico."""
        return [a for a in self.asignaciones if a.get("paralelo") == paralelo]

