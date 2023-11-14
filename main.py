# Base de Datos 1 * Hito 3.
# ULS 2023

import tkinter as tk
from tkinter import ttk
import psycopg2
#from config import config


''' TODO--> # Mejorar metodo de Query para usuario
                - Implementar botones predeterminados con consultas relevantes.
                - Implementar ComboBox para que usuario eliga usando Mouse lo que quiere
            # Implementar barra/boton de Query. --> LISTO
            # Arreglar ancho dinamico columnas. --> LISTO
            # Eliminar primera columna vacia. --> LISTO
            # Login dentro de la APP. Por ahora se ponen los datos en bloque de codigo usando strings
'''

### Datos de DB/VPN
'''TODO: Funcion para conectar a cualquier SV. No tener que escribrir 
            datos en codigo, Login dentro de App.'''
connection = psycopg2.connect(
    host="10.4.3.195", # PUERTO 5432
    database="instrumentos",
    user="instrumentos_dev", # Temporal! - Cambiar a 'instrumento'
    password="5jaLgi6" 
)



# Se crea cursor
crsr = connection.cursor()

# Cuando se usa BOTON 'execute query' en UI, Se escribe proceso  en terminal.
''' TODO: Mejora para usuario en Query
    Deberia tomar query de barra input 'query entry' LISTO - 
    O de Botones con 'consulta relevantes', Tambien usar ComboBox (Pendiente) '''
        
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
        display_results(results)
        
        # Termina de usar cursor, Lo cierra.
        # crsr.close()
    except Exception as error:
        print('ERROR EXCEPT 2 rgt>> ')
        print(error)


    

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



# Ventana principal de UI. 
root = tk.Tk()
root.title("Base de Datos Instrumentos")


# Input para Queries.
# TODO: Implementar el tomar su input y pasarlo como Query.
query_entry = ttk.Entry(root, width=50)
query_entry.grid(row=0, column=0, padx=10, pady=10, columnspan=2)


# Btn 'Execute Query'
# TODO: Hacer que tome string actual de 'query_entry' barra input y lo pase como Query.
execute_button = ttk.Button(root, text="Hacer Consulta", command=execute_query)
execute_button.grid(row=0, column=2, padx=10, pady=10)


# Resultados en tabla.
'''TODO: Hacer que las columnas se adapten bien a largo del contenido.
         A veces se sale de la pantalla. '''
result_tree = ttk.Treeview(root, show="headings")
result_tree.grid(row=1, column=0, padx=10, pady=10, columnspan=3)

''' Este bloque TRY se ejecuta cuando se inicia el programa, No se que hacer con esto.
    Por ahora queda comentado.'''
''' Primer bloque TRY comentado
try:
    # Ejecuta la Query. En duro por ahora.
    query2 = query_entry.get()
    #crsr.execute('SELECT * FROM estudiante')
    crsr.execute(query2)
    
    # Recupera los resultados.
    results = crsr.fetchall()

    # Muestra los resultados en el panel de display tipo tabla
    display_results(results)
    
    # Termina de usar cursor, Lo cierra.
    #crsr.close()
except Exception as error:
    # Captura errores. como try-catch en Java. Muestra el error en la terminal.
    print('ERROR EXCEPT rgt>> ')
    print(error)

finally:
    # no hace nada por ahora.
    print('FINALLY rgt>>')
''' 
    
# Inicia y refresca la ventana de la UI.
root.mainloop()

# Cierra la connection. No estoy seguro si esta es la posicion correcta para esto.
crsr.close()
connection.close()