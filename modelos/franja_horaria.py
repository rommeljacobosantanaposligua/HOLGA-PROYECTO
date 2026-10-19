from modelos.Entidad_Base import IEntidadAcademica

class FranjaHoraria(IEntidadAcademica):
    def __init__(self, dia, hora_inicio, hora_fin):
        self._dia = dia
        self._hora_inicio = hora_inicio
        self._hora_fin = hora_fin

    @property
    def dia(self):
        return self._dia

    @property
    def hora_inicio(self):
        return self._hora_inicio
        
    @property
    def hora_fin(self):
        return self._hora_fin

    def se_solapa_con(self, otra):
        """Verifica si dos franjas horarias coinciden en el mismo día y se cruzan en horas."""
        if self._dia.strip().lower() != otra.dia.strip().lower():
            return False
        return not (self._hora_fin <= otra.hora_inicio or self._hora_inicio >= otra.hora_fin)

    # 📙 Polimorfismo
    def mostrar_info(self):
        return f"Horario: {self._dia} de {self._hora_inicio} a {self._hora_fin}"

