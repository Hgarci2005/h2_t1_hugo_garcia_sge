from tkinter import messagebox, END, ttk
from database import conectar_bd

def crear_encuesta(entry_edad, entry_sexo):
    conn = conectar_bd()
    cursor = conn.cursor()
    try:
        edad = entry_edad.get()
        sexo = entry_sexo.get()

        cursor.execute("INSERT INTO ENCUESTA (edad, Sexo) VALUES (%s, %s)", (edad, sexo))
        conn.commit()
        messagebox.showinfo("Éxito", "Encuesta creada exitosamente.")
    except Exception as e:
        messagebox.showerror("Error", f"Error al crear la encuesta: {e}")
    finally:
        cursor.close()
        conn.close()

def ver_encuestas(treeview_encuestas):
    conn = conectar_bd()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM ENCUESTA")
        rows = cursor.fetchall()
        for row in treeview_encuestas.get_children():
            treeview_encuestas.delete(row)
        for row in rows:
            treeview_encuestas.insert("", END, values=row)
    except Exception as e:
        messagebox.showerror("Error", f"Error al obtener las encuestas: {e}")
    finally:
        cursor.close()
        conn.close()

def actualizar_encuesta(entry_edad, entry_sexo, treeview_encuestas):
    conn = conectar_bd()
    cursor = conn.cursor()
    try:
        selected_item = treeview_encuestas.selection()
        if selected_item:
            id_encuesta = treeview_encuestas.item(selected_item)['values'][0]
            edad = entry_edad.get()
            sexo = entry_sexo.get()
            cursor.execute("UPDATE ENCUESTA SET edad=%s, Sexo=%s WHERE idEncuesta=%s", (edad, sexo, id_encuesta))
            conn.commit()
            messagebox.showinfo("Éxito", "Encuesta actualizada exitosamente.")
            ver_encuestas(treeview_encuestas)
        else:
            messagebox.showwarning("Advertencia", "Selecciona una encuesta para actualizar.")
    except Exception as e:
        messagebox.showerror("Error", f"Error al actualizar la encuesta: {e}")
    finally:
        cursor.close()
        conn.close()

def eliminar_encuesta(treeview_encuestas):
    conn = conectar_bd()
    cursor = conn.cursor()
    try:
        selected_item = treeview_encuestas.selection()
        if selected_item:
            id_encuesta = treeview_encuestas.item(selected_item)['values'][0]
            cursor.execute("DELETE FROM ENCUESTA WHERE idEncuesta=%s", (id_encuesta,))
            conn.commit()
            messagebox.showinfo("Éxito", "Encuesta eliminada exitosamente.")
            ver_encuestas(treeview_encuestas)
        else:
            messagebox.showwarning("Advertencia", "Selecciona una encuesta para eliminar.")
    except Exception as e:
        messagebox.showerror("Error", f"Error al eliminar la encuesta: {e}")
    finally:
        cursor.close()
        conn.close()
