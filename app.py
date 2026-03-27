import time

print("Yo Gym girly version")

plan_semanal = {}

# -------- FUNCIONES --------

def mostrar_dias():
    if not plan_semanal:
        print("No hay rutinas cargadas")
    else:
        print("Días con rutina:")
        for d in plan_semanal:
            print("-", d)

def mostrar_rutina(dia):
    if dia in plan_semanal:
        print("Rutina de", dia)
        for i, e in enumerate(plan_semanal[dia]):
            print(i, "-", e["nombre"], "-", e["series"], "x", e["reps"], "-", e["peso"], "kg",
                  "| descanso series:", e["descanso_series"], "seg",
                  "| descanso ejercicio:", e["descanso_ejercicio"], "seg")
    else:
        print("Ese día no existe")

def agregar_ejercicio(dia):
    nombre = input("Ejercicio: ").lower()
    series = int(input("Series: "))
    reps = int(input("Repeticiones: "))
    peso = float(input("Peso: "))
    descanso_series = int(input("Descanso entre series (segundos): "))
    descanso_ejercicio = int(input("Descanso entre ejercicios (segundos): "))

    ejercicio = {
        "nombre": nombre,
        "series": series,
        "reps": reps,
        "peso": peso,
        "descanso_series": descanso_series,
        "descanso_ejercicio": descanso_ejercicio
    }

    if dia in plan_semanal:
        plan_semanal[dia].append(ejercicio)
    else:
        plan_semanal[dia] = [ejercicio]

def editar_ejercicio(dia):
    if dia in plan_semanal:
        mostrar_rutina(dia)
        i = int(input("Número del ejercicio a editar: "))

        plan_semanal[dia][i]["series"] = int(input("Nuevas series: "))
        plan_semanal[dia][i]["reps"] = int(input("Nuevas reps: "))
        plan_semanal[dia][i]["peso"] = float(input("Nuevo peso: "))
        plan_semanal[dia][i]["descanso_series"] = int(input("Nuevo descanso entre series: "))
        plan_semanal[dia][i]["descanso_ejercicio"] = int(input("Nuevo descanso entre ejercicios: "))
    else:
        print("Ese día no existe")

def eliminar_ejercicio(dia):
    if dia in plan_semanal:
        mostrar_rutina(dia)
        i = int(input("Número del ejercicio a eliminar: "))
        plan_semanal[dia].pop(i)
    else:
        print("Ese día no existe")

def eliminar_dia():
    dia = input("Día a eliminar: ").lower()
    if dia in plan_semanal:
        del plan_semanal[dia]
        print("Día eliminado")
    else:
        print("Ese día no existe")

def borrar_todo():
    plan_semanal.clear()
    print("Se eliminó toda la rutina")

def empezar_rutina(dia):
    if dia in plan_semanal:
        print("Empezando rutina de", dia)

        for e in plan_semanal[dia]:
            print("\nEjercicio:", e["nombre"])

            for s in range(e["series"]):
                input(f"Serie {s+1} - presioná Enter cuando termines")
                print("Descansando...", e["descanso_series"], "segundos")
                time.sleep(e["descanso_series"])

            print("Descanso entre ejercicios...", e["descanso_ejercicio"], "segundos")
            time.sleep(e["descanso_ejercicio"])

        print("Rutina terminada.")
    else:
        print("Ese día no existe")

# -------- MENÚ --------

while True:
    print("\n1. Ver días")
    print("2. Ver rutina de un día")
    print("3. Agregar ejercicio")
    print("4. Editar ejercicio")
    print("5. Eliminar ejercicio")
    print("6. Eliminar día")
    print("7. Borrar toda la rutina")
    print("8. Empezar rutina")
    print("9. Salir")

    opcion = input("Elegí una opción: ")

    if opcion == "1":
        mostrar_dias()

    elif opcion == "2":
        dia = input("Día: ").lower()
        mostrar_rutina(dia)

    elif opcion == "3":
        dia = input("Día: ").lower()
        agregar_ejercicio(dia)

    elif opcion == "4":
        dia = input("Día: ").lower()
        editar_ejercicio(dia)

    elif opcion == "5":
        dia = input("Día: ").lower()
        eliminar_ejercicio(dia)

    elif opcion == "6":
        eliminar_dia()

    elif opcion == "7":
        borrar_todo()

    elif opcion == "8":
        dia = input("Día: ").lower()
        empezar_rutina(dia)

    elif opcion == "9":
        print("Hasta Pronto.")
        break

    else:
        print("Opción inválida")

        