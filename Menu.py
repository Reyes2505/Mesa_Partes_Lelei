import Expedientes as mod_exp
import listar_expedientes as mod_lis_exp
import buscar_expedientes as mod_bus_exp
import ordenar_expedientes as mod_ord_exp
import modificar_expediente as mod_mod_exp
import eliminar_expediente as mod_eli_exp
import actualizar_tramite as mod_act_tra

import registrar_calificaciones as mod_reg_cal
import listar_calificaciones as mod_lis_cal
import buscar_calificaciones as mod_bus_cal
import eliminar_calificaciones as mod_eli_cal

from Guardar_Expediente import guardar_expedientes

import padre as mod_padre
import madre as mod_madre
import estudiantes as mod_estudiantes
import familia as mod_familia


def ejecutar_principal(modulo, *args):
    for nombre, obj in vars(modulo).items():
        if callable(obj) and getattr(obj, "__module__", None) == modulo.__name__:
            try:
                return obj(*args)
            except TypeError:
                return obj(args[0])


def submenu_expedientes(expedientes, estudiantes):
    while True:
        print("\n===================================")
        print("       GESTIÓN DE EXPEDIENTES")
        print("===================================")
        print("1. Registrar expediente")
        print("2. Listar expedientes")
        print("3. Buscar expediente")
        print("4. Ordenar expedientes")
        print("5. Modificar expediente")
        print("6. Actualizar estado de trámite")
        print("7. Eliminar expediente")
        print("8. Volver al menú principal")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            ejecutar_principal(mod_exp, expedientes, estudiantes)
        elif opcion == "2":
            ejecutar_principal(mod_lis_exp, expedientes)
        elif opcion == "3":
            ejecutar_principal(mod_bus_exp, expedientes)
        elif opcion == "4":
            ejecutar_principal(mod_ord_exp, expedientes)
        elif opcion == "5":
            ejecutar_principal(mod_mod_exp, expedientes, estudiantes)
        elif opcion == "6":
            ejecutar_principal(mod_act_tra, expedientes)
        elif opcion == "7":
            ejecutar_principal(mod_eli_exp, expedientes)
        elif opcion == "8":
            break
        else:
            print("Opción no válida.")


def submenu_calificaciones(calificaciones, expedientes):
    while True:
        print("\n===================================")
        print("      GESTIÓN DE CALIFICACIONES")
        print("===================================")
        print("1. Registrar calificaciones")
        print("2. Listar calificaciones")
        print("3. Buscar calificaciones")
        print("4. Eliminar calificaciones")
        print("5. Volver al menú principal")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            ejecutar_principal(mod_reg_cal, calificaciones, expedientes)
        elif opcion == "2":
            ejecutar_principal(mod_lis_cal, calificaciones)
        elif opcion == "3":
            ejecutar_principal(mod_bus_cal, calificaciones)
        elif opcion == "4":
            ejecutar_principal(mod_eli_cal, calificaciones)
        elif opcion == "5":
            break
        else:
            print("Opción no válida.")


def menu_principal(datos):
    padres = datos["padres"]
    madres = datos["madres"]
    estudiantes = datos["estudiantes"]
    familias = datos["familias"]
    expedientes = datos["expedientes"]
    calificaciones = datos["calificaciones"]

    while True:
        print("\n===================================")
        print("     SISTEMA MESA DE PARTES 2026")
        print("===================================")
        print("1. Gestión de Padres")
        print("2. Gestión de Madres")
        print("3. Gestión de Estudiantes")
        print("4. Gestión de Familias")
        print("5. Gestión de Expedientes")
        print("6. Gestión de Calificaciones")
        print("7. Guardar todos los registros en CSV")
        print("8. Guardar y Salir")

        opcion = input("Seleccione una opción: ").strip()

        if opcion == "1":
            ejecutar_principal(mod_padre, padres)
        elif opcion == "2":
            ejecutar_principal(mod_madre, madres)
        elif opcion == "3":
            ejecutar_principal(mod_estudiantes, estudiantes)
        elif opcion == "4":
            ejecutar_principal(mod_familia, familias, padres, madres, estudiantes)
        elif opcion == "5":
            submenu_expedientes(expedientes, estudiantes)
        elif opcion == "6":
            submenu_calificaciones(calificaciones, expedientes)
        elif opcion == "7":
            guardar_expedientes(padres, madres, estudiantes, familias, expedientes, calificaciones)
        elif opcion == "8":
            guardar_expedientes(padres, madres, estudiantes, familias, expedientes, calificaciones)
            print("Saliendo del sistema...")
            break
        else:
            print("Opción no válida.")
