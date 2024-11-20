from tkinter import messagebox
import pandas as pd
from database import conectar_bd

def exportar_a_excel():
    conn = conectar_bd()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM ENCUESTA")
        rows = cursor.fetchall()
        df = pd.DataFrame(rows, columns=[i[0] for i in cursor.description])
        df.to_excel("encuestas.xlsx", index=False)
        messagebox.showinfo("Éxito", "Datos exportados a Excel exitosamente.")
    except Exception as e:
        messagebox.showerror("Error", f"Error al exportar a Excel: {e}")
    finally:
        cursor.close()
        conn.close()
