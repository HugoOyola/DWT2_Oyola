class Alumno:
  def __init__(self, nombre, apellido, edad, nacionalidad, nota=0):
      self.nombre = nombre
      self.apellido = apellido
      self.edad = edad
      self.nacionalidad = nacionalidad
      self.nota = nota

  def leerNota(self):
      return self.nota

  def registrarNota(self, notaAlumno):
      if 0 <= notaAlumno <= 20:
          self.nota = notaAlumno
          print(f"Nota registrada para {self.nombre} {self.apellido}")
      else:
          print("La nota debe estar en un rango de 0 a 20. Inténtelo de nuevo.")