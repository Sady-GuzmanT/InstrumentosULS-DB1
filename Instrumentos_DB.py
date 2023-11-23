import tkinter as tk
#from tkinter import ttk, messagebox
import ttkbootstrap as ttk
from tkinter import messagebox
import psycopg2



''' TODO:
    # NOTA: ComboBox_Query1 se llama ComboBox pero es una Query fija, Se mantiene asi por orden.
                
      NOTA: Hay un elemento de 'tk.entry', Esta comentado, pero se mantiene por conveniencia.
    
    
    # Hay que hacer login dentro del programa en vez de poner datos de psycopg en codigo.
    
    # Agregar Tabs para separar funcionalidades. (Por ahora: Home, Consulta, Registro)
    
    # Agregar funciones de registro de prestamos. (y de estudiante?)
    
    # Agregar visualizacion de consulta, Puede ser cantidad de prestamos o cant tipos instrumentos
        prestados mensuales. (Mathplot lib??)
'''



# Configuracion de psycop CONNECT con PostgresSQL
connection = psycopg2.connect(
    host="10.4.3.195",  # PUERTO 5432
    database="instrumentos",
    user="instrumentos",  # Temporal! - Cambiar a 'instrumento'
    password="abKimY4"
)

# Crea cursor para hacer las consultas
crsr = connection.cursor()

# Elementos U.I. de programa. ---->


#root = ttk.Window(themename = 'yeti') # Tema claro
root = ttk.Window(themename = 'superhero') # temas oscuros: superhero, Darkly, Vapor
root.geometry("320x390") # Tamano ventana fijo
root.resizable(False, False) # Hace ventana no modificable. Ahorra hacerla dinamica.
root.title("Base de Datos Instrumentos")

# ### TITULO dentro de ventana
label_titulo = ttk.Label(
    root,
    text="Central Instrumentos ULS",
    font=("BlinkMacSystemFont", 16, "bold"),
    foreground="White",
    padding=(10, 10),
)
label_titulo.grid(row=0, column=0, padx=10, pady=10, columnspan=20)


# Muestra resultados en una nueva ventana resultado. (usa treeview)
def display_results_in_window(results):
    # Create a new window to display the results
    result_window = tk.Toplevel(root)
    result_window.title("Resultado Consulta")

    # Create a treeview widget to display the results
    result_tree = ttk.Treeview(result_window, show="headings")
    result_tree.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

    # Create a vertical scrollbar
    y_scrollbar = ttk.Scrollbar(result_window, orient="vertical", command=result_tree.yview)
    y_scrollbar.grid(row=0, column=1, sticky="ns")
    result_tree.configure(yscrollcommand=y_scrollbar.set)

    # Display column names
    columns = [desc[0] for desc in crsr.description]
    result_tree["columns"] = columns
    for col in columns:
        result_tree.heading(col, text=col)
        result_tree.column(col, anchor=tk.CENTER)

    # Display data
    for i, row in enumerate(results, 1):
        result_tree.insert("", "end", iid=i, values=tuple(row))

    # Update the window's layout to make it resizable
    result_window.grid_rowconfigure(0, weight=1)
    result_window.grid_columnconfigure(0, weight=1)


# Logica Consultas. --->



# Ejecuta query de grupo combobox 1 - Ver estudiantes
def execute_combobox_query1():
    query = f"SELECT * FROM estudiante"
    try:
        crsr.execute(query)
        results = crsr.fetchall()
        display_results_in_window(results)
    except Exception as error:
        print('ERROR EXCEPT Combobox rgt>> ')
        print(error)
        messagebox.showerror("Error", str(error))



# Ejecuta query de grupo combobox 2 - Ver Prestamos * Eventual y Anual
def execute_combobox_query2():
    selected_item = combobox_query2.get()

    if selected_item == "Eventual":
        query = f"SELECT NombreDePila AS Nombre_Estudiante, rut AS rut_Estudiante, i.numSerie AS Num_Serie_Intrumento \
                    FROM Estudiante e \
                    INNER JOIN prestamo_eventual p ON e.rut = p.rutest \
                    INNER JOIN Instrumento i ON p.NumSerieInst = i.NumSerie"
        try:
            crsr.execute(query)
            results = crsr.fetchall()
            display_results_in_window(results)
        except Exception as error:
            print('ERROR EXCEPT Combobox rgt>> ')
            print(error)
    else:
        query = f"SELECT NombreDePila AS Nombre_Estudiante, rut AS rut_Estudiante, i.numSerie AS Num_Serie_Intrumento \
                    FROM Estudiante e \
                    INNER JOIN gestiona g ON e.rut = g.rutest \
                    INNER JOIN instrumento i ON g.numserieinst = i.numserie"
        try:
            crsr.execute(query)
            results = crsr.fetchall()
            display_results_in_window(results)
        except Exception as error:
            print('ERROR EXCEPT Combobox rgt>> ')
            print(error)
            messagebox.showerror("Error", str(error))


