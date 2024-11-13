import csv

class AutomataFD:
    def __init__(self, ruta_archivo):
        """Inicializar el autómata con datos del archivo CSV"""
        self.estados, self.alfabeto, self.transiciones, self.estado_inicial, self.estados_finales = self.cargar_csv(ruta_archivo)
        self.estado_actual = None

    def cargar_csv(self, ruta_archivo):
        """Cargar configuración del autómata desde archivo CSV"""
        estados = []
        alfabeto = []
        transiciones = {}
        estado_inicial = None
        estados_finales = []

        try:
            with open(ruta_archivo, mode='r') as archivo:
                lector = csv.reader(archivo)
                alfabeto = next(lector)[1:]  # Primera fila sin primera columna

                for fila in lector:
                    estado = fila[0]
                    trans = fila[1:]

                    # Procesar marcadores de estados
                    if '+*' in estado:
                        estado = estado.replace('+*', '')
                        estado_inicial = estado
                        estados_finales.append(estado)
                    elif '+' in estado:
                        estado = estado.replace('+', '')
                        estado_inicial = estado
                    elif '*' in estado:
                        estado = estado.replace('*', '')
                        estados_finales.append(estado)

                    estados.append(estado)
                    transiciones[estado] = dict(zip(alfabeto, trans))

            return estados, alfabeto, transiciones, estado_inicial, estados_finales
        except FileNotFoundError:
            raise Exception("Archivo no encontrado")
        except Exception as e:
            raise Exception(f"Error al leer el archivo: {str(e)}")

    def validar_cadena(self, cadena):
        """Valida si una cadena es aceptada por el autómata"""
        self.estado_actual = self.estado_inicial
        
        for simbolo in cadena:
            if simbolo not in self.alfabeto:
                return False
            
            if simbolo not in self.transiciones[self.estado_actual]:
                return False
                
            self.estado_actual = self.transiciones[self.estado_actual][simbolo]
            
            # Estado trampa
            if self.estado_actual == "TRAMPA":
                return False

        return self.estado_actual in self.estados_finales

def menu_principal():
    automata = None

    while True:
        print("\nMenú del Autómata:")
        print("1. Cargar archivo CSV")
        print("2. Probar cadena")
        print("3. Salir")

        opcion = input("\nSeleccione una opción (1-3): ")

        if opcion == '1':
            try:
                archivo = input("Nombre del archivo CSV (favor de poner .csv al final): ")
                automata = AutomataFD(archivo)
                
                # Mostrar los vectores de valores
                print("\nDatos cargados del autómata:")
                print(f"Estados (Q): {automata.estados}")
                print(f"Alfabeto (Σ): {automata.alfabeto}")
                print(f"Estado inicial: {automata.estado_inicial}")
                print(f"Estados finales: {automata.estados_finales}")
                print("Transiciones (δ):")
                for estado, trans in automata.transiciones.items():
                    print(f"  {estado}: {trans}")
                
                print("\nArchivo cargado exitosamente")
            except Exception as e:
                print(f"Error: {str(e)}")
                
        elif opcion == '2':
            if not automata:
                print("Primero debe cargar un archivo CSV")
                continue
                
            cadena = input("Ingrese la cadena a validar: ")
            resultado = automata.validar_cadena(list(cadena))
            print("Cadena ACEPTADA" if resultado else "Cadena RECHAZADA")
            
        elif opcion == '3':
            print("Vuelva pronto")
            break
            
        else:
            print("Opción no válida")

if __name__ == "__main__":
    print("Autómata Finito Determinista")
    menu_principal()
