import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import psycopg2


''' TODO:
    # Para cada boton de EXECUTE_QUERY tiene que haber un procedimiento de EXECUTE_QUERY()
        distinto. Dentro de ese DEF especial se aplican las condiciones.
        Cada DEF EXECUTE_QUERY() va a tener la tabla puesta por defecto y lo que cambia es
        el valor de WHERE = {CUSTOM}.
        Si el ComboBox esta en 'TODOS' se usa un string de Query especial, Sin WHERE
        Si el ComboBox es distinto de 'todos' se usa query string con condicion WHERE = {}
    
    # Hay que enconder boton y barra original. Por ahora se mantiene por conveniencia
    
    # Hay que hacer login dentro del programa en vez de poner datos de psycopg en codigo
'''

# Configuracion de psycop CONNECT ---> Hacerlo con login en futura version.
connection = psycopg2.connect(
    host="10.4.3.195",  # PUERTO 5432
    database="instrumentos",
    user="instrumentos_dev",  # Temporal! - Cambiar a 'instrumento'
    password="5jaLgi6"
)


# ### Logica.


# Create a cursor
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


# Execute query based on Combobox content
def execute_combobox_query():
    selected_item = query_entry.get()
    query = f"SELECT * FROM instrumento WHERE nombre = '{selected_item}'"  # Modify this query based on your table and column
    try:
        crsr.execute(query)
        results = crsr.fetchall()
        display_results_in_window(results)
    except Exception as error:
        print('ERROR EXCEPT Combobox rgt>> ')
        print(error)
        messagebox.showerror("Error", str(error))


# Muestra resultados en UI. \ Ya no se usa, pero es bueno mantenerlo
''' def display_results(results):
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
'''

# Muestra resultados en una nueva ventana.

def display_results_in_window(results):
    # Create a new window to display the results
    result_window = tk.Toplevel(root)
    result_window.title("Query Results")

    # Create a treeview widget to display the results
    result_tree = ttk.Treeview(result_window, show="headings")
    result_tree.grid(row=0, column=0, padx=10, pady=10)

    # Display column names
    columns = [desc[0] for desc in crsr.description]
    result_tree["columns"] = columns
    for col in columns:
        result_tree.heading(col, text=col)
        result_tree.column(col, anchor=tk.CENTER)

    # Display data
    for i, row in enumerate(results, 1):
        result_tree.insert("", "end", iid=i, values=tuple(row))




# ### ---> ELEMENTOS DE U.I.

# Ventana principal de UI.
root = tk.Tk()
root.title("Base de Datos Instrumentos")


# QUERY BAR Y BTN ORIGINALES --> Hay que comentarlos despues.

# Input para Queries. \ Hay que comentar este bloque despues
query_entry = ttk.Entry(root, width=50)
query_entry.grid(row=10, column=0, padx=10, pady=10, columnspan=2)

# Btn 'Execute Query'. \ Hay que comentar este bloque despues
execute_button = ttk.Button(root, text="Hacer Consulta", command=execute_query)
execute_button.grid(row=10, column=2, padx=10, pady=10)


# ### TITULO dentro de ventana
label_titulo = tk.Label(
    root,
    text="Central Instrumentos ULS",
    font=("Arial", 14, "bold"),
    fg="blue",
    bg="#dedede",
    padx=10,
    pady=10,
)
label_titulo.grid(row=0, column=0, padx=10, pady=10, columnspan=20)



# Conjunto de ComboBox y Boton de ejecucion de ComboBox_Query.

# ### 1ra consulta

# Label para combobox 1
label_combobox1 = ttk.Label(root, text="Ver Disponibles")
label_combobox1.grid(row=1, column=0, padx=10, pady=10)

# Combobox1 -- No se usa
    #combobox_query_values3 = ["Anual", "Eventual"]
    #combobox_query3 = ttk.Combobox(root, values=combobox_query_values3)
    #combobox_query3.grid(row=3, column=0, padx=10, pady=10)

# Btn 'Execute Combobox Query' 1
execute_combobox_button1 = ttk.Button(root, text="Hacer Consulta", command=execute_combobox_query)
execute_combobox_button1.grid(row=1, column=1, padx=10, pady=10)



# ### 2da consulta

# Label para combobox 2
label_combobox2 = ttk.Label(root, text="Ver Prestamos")
label_combobox2.grid(row=3, column=0, padx=10, pady=10)

# Combobox2
combobox_query_values2 = ["Anual", "Eventual"]
combobox_query2 = ttk.Combobox(root, values=combobox_query_values2)
combobox_query2.grid(row=4, column=0, padx=10, pady=10)

# Btn 'Execute Combobox Query' 2 
execute_combobox_button2 = ttk.Button(root, text="Hacer Consulta", command=execute_combobox_query)
execute_combobox_button2.grid(row=4, column=1, padx=10, pady=10)



# ### 3ra consulta

# Label para combobox 3
label_combobox3 = ttk.Label(root, text="Ver Instrumentos")
label_combobox3.grid(row=5, column=0, padx=10, pady=10)

# Combobox 3
combobox_query_values3 = ["Todos", "Violin", "Corno"]
combobox_query3 = ttk.Combobox(root, values=combobox_query_values3)
combobox_query3.grid(row=6, column=0, padx=10, pady=10)

# Btn 'Execute Combobox Query' 3
execute_combobox_button3 = ttk.Button(root, text="Hacer Consulta", command=execute_combobox_query)
execute_combobox_button3.grid(row=6, column=1, padx=10, pady=10)



# ### 4ta consulta

# Label para combobox 4
label_combobox4 = ttk.Label(root, text="Pensar Consulta")
label_combobox4.grid(row=7, column=0, padx=10, pady=10)

# Combobox4
combobox_query_values4 = ["Pensar opcion1", "Pensar opcion2"]
combobox_query4 = ttk.Combobox(root, values=combobox_query_values4)
combobox_query4.grid(row=8, column=0, padx=10, pady=10)

# Btn 'Execute Combobox Query' 4 
execute_combobox_button4 = ttk.Button(root, text="Hacer Consulta", command=execute_combobox_query)
execute_combobox_button4.grid(row=8, column=1, padx=10, pady=10)




# TreeView para ver resultados de la Query.
'''#Resultados en tabla. --> Ahora queda comentado, porque se ven los resultados en nueva ventana.
result_tree = ttk.Treeview(root, show="headings")
result_tree.grid(row=2, column=0, padx=10, pady=10, columnspan=3)
'''




# Inicia y refresca la ventana de la UI.
root.mainloop()

# Cierra la connection y el cursor al salir de la aplicación.
crsr.close()
connection.close()
