import matplotlib.pyplot as plt
import numpy as np

class VentasVideojuegos:
    def __init__(self, datos):
        self.datos = datos
        self.m = []
        self.generos = []
        self.ventas = []
        self.masvendido = 0

    def cargar_datos(self):
        with open(self.datos, "r") as archivo:
            leerlineas = archivo.readlines()
            for i in leerlineas:
                numelemen = i.strip().split(",")
                self.m.append(numelemen)

    def calcular_ventas(self):
        self.generos = self.m[0][1:]
        self.ventas = [0] * len(self.generos)

        for i in self.m:
            if i[0] == "2017":
                for j in range(1, len(i)):
                    self.ventas[j - 1] += int(i[j])

        self.masvendido = self.ventas.index(max(self.ventas))

    def generar_grafico(self):
        y = self.m
        # encabezado = y[0]
        generos_graficos = y[1:]

        años = [int(fila[0]) for fila in generos_graficos]
        deportes = [int(fila[1]) for fila in generos_graficos]
        accion = [int(fila[2]) for fila in generos_graficos]
        aventura = [int(fila[3]) for fila in generos_graficos]
        estrategia = [int(fila[4]) for fila in generos_graficos]

        fig, ax = plt.subplots()

        posiciones = np.arange(len(años))
        ancho = 0.2

        ax.bar(posiciones, deportes, ancho, label='Deportes')
        ax.bar(posiciones + ancho, accion, ancho, label='Acción')
        ax.bar(posiciones + 2 * ancho, aventura, ancho, label='Aventura')
        ax.bar(posiciones + 3 * ancho, estrategia, ancho, label='Estrategia')

        ax.set_xlabel('Año')
        ax.set_ylabel('Cantidad')
        ax.set_title('Ventas de videojuegos por género y año')
        ax.legend()

        ax.set_xticks(posiciones + 2 * ancho)
        ax.set_xticklabels(años)

        plt.show()

    def generar_grafico2(self):
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

    def calcular_ventas_continentes(self, datos_continentes):
        tengosueño = []
        with open(datos_continentes, "r") as archivo:
            leerlineas = archivo.readlines()
            for i in leerlineas:
                numelemen = i.strip().split(",")
                tengosueño.append(numelemen)

        ventasa = [0] * len(self.generos)

        for i in tengosueño:
            if i[0] == "2022":
                for j in range(1, len(i)):
                    ventasa[j - 1] += int(i[j])

        a = ventasa[self.masvendido]

        return a

    def calcular_promedio(self, datos_america, datos_asia, datos_europa):
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

            ventas_continentes.append(ventas[self.masvendido])

        promedio = sum(ventas_continentes) / len(ventas_continentes)

        return promedio


datos_america = 'VentasVideoJuegosAmerica.csv'
datos_asia = 'VentasVideoJuegosAsia.csv'
datos_europa = 'VentasVideoJuegosEuropa.csv'

ventas_videojuegos = VentasVideojuegos(datos_america)
ventas_videojuegos.cargar_datos()
ventas_videojuegos.calcular_ventas()
ventas_videojuegos.generar_grafico()

ventas_videojuegos2 = VentasVideojuegos(datos_asia)
# ventas_videojuegos2.calcular_ventas()
ventas_videojuegos2.cargar_datos()
ventas_videojuegos2.generar_grafico2()

a = ventas_videojuegos.calcular_ventas_continentes(datos_asia)
potocaca = ventas_videojuegos.calcular_ventas_continentes(datos_europa)
marcianeke = ventas_videojuegos.calcular_ventas_continentes(datos_america)

promedio = ventas_videojuegos.calcular_promedio(datos_america, datos_asia, datos_europa)

gmasvendido = ventas_videojuegos.generos[ventas_videojuegos.masvendido]

print(f'El género que más vendido: {gmasvendido}')
print(f'Estimado de ventas del género {gmasvendido} en Asia en 2022: {a}')
print(f'Estimado de ventas del género {gmasvendido} en Europa en 2022: {potocaca}')
print(f'Estimado de ventas del género {gmasvendido} en América en 2022: {marcianeke}')
print(f'El promedio de ventas de los continentes en el año 2022 es de {round(promedio, 1)}')

