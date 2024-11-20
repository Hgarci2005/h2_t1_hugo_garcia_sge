import tkinter as tk
from tkinter import ttk, messagebox, Toplevel
from Crud import crear_encuesta, ver_encuestas, actualizar_encuesta, eliminar_encuesta
from excell import exportar_a_excel
from filtros import buscar_encuestas
from grafico import generar_grafico


def create_label_entry(frame, text, row, col):
    tk.Label(frame, text=text, font=("Arial", 12), bg="#2C3E50", fg="#ECF0F1").grid(row=row, column=col * 2, padx=5, pady=5, sticky="w")
    entry = ttk.Entry(frame, font=("Arial", 12))
    entry.grid(row=row, column=col * 2 + 1, padx=5, pady=5, sticky="ew")
    return entry

def create_button(frame, text, command):
    button = tk.Button(frame, text=text, command=command, bg="#1ABC9C", fg="white", font=("Arial", 12, "bold"), relief="flat")
    button.pack(side=tk.LEFT, padx=5, pady=5)
    return button

def on_select(event):
    try:
        selected_item = treeview_encuestas.selection()
        if selected_item:
            data = treeview_encuestas.item(selected_item)['values']
            entry_edad.delete(0, tk.END)
            entry_edad.insert(0, data[1])
            entry_sexo.delete(0, tk.END)
            entry_sexo.insert(0, data[2])
            entry_bebidas_semana.delete(0, tk.END)
            entry_bebidas_semana.insert(0, data[3])
            entry_cervezas_semana.delete(0, tk.END)
            entry_cervezas_semana.insert(0, data[4])
            entry_bebidas_fin_semana.delete(0, tk.END)
            entry_bebidas_fin_semana.insert(0, data[5])
            entry_bebidas_destiladas_semana.delete(0, tk.END)
            entry_bebidas_destiladas_semana.insert(0, data[6])
            entry_vinos_semana.delete(0, tk.END)
            entry_vinos_semana.insert(0, data[7])
            entry_perdidas_control.delete(0, tk.END)
            entry_perdidas_control.insert(0, data[8])
            entry_diversion_dependencia_alcohol.delete(0, tk.END)
            entry_diversion_dependencia_alcohol.insert(0, data[9])
            entry_problemas_digestivos.delete(0, tk.END)
            entry_problemas_digestivos.insert(0, data[10])
            entry_tension_alta.delete(0, tk.END)
            entry_tension_alta.insert(0, data[11])
            entry_dolor_cabeza.delete(0, tk.END)
            entry_dolor_cabeza.insert(0, data[12])
    except Exception as e:
        messagebox.showerror("Error", f"An error occurred: {e}")

def show_graph_selection():
    top = Toplevel(root)
    top.title("Seleccionar Datos para Gráfico")

    def generate():
        datos_x = entry_datos_x.get()
        datos_y = entry_datos_y.get()
        generar_grafico(datos_x, datos_y)

    tk.Label(top, text="Datos para Eje X:", font=("Arial", 12)).grid(row=0, column=0, padx=10, pady=10, sticky="w")
    entry_datos_x = ttk.Entry(top, font=("Arial", 12))
    entry_datos_x.grid(row=0, column=1, padx=10, pady=10, sticky="ew")

    tk.Label(top, text="Datos para Eje Y:", font=("Arial", 12)).grid(row=1, column=0, padx=10, pady=10, sticky="w")
    entry_datos_y = ttk.Entry(top, font=("Arial", 12))
    entry_datos_y.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

    tk.Button(top, text="Generar Gráfico", command=generate, bg="#1ABC9C", fg="white", font=("Arial", 12, "bold"), relief="flat").grid(row=2, column=0, columnspan=2, pady=10)

# Configuración de la interfaz gráfica
root = tk.Tk()
root.title("Gestión de Encuestas")
root.geometry("1000x800")
root.config(bg="#2C3E50")

style = ttk.Style()
style.configure('TButton', font=('Arial', 10, 'bold'), padding=6, relief="flat", background="#1ABC9C", foreground="white")
style.map('TButton', background=[('active', '#16A085')])

frame_principal = ttk.Frame(root, padding="20", style="TFrame")
frame_principal.pack(fill=tk.BOTH, expand=True)

tk.Label(frame_principal, text="Gestión de Encuestas", font=("Arial", 24, "bold"), bg="#2C3E50", fg="#ECF0F1").pack(pady=20)

frame_entradas = ttk.Frame(frame_principal, padding="10")
frame_entradas.pack(fill=tk.X)

