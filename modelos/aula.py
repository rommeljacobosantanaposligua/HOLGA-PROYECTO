from modelos.entidad_base import IEntidadAcademica
class Aula(IEntidadAcademica):
  def _init_
  self._codigo-codigo
  self._capacidad-capacidad
  @property
  def capacidad(self):
    retur self._capacidad
#polimorfismo: Misma funcion que en docente, pero comportamiento diferente
  def mostrar_info(self):
    return f"Aula:{self._codigo} | Capacidad:{self._capacidad}estudiantes"
