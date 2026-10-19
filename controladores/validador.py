# 📗 Cohesión: Esta clase tiene alta cohesión porque su único propósito es validar reglas de negocio.
class Validador:

    # 📙 Tipos de métodos: Método estático (staticmethod), no requiere 'self' ni instanciar la clase
    @staticmethod
    def verificar_capacidad(aula, cantidad_estudiantes):
        """Retorna True si el aula tiene capacidad suficiente para la cantidad de estudiantes."""
        return aula.capacidad >= cantidad_estudiantes

    @staticmethod
    def verificar_conflicto_docente(asignaciones, docente, franja_horaria):
        """
        Retorna True si el docente ya tiene una clase asignada que se cruce
        con la franja horaria solicitada.
        """
        if not franja_horaria:
            return False
        for asig in asignaciones:
            if asig.get("docente") == docente and asig.get("franja"):
                if asig["franja"].se_solapa_con(franja_horaria):
                    return True
        return False

    @staticmethod
    def verificar_conflicto_aula(asignaciones, aula, franja_horaria):
        """
        Retorna True si el aula ya está ocupada en un horario que se cruce
        con la franja horaria solicitada.
        """
        if not franja_horaria:
            return False
        for asig in asignaciones:
            if asig.get("aula") == aula and asig.get("franja"):
                if asig["franja"].se_solapa_con(franja_horaria):
                    return True
        return False

    @staticmethod
    def verificar_conflicto_paralelo(asignaciones, paralelo, franja_horaria):
        """
        Retorna True si el paralelo ya tiene una materia asignada que se cruce
        con la franja horaria solicitada.
        """
        if not franja_horaria or not paralelo:
            return False
        for asig in asignaciones:
            if asig.get("paralelo") == paralelo and asig.get("franja"):
                if asig["franja"].se_solapa_con(franja_horaria):
                    return True
        return False


