# Definir la clase Alumno
class Alumno:
    # Constructor de la clase
    def __init__(self, nombre, apellido, edad, nacionalidad):
        self.nombre = nombre # Atributo nombre
        self.apellido = apellido # Atributo apellido
        self.edad = edad # Atributo edad
        self.nacionalidad = nacionalidad # Atributo nacionalidad
        self.nota = None # Atributo nota, inicialmente None

    # Método para leer la nota del alumno
    def leerNota(self):
        return self.nota

    # Método para registrar la nota del alumno
    def registrarNota(self, notaAlumno):
        # Validar que la nota sea un número entre 0 y 20
        if isinstance(notaAlumno, int) or isinstance(notaAlumno, float):
            if notaAlumno >= 0 and notaAlumno <= 20:
                self.nota = notaAlumno # Asignar la nota al atributo
            else:
                print("La nota debe estar entre 0 y 20") # Mostrar mensaje de error
        else:
            print("La nota debe ser un número") # Mostrar mensaje de error
