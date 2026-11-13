from Cargar_Expediente import cargar_expedientes
from Menu import menu_principal

def main():
    datos = cargar_expedientes()
    menu_principal(datos)

if __name__ == "__main__":
    main()
