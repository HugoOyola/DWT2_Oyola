# Importar la clase Alumno y la librería pickle
from alumnos import Alumno
import pickle

# Crear una lista vacía para almacenar los objetos Alumno
listaAlumnos = []

# Desplegar un mensaje inicial
print("Bienvenidos al registro de notas")

# Crear un bucle para esperar el ingreso de comandos
while True:
    # Pedir el ingreso de un comando
    comando = input("Ingrese comando (R, C, P, S, X): ")

    # Si el comando es R, registrar un alumno
    if comando == "R":
        # Pedir los datos del alumno
        nombre = input("Ingrese el nombre del alumno: ")
        apellido = input("Ingrese el apellido del alumno: ")
        edad = input("Ingrese la edad del alumno: ")
        nacionalidad = input("Ingrese la nacionalidad del alumno: ")

        # Crear un objeto Alumno con los datos ingresados
        alumno = Alumno(nombre, apellido, edad, nacionalidad)

        # Agregar el objeto Alumno a la lista
        listaAlumnos.append(alumno)

    # Si el comando es C, calificar a los alumnos
    elif comando == "C":
        # Recorrer la lista de alumnos
        for alumno in listaAlumnos:
            # Pedir el ingreso de la nota para cada alumno
            nota = input(f"Alumno {alumno.nombre} {alumno.apellido}, Ingrese nota: ")

            # Intentar convertir la nota a un número
            try:
                nota = float(nota)
            except:
                # Si no se puede convertir, asignar None
                nota = None

            # Registrar la nota del alumno usando el método de la clase
            alumno.registrarNota(nota)

    # Si el comando es P, obtener el promedio de notas
    elif comando == "P":
        # Crear una variable para almacenar la suma de notas
        suma = 0

        # Recorrer la lista de alumnos
        for alumno in listaAlumnos:
            # Sumar la nota de cada alumno a la variable suma
            suma += alumno.leerNota()

        # Calcular el promedio de notas dividiendo la suma por la cantidad de alumnos
        promedio = suma / len(listaAlumnos)

        # Mostrar el mensaje con el promedio de notas
        print(f"El promedio de notas para {len(listaAlumnos)} alumnos es: {promedio}")

    # Si el comando es S, obtener la suma de notas
    elif comando == "S":
        # Crear una variable para almacenar la suma de notas
        suma = 0

        # Recorrer la lista de alumnos
        for alumno in listaAlumnos:
            # Sumar la nota de cada alumno a la variable suma
            suma += alumno.leerNota()

        # Mostrar el mensaje con la suma de notas
        print(f"La suma de notas de {len(listaAlumnos)} alumnos es: {suma}")

    # Si el comando es X, terminar el programa
    elif comando == "X":
        # Guardar los objetos Alumno en un archivo usando pickle
        with open("alumnos.pkl", "wb") as archivo:
            pickle.dump(listaAlumnos, archivo)

        # Mostrar un mensaje de despedida
        print("Gracias por usar el registro de notas. Hasta pronto.")

        # Romper el bucle
        break

    # Si el comando no es válido, mostrar un mensaje de error
    else:
        print("Comando no válido. Por favor, ingrese R, C, P, S o X.")
