import registrar_calificaciones as mod_reg_cal
import listar_calificaciones as mod_lis_cal
import buscar_calificaciones as mod_bus_cal
import eliminar_calificaciones as mod_eli_cal

def obtener_funcion(modulo):
    for nombre, obj in vars(modulo).items():
        if callable(obj) and getattr(obj, "__module__", None) == modulo.__name__:
            return obj
    return lambda *args, **kwargs: None

registrar_calificaciones = obtener_funcion(mod_reg_cal)
listar_calificaciones = obtener_funcion(mod_lis_cal)
buscar_calificaciones = obtener_funcion(mod_bus_cal)
eliminar_calificaciones = obtener_funcion(mod_eli_cal)
