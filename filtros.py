from database import conectar_bd
from tkinter import messagebox

def buscar_encuestas(entry_buscar_edad, entry_buscar_sexo):
    conn = conectar_bd()
    cursor = conn.cursor()
    try:
        # Tu lógica para búsqueda
        pass
    except Exception as e:
        messagebox.showerror("Error", f"Error al buscar encuestas: {e}")
    finally:
        cursor.close()
        conn.close()
