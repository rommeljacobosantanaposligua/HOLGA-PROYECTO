from modelos.Entidad_Base import IEntidadAcademica

# 📗 Herencia: Aula hereda de IEntidadAcademica
class Aula(IEntidadAcademica):
    def __init__(self, codigo, capacidad):
        self._codigo = codigo
        self._capacidad = capacidad

    @property
    def codigo(self):
        return self._codigo

    @property
    def capacidad(self):
        return self._capacidad

    # 📙 Polimorfismo: Misma función que en otras entidades, pero comportamiento propio
    def mostrar_info(self):
        return f"Aula: {self._codigo} | Capacidad: {self._capacidad} estudiantes"

