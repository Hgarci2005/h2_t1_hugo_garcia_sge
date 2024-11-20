import pandas as pd
import matplotlib.pyplot as plt
from tkinter import messagebox, Toplevel
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from database import conectar_bd

def generar_grafico(datos_x, datos_y):
    conn = conectar_bd()
    cursor = conn.cursor()
    try:
        # Consulta dinámica basada en los datos seleccionados por el usuario
        cursor.execute(f"SELECT {datos_x}, {datos_y} FROM ENCUESTA")
        rows = cursor.fetchall()
        df = pd.DataFrame(rows, columns=[datos_x, datos_y])

        fig, ax = plt.subplots()
        # Graficar según los ejes seleccionados
        df.groupby(datos_x)[datos_y].mean().plot(kind='bar', ax=ax)
        ax.set_title(f'Distribución de {datos_y} según {datos_x}')
        ax.set_xlabel(datos_x)
        ax.set_ylabel(f'{datos_y} (Promedio)')

        # Crear una nueva ventana para mostrar el gráfico
        ventana_grafico = Toplevel()
        ventana_grafico.title(f"Gráfico de Distribución de {datos_y} según {datos_x}")

        # Integrar el gráfico en la ventana de Tkinter
        canvas = FigureCanvasTkAgg(fig, master=ventana_grafico)
        canvas.draw()
        canvas.get_tk_widget().pack(fill='both', expand=True)
    except Exception as e:
        messagebox.showerror("Error", f"Error al generar el gráfico: {e}")
    finally:
        cursor.close()
        conn.close()
