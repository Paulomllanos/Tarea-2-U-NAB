"""
Nombre de la Asignatura: Introducción a la programación - TDFI102

NRC de la Sección: 12704

Descripción: Este programa está enfocado al análisis de datos de distintos archivos CSV("Análisis del amigo"), con el fin de poder recopilar información necesaria a lo solicitado, además de proporcionar graficos que respaldan la información. Cabe mencionar que se desarrolla a través de programación orientada a objetos, interactuando el usuario en el programa, a través de un menú interactivo de opciones.

Autores: 
1- 
    Nombre: Axel Matias Contreras Ortega
    RUT: 21.245.507-5
2- 
    Nombre: Paulo Andres Maldonado Llanos
    RUT: 20.063.001-7

"""

# Librerias utilizadas para nuestra app: 
import matplotlib.pyplot as plt # Libreria para generación de graficos , la llamamos como plt
import numpy as np # Librería que da soporte para crear vectores y matrices grandes, generando calculos matematicos de alto nivel, la llamamos como np
import time # Libreria que proporciona varias opciones en relación al tiempo.

class VentasVideojuegos:
    def __init__(self, datos):
        """
        Clase que representa las ventas de videojuegos.

        Args:
        - datos (str): Nombre del archivo de datos.

        Atributos:
        - datos (str): Nombre del archivo de datos.
        - m (list): Lista que almacena los datos leídos del archivo.
        - generos (list): Lista que almacena los géneros de videojuegos.
        - ventas (list): Lista que almacena las ventas de videojuegos por género.
        - mas_vendido (int): Índice del género más vendido.
        """
        self.datos = datos
        self.m = []
        self.generos = []
        self.ventas = []
        self.mas_vendido = 0

    def cargar_datos(self):
        """
        Carga los datos del archivo especificado en el atributo `datos`.
        """
        with open(self.datos, "r") as archivo:
            leerlineas = archivo.readlines()
            for i in leerlineas:
                numelemen = i.strip().split(",")
                self.m.append(numelemen)

    def genero_mas_vendido(self):
        """
        Graba las ventas totales por género para el año 2017.
        Establece el género más vendido.
        """
        self.generos = self.m[0][1:]
        self.ventas = [0] * len(self.generos)

        for i in self.m:
            if i[0] == "2017":
                for j in range(1, len(i)):
                    self.ventas[j - 1] += int(i[j])

        self.mas_vendido = self.ventas.index(max(self.ventas))

    """ 
    Los métodos generar_grafico_asia(), generar_grafico_europa() y generar_grafico_america() tienen una estructura similar, pero se enfocan en cada uno de sus continentes respectivamente.
    """
    def generar_grafico_america(self):
        # Genera un gráfico de barras que muestra las ventas de videojuegos de deportes por año en America.
        y = self.m
        generos_graficos = y[1:]

        años = [int(fila[0]) for fila in generos_graficos] #Guardamos en que posicion se encuentran los años(fila)
        deportes = [int(fila[1]) for fila in generos_graficos] #Guardamos en que posicion se encuentra Deportes(fila)

        fig, ax = plt.subplots() # Nos sirve para empezar a dibujar el grafico.

        posiciones = np.arange(len(años))
        ancho = 0.4

        ax.bar(posiciones, deportes, ancho, label='Deportes')

        ax.set_xlabel('Año')
        ax.set_ylabel('Cantidad')
        ax.set_title('Ventas de videojuegos de deportes por año en América')
        ax.legend()

        ax.set_xticks(posiciones)
        ax.set_xticklabels(años)

        plt.show()

    def generar_grafico_asia(self):
        # Genera un gráfico de barras que muestra las ventas de videojuegos de deportes por año en Asia.
        y = self.m
        generos_graficos = y[1:]

        años = [int(fila[0]) for fila in generos_graficos] 
        deportes = [int(fila[1]) for fila in generos_graficos]

        fig, ax = plt.subplots()

        posiciones = np.arange(len(años))
        ancho = 0.4

        ax.bar(posiciones, deportes, ancho, label='Deportes')

        ax.set_xlabel('Año')
        ax.set_ylabel('Cantidad')
        ax.set_title('Ventas de videojuegos de deportes por año en Asia')
        ax.legend()

        ax.set_xticks(posiciones)
        ax.set_xticklabels(años)

        plt.show()

    def generar_grafico_europa(self):
        # Genera un gráfico de barras que muestra las ventas de videojuegos de deportes por año en Europa.
        y = self.m
        generos_graficos = y[1:]

        años = [int(fila[0]) for fila in generos_graficos]
        deportes = [int(fila[1]) for fila in generos_graficos]

        fig, ax = plt.subplots()

        posiciones = np.arange(len(años))
        ancho = 0.4

        ax.bar(posiciones, deportes, ancho, label='Deportes')

        ax.set_xlabel('Año')
        ax.set_ylabel('Cantidad')
        ax.set_title('Ventas de videojuegos de deportes por año en Europa')
        ax.legend()

        ax.set_xticks(posiciones)
        ax.set_xticklabels(años)

        plt.show()

    def v_continente_2022(self, datos_continentes):
        """
        Guarda las ventas del género más vendido en el año 2022 para un continente específico.

        Args:
        - datos_continentes (str): Nombre del archivo de datos del continente.

        Returns:
        - venta_total_año_2022 (int): Total de ventas del año 2022 del genero más vendido respecto al continente señalado.
        """
        m_aux = []
        with open(datos_continentes, "r") as archivo:
            leerlineas = archivo.readlines()
            for i in leerlineas:
                numelemen = i.strip().split(",")
                m_aux.append(numelemen)

        # variable utilizada para almacenar el dato del total de ventas del genero elegido respecto a su longitud
        venta = [0] * len(self.generos)

        for i in m_aux:
            if i[0] == "2022":
                for j in range(1, len(i)):
                    venta[j - 1] += int(i[j])

        # Variable que guarda la informacion del total de ventas del año 2022 del genero más vendido respecto al continente señalado.
        venta_total_año_2022 = venta[self.mas_vendido] 

        return venta_total_año_2022

    def calcular_ventas_totales(self, datos_america, datos_asia, datos_europa):
        """
        Calcula las ventas totales del género más vendido en el año 2022 para todos los continentes.

        Args:
        - datos_america (str): Nombre del archivo de datos de América.
        - datos_asia (str): Nombre del archivo de datos de Asia.
        - datos_europa (str): Nombre del archivo de datos de Europa.

        Returns:
        - ventas_totales (int): Ventas totales del género más vendido en el año 2022 para todos los continentes.
        """
        datos_continentes = [datos_america, datos_asia, datos_europa]
        ventas_continentes = []

        for continente in datos_continentes:
            ventas = [0] * len(self.generos)

            with open(continente, "r") as archivo:
                leerlineas = archivo.readlines()
                for i in leerlineas:
                    numelemen = i.strip().split(",")
                    if numelemen[0] == "2022":
                        for j in range(1, len(numelemen)):
                            ventas[j - 1] += int(numelemen[j])

            ventas_continentes.append(ventas[self.mas_vendido])

        ventas_totales = sum(ventas_continentes)

        return ventas_totales


