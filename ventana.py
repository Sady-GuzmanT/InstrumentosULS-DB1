import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import psycopg2

# Your PostgreSQL connection details here
connection = psycopg2.connect(
    host="10.4.3.195",  # PUERTO 5432
    database="instrumentos",
    user="instrumentos_dev",  # Temporal! - Cambiar a 'instrumento'
    password="5jaLgi6"
)

# Se crea cursor
crsr = connection.cursor()


# Cuando se usa BOTON 'execute query' en UI, Se escribe proceso  en terminal.
def execute_query():
    # Recupera string de entry query_entry
    query = query_entry.get()

    try:
        print("TERMINAL rgt>> Executing query 2...")
        # --> De aqui para abajo es lo mismo que en 1er bloque TRY EXCEPT
        # Ejec Query
        crsr.execute(query)

        # Recupera los resultados.
        results = crsr.fetchall()

        # Muestra los resultados en el panel de display tipo tabla
        display_results_in_window(results)

    except Exception as error:
        print('ERROR EXCEPT 2 rgt>> ')
        print(error)
        messagebox.showerror("Error", str(error))


# Muestra resultados en UI.
def display_results(results):
    # Limpia el resultado anterior
    result_tree.delete(*result_tree.get_children())

    # Header de las columnas.
    columns = [desc[0] for desc in crsr.description]
    result_tree["columns"] = columns
    for col in columns:
        result_tree.heading(col, text=col)
        result_tree.column(col, anchor=tk.CENTER)

    # Contenido.
    for i, row in enumerate(results, 1):
        result_tree.insert("", "end", iid=i, values=tuple(row))


# Muestra resultados en una nueva ventana.
def display_results_in_window(results):
    # Create a new window to display the results
    result_window = tk.Toplevel(root)
    result_window.title("Query Results")

    # Create a treeview widget to display the results
    result_tree = ttk.Treeview(result_window)
    result_tree.grid(row=0, column=0, padx=10, pady=10)

    # Display column names
    columns = [desc[0] for desc in crsr.description]
    result_tree["columns"] = columns
    for col in columns:
        result_tree.heading(col, text=col, show="headings")
        result_tree.column(col, anchor=tk.CENTER)

    # Display data
    for i, row in enumerate(results, 1):
        result_tree.insert("", "end", iid=i, values=tuple(row))


# Ventana principal de UI.
root = tk.Tk()
root.title("Base de Datos Instrumentos")

# Input para Queries.
query_entry = ttk.Entry(root, width=50)
query_entry.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

# Btn 'Execute Query'
execute_button = ttk.Button(root, text="Hacer Consulta", command=execute_query)
execute_button.grid(row=0, column=2, padx=10, pady=10)

# Resultados en tabla.
result_tree = ttk.Treeview(root, show="headings")
result_tree.grid(row=1, column=0, padx=10, pady=10, columnspan=3)

# Inicia y refresca la ventana de la UI.
root.mainloop()

# Cierra la connection y el cursor al salir de la aplicación.
crsr.close()
connection.close()
