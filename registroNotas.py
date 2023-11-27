import pickle
from alumnos import Alumno


def main():
    alumnos_registrados = []

    print("Bienvenidos al registro de notas")

    while True:
        comando = input("Ingrese comando (R, C, P, S, X): ").upper()

        if comando == "R":
            nombre = input("Ingrese nombre del alumno: ")
            apellido = input("Ingrese apellido del alumno: ")
            edad = int(input("Ingrese edad del alumno: "))
            nacionalidad = input("Ingrese nacionalidad del alumno: ")

            nuevo_alumno = Alumno(nombre, apellido, edad, nacionalidad)
            alumnos_registrados.append(nuevo_alumno)

        elif comando == "C":
            for alumno in alumnos_registrados:
                nota_valida = False
                while not nota_valida:
                    try:
                        nota = int(
                            input(
                                f"Ingrese nota para {alumno.nombre} {alumno.apellido}: "
                            )
                        )
                        alumno.registrarNota(nota)
                        nota_valida = True
                    except ValueError:
                        print("Ingrese un valor numérico válido.")

        elif comando == "P":
            if alumnos_registrados:
                promedio = sum(
                    alumno.leerNota() for alumno in alumnos_registrados
                ) / len(alumnos_registrados)
                print(
                    f"El promedio de notas para {len(alumnos_registrados)} alumnos es: {promedio:.2f}"
                )
            else:
                print("No hay alumnos registrados.")

        elif comando == "S":
            if alumnos_registrados:
                suma_notas = sum(alumno.leerNota()
                                 for alumno in alumnos_registrados)
                print(
                    f"La suma de notas de {len(alumnos_registrados)} alumnos es: {suma_notas}"
                )
            else:
                print("No hay alumnos registrados.")

        elif comando == "X":
            with open("alumnos_data.pkl", "wb") as file:
                pickle.dump(alumnos_registrados, file)
            print("Programa finalizado.")
            break

        else:
            print("Comando no reconocido. Inténtelo de nuevo.")


if __name__ == "__main__":
    main()
