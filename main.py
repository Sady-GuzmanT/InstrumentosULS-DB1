# Base de Datos 1 * Hito 3.
# ULS 2023

import tkinter as tk
from tkinter import ttk
import psycopg2
#from config import config


# TODO ---> # Implementar botones predeterminados con consultas relevantes.
            # Implementar barra/boton de Query.
            # Arreglar ancho dinamico columnas.

# Datos de DB/VPN
connection = psycopg2.connect(
    host="10.4.3.195", # PUERTO 5432
    database="instrumentos",
    user="instrumentos_dev", # Temporal! - Cambiar a 'instrumento'
    password="5jaLgi6" 
)


# Se crea cursor
crsr = connection.cursor()

# Cuando se usa btn'execute query' en UI, Se escribe 'log' en terminal.
# TODO: Implementar funcionalidad junto a barra de Query.
def execute_query():
    # Your function code here
    print("TERMINAL rgt>> Executing query...")

# Muestra resultados eN UI.
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



# Ventana principal de UI. 
root = tk.Tk()
root.title("Base de Datos Instrumentos")


# Input para Queries.
# TODO: Implementar el tomar su input y pasarlo como Query.
query_entry = ttk.Entry(root, width=50)
query_entry.grid(row=0, column=0, padx=10, pady=10, columnspan=2)


# Btn 'Execute Query'
# TODO: Hacer que tome string actual de 'query_entry' barra input y lo pase como Query.
execute_button = ttk.Button(root, text="Execute Query", command=execute_query)
execute_button.grid(row=0, column=2, padx=10, pady=10)


# Resultados en tabla.
# TODO: Hacer que las columnas se adapten bien a el largo del contenido. A veces se sale de la pantalla
result_tree = ttk.Treeview(root)
result_tree.grid(row=1, column=0, padx=10, pady=10, columnspan=3)


# Bloque de Query. Por ahora esta en 'duro'
# TODO: Deberia tomar query de barra input 'query entry' o de Botones con 'consulta relevantes' (Pendientes)
try:
    # Ejecuta la Query. En duro por ahora.
    crsr.execute('SELECT * FROM estudiante')
    
    # Recupera los resultados.
    results = crsr.fetchall()

    # Muestra los resultados en el panel de display tipo tabla
    display_results(results)
    
    # Termina de usar cursor, Lo cierra.
    crsr.close()
except Exception as error:
    # Captura errores. como try-catch en Java. Muestra el error en la terminal.
    print('ERROR EXCEPT rgt>> ')
    print(error)

finally:
    # no hace nada por ahora.
    print('FINALLY rgt>>')
    
    
    

# Cierra la connection. No estoy seguro si esta es la posicion correcta para esto.
connection.close()

# Inicia y refresca la ventana de la UI.
root.mainloop()