# Se crean instancias de la clase VentasVideojuegos y se realizan los cálculos necesarios.

# Se almacena los en variables los nombres de los archivos de datos entregados.
datos_america = 'VentasVideoJuegosAmerica.csv'
datos_asia = 'VentasVideoJuegosAsia.csv'
datos_europa = 'VentasVideoJuegosEuropa.csv'

# Se instancia la clase con los datos de cada archivo y se cargan sus datos.

#America
ventas_videojuegos = VentasVideojuegos(datos_america)
ventas_videojuegos.cargar_datos()
ventas_videojuegos.genero_mas_vendido() # Se busca el género más vendido en america para el año 2017.

#Asia
ventas_videojuegos2 = VentasVideojuegos(datos_asia)
ventas_videojuegos2.cargar_datos()

#Europa
ventas_videojuegos3 = VentasVideojuegos(datos_europa)
ventas_videojuegos3.cargar_datos()

# Se guarda en una variable el nombre del género más vendido en America año 2017.
g_mas_vendido = ventas_videojuegos.generos[ventas_videojuegos.mas_vendido]

# Guardamos las ventas del género más vendido en America año 2017 por continente en variables.
ventas_asia = ventas_videojuegos.v_continente_2022(datos_asia)
ventas_europa = ventas_videojuegos.v_continente_2022(datos_europa)
ventas_america = ventas_videojuegos.v_continente_2022(datos_america)

# Guardamos en una variable el total de ventas de los continentes respecto al género del videojuego más vendido en  America año 2017.
ventas_totales = ventas_videojuegos.calcular_ventas_totales(datos_america, datos_asia, datos_europa)

# Calculamos el porcentaje de ventas por Continente, respecto al total de ventas.
porcentaje_ventas_asia = round((ventas_asia / ventas_totales) * 100)
porcentaje_ventas_america = round((ventas_america / ventas_totales) * 100)
porcentaje_ventas_europa = round((ventas_europa / ventas_totales) * 100)


# Programa principal: Se muestra un menú interactivo para el usuario.

op = "" # Variable que servira para seleccionar una opcion, parte como string vacio.
while op != "7": # Se realiza un ciclo while para repetir el menú hasta que el usuario termine el programa.
    print("\nAnálisis de videojuego a desarrollar")
    print("1. Género a desarrollar de videojuego: ")
    print("2. Monto de ventas estimadas: ")
    print("3. Inversión de publicidad en porcentaje por continente: ")
    print("4. Gráfico de ventas del \"Género de Deportes\" por año en América")
    print("5. Gráfico de ventas del \"Género de Deportes\" por año en Asia")
    print("6. Gráfico de ventas del \"Género de Deportes\" por año en Europa")
    print("7. Salir")
    op = input("Elige una opción: ")
    # Realizamos condicionales para mostrar la información de la opción escogida por el usuario.
    # El time.sleep() Nos sirve para que el usuario pueda observar la información antes de que se repita el menú.
    if op == "1":
        print(f'\nEl género a desarrollar de videojuego es: \"{g_mas_vendido}\"')
        time.sleep(2)
    elif op == "2":
        print(f'\nEl monto de ventas estimada será de: {ventas_asia}')
        time.sleep(2)
    elif op == "3":
        print(f'\nLa inversión de la publicidad será repartida aproximadamente de esta manera:')
        print(f'Asia = {porcentaje_ventas_asia}%')
        print(f'América = {porcentaje_ventas_america}%')
        print(f'Europa = {porcentaje_ventas_europa}%')
        time.sleep(3)
    elif op == "4":
        ventas_videojuegos.generar_grafico_america()
    elif op == "5":
        ventas_videojuegos2.generar_grafico_asia()
    elif op == "6":
        ventas_videojuegos3.generar_grafico_europa()
print("\nPrograma terminado...")