entry_edad = create_label_entry(frame_entradas, "Edad:", 0, 0)
entry_sexo = create_label_entry(frame_entradas, "Sexo:", 1, 0)
entry_bebidas_semana = create_label_entry(frame_entradas, "Bebidas a la semana:", 2, 0)
entry_cervezas_semana = create_label_entry(frame_entradas, "Cervezas a la semana:", 3, 0)
entry_bebidas_fin_semana = create_label_entry(frame_entradas, "Bebidas Fin de Semana:", 4, 0)
entry_bebidas_destiladas_semana = create_label_entry(frame_entradas, "Bebidas Destiladas a la semana:", 5, 0)
entry_vinos_semana = create_label_entry(frame_entradas, "Vinos a la semana:", 6, 0)
entry_perdidas_control = create_label_entry(frame_entradas, "Perdidas de control:", 7, 0)
entry_diversion_dependencia_alcohol = create_label_entry(frame_entradas, "Diversión y Dependencia del Alcohol:", 8, 0)
entry_problemas_digestivos = create_label_entry(frame_entradas, "Problemas Digestivos:", 9, 0)
entry_tension_alta = create_label_entry(frame_entradas, "Tensión Alta:", 10, 0)
entry_dolor_cabeza = create_label_entry(frame_entradas, "Dolor de Cabeza:", 11, 0)

frame_botones = ttk.Frame(frame_principal, padding="10")
frame_botones.pack(fill=tk.X)

create_button(frame_botones, "Crear Encuesta", lambda: crear_encuesta(entry_edad, entry_sexo))
create_button(frame_botones, "Ver Encuestas", lambda: ver_encuestas(treeview_encuestas))
create_button(frame_botones, "Actualizar Encuesta", lambda: actualizar_encuesta(entry_edad, entry_sexo, treeview_encuestas))
create_button(frame_botones, "Eliminar Encuesta", lambda: eliminar_encuesta(treeview_encuestas))
create_button(frame_botones, "Exportar a Excel", exportar_a_excel)
create_button(frame_botones, "Generar Gráfico", show_graph_selection)

frame_listbox = ttk.Frame(frame_principal)
frame_listbox.pack(fill=tk.BOTH, expand=True)

scrollbar = ttk.Scrollbar(frame_listbox)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

columns = ("ID", "Edad", "Sexo", "Bebidas Semana", "Cervezas Semana", "Bebidas Fin Semana",
           "Bebidas Destiladas Semana", "Vinos Semana", "Perdidas Control", "Diversion Dependencia",
           "Problemas Digestivos", "Tension Alta", "Dolor Cabeza")

treeview_encuestas = ttk.Treeview(frame_listbox, columns=columns, show="headings", yscrollcommand=scrollbar.set)
for col in columns:
    treeview_encuestas.heading(col, text=col)
    treeview_encuestas.column(col, width=100)
treeview_encuestas.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
scrollbar.config(command=treeview_encuestas.yview)

treeview_encuestas.bind('<<TreeviewSelect>>', on_select)

frame_buscar = ttk.Frame(frame_principal, padding="10")
frame_buscar.pack(fill=tk.X)

tk.Label(frame_buscar, text="Buscar por Edad:", font=("Arial", 12), bg="#2C3E50", fg="#ECF0F1").grid(row=0, column=0, padx=5, pady=5, sticky="w")
entry_buscar_edad = ttk.Entry(frame_buscar, font=("Arial", 12))
entry_buscar_edad.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

tk.Label(frame_buscar, text="Buscar por Sexo:", font=("Arial", 12), bg="#2C3E50", fg="#ECF0F1").grid(row=1, column=0, padx=5, pady=5, sticky="w")
tk.Label(frame_buscar, text="Buscar por Edad:", font=("Arial", 12), bg="#2C3E50", fg="#ECF0F1").grid(row=0, column=0, padx=5, pady=5, sticky="w")
entry_buscar_edad = ttk.Entry(frame_buscar, font=("Arial", 12))
entry_buscar_edad.grid(row=0, column=1, padx=5, pady=5, sticky="ew")

tk.Label(frame_buscar, text="Buscar por Sexo:", font=("Arial", 12), bg="#2C3E50", fg="#ECF0F1").grid(row=1, column=0, padx=5, pady=5, sticky="w")
entry_buscar_sexo = ttk.Entry(frame_buscar, font=("Arial", 12))
entry_buscar_sexo.grid(row=1, column=1, padx=5, pady=5, sticky="ew")

tk.Button(frame_buscar, text="Buscar Encuestas", command=lambda: buscar_encuestas(entry_buscar_edad.get(), entry_buscar_sexo.get()), bg="#1ABC9C", fg="white", font=("Arial", 12, "bold"), relief="flat").grid(row=2, column=0, columnspan=2, pady=10)

root.mainloop()
