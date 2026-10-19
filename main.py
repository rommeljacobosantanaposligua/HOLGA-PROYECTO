from modelos.Docente import Docente
from modelos.Aula import Aula
from modelos.Materia import Materia
from modelos.Paralelo import Paralelo
from modelos.Franja_Horaria import FranjaHoraria
from controladores.Gestor_Horarios import GestorHorarios

# 📗 Funciones: Función externa a las clases
def imprimir_resumen(entidad):
    # Aquí aplicamos polimorfismo desde una función: no importa qué entidad sea,
    # todas heredan de IEntidadAcademica e implementan mostrar_info().
    print(entidad.mostrar_info())

def main():
    print("=========================================================")
    print("       SISTEMA HOLGA (Gestión de Horarios Académicos)   ")
    print("       Facultad de Ciencias de la Vida y Tecnologías     ")
    print("=========================================================\n")

    # 1. Instanciamos entidades base
    docente1 = Docente("Jharol Ormaza", 20)
    aula_lab = Aula("Laboratorio TI", 30)
    aula_comun = Aula("Bloque B - 101", 15)

    # 2. Uso del Property Setter (Cambiamos el nombre)
    docente1.nombre = "Ing. Jharol Antonio Ormaza"

    # 3. Demostración de Polimorfismo
    print("--- DEMOSTRACIÓN DE POLIMORFISMO ---")
    imprimir_resumen(docente1)
    imprimir_resumen(aula_lab)

    materia1 = Materia("Programación Orientada a Objetos", 4, 3)
    paralelo1 = Paralelo("Tercero A")
    franja1 = FranjaHoraria("Lunes", "07:00", "09:00")
    franja_conflicto = FranjaHoraria("Lunes", "08:00", "10:00")

    imprimir_resumen(materia1)
    imprimir_resumen(paralelo1)
    imprimir_resumen(franja1)

    # 4. Uso de método de clase
    print(f"\nTotal de docentes registrados (Método de Clase): {Docente.obtener_total_docentes()}\n")

    # 5. Iniciar el Gestor y validar asignaciones
    gestor = GestorHorarios()
    
    print("--- VALIDACIÓN DE HORARIOS Y ESPACIOS ---")
    
    # Intento 1: Exitoso por capacidad
    exito1 = gestor.asignar_clase(docente1, aula_lab, 25, materia1, paralelo1, franja1)
    print(f"[Asignación 1] 25 alumnos al Laboratorio TI (Cap. 30): {'Aprobado' if exito1 else 'Rechazado'}")
    
    # Intento 2: Fallido por validación de capacidad (Espacio insuficiente)
    exito2 = gestor.asignar_clase(docente1, aula_comun, 25)
    print(f"[Asignación 2] 25 alumnos a Bloque B (Cap. 15): {'Aprobado' if exito2 else 'Rechazado por conflicto de espacio'}")

    # Intento 3: Conflicto de horario del docente / aula (Solapamiento de franjas)
    materia2 = Materia("Estructura de Datos", 4, 3)
    exito3 = gestor.asignar_clase(docente1, aula_lab, 20, materia2, paralelo1, franja_conflicto)
    print(f"[Asignación 3] Cruce de horario Lunes (07:00-09:00 vs 08:00-10:00): {'Aprobado' if exito3 else 'Rechazado por cruce de horario'}")

    # 6. Consultas y Filtros del Sistema HOLGA
    print("\n--- CONSULTAS Y FILTROS ACADÉMICOS ---")
    clases_docente = gestor.consultar_por_docente(docente1)
    print(f"Clases asignadas a {docente1.nombre}: {len(clases_docente)}")
    for c in clases_docente:
        print(f" -> {c['detalle']}")

    print(f"\nResumen final del paralelo: {paralelo1.mostrar_info()}")

if __name__ == "__main__":
    main()

