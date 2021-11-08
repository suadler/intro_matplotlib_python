# Matplotlib [Python]
# Ejercicios de práctica

# Autor: Inove Coding School
# Version: 2.0

# IMPORTANTE: NO borrar los comentarios
# que aparecen en verde con el hashtag "#"

# Ejercicios de matplotlib
import numpy as np
import matplotlib.pyplot as plt


if __name__ == '__main__':
    print("Bienvenidos a otra clase de Inove con Python")
    print("Line Plot: Figura con múltiples gráficos")

    # NOTA: aproveche los ejemplos "line_plot" y "scatter_plot" de clase

    # Se desea graficar cuatro funciones en una misma figura
    # en cuatros gráficos (axes) distintos. Para el siguiente
    # intervalor de valores de "X":
    x = np.linspace(0, 10, 40)

    # Realizar tres gráficos que representen
    # y1 = x^2 (X al cuadrado)
    # y2 = x^3 (X al cubo)
    # y3 = x^4 (X a la cuarta)
    # y4 = raiz_cuadrada(X)

    # Implementación:
    y1 = x**2
    y2 = x**3
    y3 = x**4
    y4 = np.sqrt(x)

    # Alumnos: Esos cuatro gráficos deben estar colocados
    # en la diposición de 2 filas y 2 columna:
    # ------
    #  graf1 | graf2
    # ------
    #  graf3 | graf4
    # Utilizar add_subplot para lograr este efecto
    # de "2 filas" "2 columna" de gráficos

    # Se debe colocar en la leyenda la función que representa
    # cada gráfico

    # Cada gráfico realizarlo con un color distinto
    # a su elección

    # Colocar una grilla a elección

    # Crear acá su gráfico

    fig = plt.figure()
    ax = fig.add_subplot()
    fig.suptitle("Ejecicio 4", fontsize=16, color="b")

    ax1 = fig.add_subplot(2, 2, 1)  
    ax2 = fig.add_subplot(2, 2, 2)
    ax3 = fig.add_subplot(2, 2, 3)
    ax4 = fig.add_subplot(2, 2, 4)

    ax1.plot(x, y1, color="m", marker="<", label="x**2")
    ax1.set_facecolor("w")
    ax1.set_title("graf1")
    ax1.set_ylabel("yeje")
    ax1.set_xlabel("xeje")
    ax1.legend()

    ax2.plot(x, y2, color="g", marker=".", label="x**3")
    ax2.set_facecolor("w")
    ax2.set_title("graf2")
    ax2.set_ylabel("yeje")
    ax2.set_xlabel("xeje")
    ax2.legend()

    ax3.scatter(x, y3, color="r", marker="v", label="x**4")
    ax3.set_facecolor("w")
    ax3.set_title("graf3")
    ax3.set_ylabel("yeje")
    ax3.set_xlabel("xeje")
    ax3.legend()

    ax4.scatter(x, y4, color="y", marker=">", label="sqrt")
    ax4.set_facecolor("w")
    ax4.set_title("graf4")
    ax4.set_ylabel("yeje")
    ax4.set_xlabel("xeje")
    ax4.legend()

    plt.show()



    print("terminamos")
