import csv
import os

def escribir_csv(ruta, encabezados, lista):
    os.makedirs("datos", exist_ok=True)
    with open(ruta, "w", newline="", encoding="utf-8-sig") as archivo:
        escritor = csv.DictWriter(archivo, fieldnames=encabezados)
        escritor.writeheader()
        escritor.writerows(lista)

def guardar_expedientes(padres, madres, estudiantes, familias, expedientes, calificaciones):
    print("\n--- GUARDANDO TODOS LOS REGISTROS EN CSV ---")
    
    escribir_csv("datos/padres.csv", ["codigo", "dni", "nombres", "paterno", "materno", "telefono", "correo"], padres)
    escribir_csv("datos/madres.csv", ["codigo", "dni", "nombres", "paterno", "materno", "telefono", "correo"], madres)
    escribir_csv("datos/estudiantes.csv", ["codigo", "dni", "nombres", "paterno", "materno", "nivel", "turno", "taller"], estudiantes)
    escribir_csv("datos/familias.csv", ["codigo_familia", "codigo_padre", "codigo_madre", "codigo_estudiante"], familias)
    
    encabezados_exp = list(expedientes[0].keys()) if len(expedientes) > 0 else ["codigo", "codigo_estudiante", "nivel", "estado"]
    escribir_csv("datos/expedientes.csv", encabezados_exp, expedientes)
        
    encabezados_cal = list(calificaciones[0].keys()) if len(calificaciones) > 0 else ["codigo", "codigo_expediente", "nota1", "nota2", "nota3", "nota4", "promedio", "maxima", "minima", "condicion", "estado_final"]
    escribir_csv("datos/calificaciones.csv", encabezados_cal, calificaciones)
        
    print("¡Respaldo exitoso! Todos los registros fueron guardados en la carpeta 'datos/'")
    print("\n")
