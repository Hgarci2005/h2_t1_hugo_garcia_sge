from tkinter import messagebox, END
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

def ver_encuestas(listbox_encuestas):
    conn = conectar_bd()
    cursor = conn.cursor()
    try:
        cursor.execute("SELECT * FROM ENCUESTA")
        rows = cursor.fetchall()
        listbox_encuestas.delete(0, END)
        for row in rows:
            listbox_encuestas.insert(END, row)
    except Exception as e:
        messagebox.showerror("Error", f"Error al obtener las encuestas: {e}")
    finally:
        cursor.close()
        conn.close()

def actualizar_encuesta(entry_edad, entry_sexo, listbox_encuestas):
    conn = conectar_bd()
    cursor = conn.cursor()
    try:
        selected_item = listbox_encuestas.curselection()
        if selected_item:
            id_encuesta = listbox_encuestas.get(selected_item)[0]
            edad = entry_edad.get()
            sexo = entry_sexo.get()
            cursor.execute("UPDATE ENCUESTA SET edad=%s, Sexo=%s WHERE idEncuesta=%s", (edad, sexo, id_encuesta))
            conn.commit()
            messagebox.showinfo("Éxito", "Encuesta actualizada exitosamente.")
            ver_encuestas(listbox_encuestas)
        else:
            messagebox.showwarning("Advertencia", "Selecciona una encuesta para actualizar.")
    except Exception as e:
        messagebox.showerror("Error", f"Error al actualizar la encuesta: {e}")
    finally:
        cursor.close()
        conn.close()

def eliminar_encuesta(listbox_encuestas):
    conn = conectar_bd()
    cursor = conn.cursor()
    try:
        selected_item = listbox_encuestas.curselection()
        if selected_item:
            id_encuesta = listbox_encuestas.get(selected_item)[0]
            cursor.execute("DELETE FROM ENCUESTA WHERE idEncuesta=%s", (id_encuesta,))
            conn.commit()
            messagebox.showinfo("Éxito", "Encuesta eliminada exitosamente.")
            ver_encuestas(listbox_encuestas)
        else:
            messagebox.showwarning("Advertencia", "Selecciona una encuesta para eliminar.")
    except Exception as e:
        messagebox.showerror("Error", f"Error al eliminar la encuesta: {e}")
    finally:
        cursor.close()
        conn.close()