# Ejecuta query de grupo combobox 3. 'Ver Instrumento'
# TODO: Agregar mas tipos de instrumentos.
def execute_combobox_query3():
    selected_item = combobox_query3.get()

    if selected_item == "":
        query = f"SELECT * FROM instrumento"
        try:
            crsr.execute(query)
            results = crsr.fetchall()
            display_results_in_window(results)
        except Exception as error:
            print('ERROR EXCEPT Combobox rgt>> ')
            print(error)
            messagebox.showerror("Error", str(error))
    elif selected_item == "Todos":
        query = f"SELECT * FROM instrumento"
        try:
            crsr.execute(query)
            results = crsr.fetchall()
            display_results_in_window(results)
        except Exception as error:
            print('ERROR EXCEPT Combobox rgt>> ')
            print(error)
            messagebox.showerror("Error", str(error))
    else:
        query = f"SELECT * FROM instrumento WHERE nombre = '{selected_item}'"
        try:
            crsr.execute(query)
            results = crsr.fetchall()
            display_results_in_window(results)
        except Exception as error:
            print('ERROR EXCEPT Combobox rgt>> ')
            print(error)
            messagebox.showerror("Error", str(error))


# Ejecuta query de grupo combobox 4. - Ver prestamos de estudiante especifico por rut
def execute_combobox_query4():
    selected_item = combobox_query4.get()
    query = f"SELECT e.RUT AS RUT_Estudiante, i.NumSerie AS Num_Serie_Instrumento, s.EstadoSolicitud, COUNT(s.RutEst) AS Cant_Veces_Prestado \
                FROM Estudiante e \
                INNER JOIN Solicita s ON e.RUT = s.RutEst \
                INNER JOIN Instrumento i ON i.NumSerie = s.NumSerieInst \
                WHERE e.RUT = '{selected_item}' \
                GROUP BY e.RUT, s.RutEst, i.NumSerie, s.EstadoSolicitud"
    try:
        crsr.execute(query)
        results = crsr.fetchall()
        display_results_in_window(results)
    except Exception as error:
        print('ERROR EXCEPT Combobox rgt>> ')
        print(error)
        messagebox.showerror("Error", str(error))









# Elementos de U.I. De Consultas ---->

# ### 1ra consulta - VER ESTUDIANTES
# Label para combobox 1
label_combobox1 = ttk.Label(root, text="Ver Estudiantes", font=("Arial", 9, "bold"))
label_combobox1.grid(row=1, column=0, padx=10, pady=10)

# Btn 'Execute Combobox Query' 1
execute_combobox_button1 = ttk.Button(root, text="Hacer Consulta", command=execute_combobox_query1)
execute_combobox_button1.grid(row=1, column=1, padx=10, pady=10)




# ### 2da consulta - VER PRESTAMOS
# Label para combobox 2
label_combobox2 = ttk.Label(root, text="Ver Prestamos", font=("Arial", 9, "bold"))
label_combobox2.grid(row=3, column=0, padx=10, pady=10)

# Combobox2
combobox_query_values2 = ["Eventual", "Anual"]
combobox_query2 = ttk.Combobox(root, values=combobox_query_values2)
combobox_query2.grid(row=4, column=0, padx=10, pady=10)

# Btn 'Execute Combobox Query' 2
execute_combobox_button2 = ttk.Button(root, text="Hacer Consulta", command=execute_combobox_query2)
execute_combobox_button2.grid(row=4, column=1, padx=10, pady=10)




# ### 3ra consulta - VER INSTRUMENTOS
# Label para combobox 3
label_combobox3 = ttk.Label(root, text="Ver Instrumentos", font=("Arial", 9, "bold"))
label_combobox3.grid(row=5, column=0, padx=10, pady=10)

# Combobox 3
combobox_query_values3 = ["Todos", "Baritono", "Clarinete", "Corno", "Trombon", "Trompeta", "Tuba", "Viola", "Violin", "Violoncello"]
combobox_query3 = ttk.Combobox(root, values=combobox_query_values3)
combobox_query3.grid(row=6, column=0, padx=10, pady=10)

# Btn 'Execute Combobox Query' 3
execute_combobox_button3 = ttk.Button(root, text="Hacer Consulta", command=execute_combobox_query3)
execute_combobox_button3.grid(row=6, column=1, padx=10, pady=10)




# ### 4ta consulta - VER PRESTAMOS HISTORICOS DE ESTUDIANTE
# Label para combobox 4
label_combobox4 = ttk.Label(root, text="Prestamos de un Estudiante", font=("Arial", 9, "bold"))
label_combobox4.grid(row=7, column=0, padx=10, pady=10)

# Combobox4
combobox_query4 = ttk.Entry(width=25)
combobox_query4.grid(row=8, column=0, padx=10, pady=10)

# Btn 'Execute Combobox Query' 4
execute_combobox_button4 = ttk.Button(root, text="Hacer Consulta", command=execute_combobox_query4)
execute_combobox_button4.grid(row=8, column=1, padx=10, pady=10)



# Fin codigo, Las lineas siguientes tienen que estar al final del archivo para que funcione correctamente.

# Inicia y refresca la ventana de la UI.
root.mainloop()

# Cierra la connection y el cursor al salir de la aplicación.
crsr.close()
connection.close()
