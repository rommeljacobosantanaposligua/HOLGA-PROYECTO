from modelos.docente import Docente
from modelos.aula import Aula
from controladores.gestor_horarios import GestorHorarios

# 📗 Funciones: Función externa a las clases
def imprimir_resumen(entidad):
    # Aquí aplicamos polimorfismo desde una función: no importa si es aula o docente,
    # ambos tienen mostrar_info() y Python sabrá cuál ejecutar.
    print(entidad.mostrar_info())

def main():
    print("--- INICIANDO SISTEMA HOLGA ---\n")

    # Instanciamos los objetos
    docente1 = Docente("Jharol Ormaza", 20)
    aula_lab = Aula("Laboratorio TI", 30)
    aula_comun = Aula("Bloque B - 101", 15)

    # Uso del Property Setter (Cambiamos el nombre)
    docente1.nombre = "Ing. Jharol Antonio Ormaza"

    # Ver polimorfismo en la función
    imprimir_resumen(docente1)
    imprimir_resumen(aula_lab)
    
    # Uso de método de clase
    print(f"El total de docentes registrados es: {Docente.obtener_total_docentes()}\n")

    # Iniciar el Gestor
    gestor = GestorHorarios()
    
    print("--- VALIDACIÓN DE HORARIOS Y ESPACIOS ---")
    
    # Intento 1: Exitoso
    exito1 = gestor.asignar_clase(docente1, aula_lab, 25)
    print(f"Asignación de 25 alumnos al Laboratorio (Cap. 30): {'Aprobado' if exito1 else 'Rechazado'}")
    
    # Intento 2: Fallido por validación (Acoplamiento y Cohesión en acción)
    exito2 = gestor.asignar_clase(docente1, aula_comun, 25)
    print(f"Asignación de 25 alumnos a Bloque B (Cap. 15): {'Aprobado' if exito2 else 'Rechazado por conflicto de espacio'}")

if __name__ == "__main__":
    main()
