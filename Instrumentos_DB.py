import tkinter as tk
#from tkinter import ttk, messagebox
import ttkbootstrap as ttk
from ttkbootstrap import Style, Notebook
from tkinter import messagebox
import psycopg2
from PIL import Image, ImageTk


''' TODO:
    # NOTA: ComboBox_Query1 se llama ComboBox pero es una Query fija, Se mantiene asi por orden.
                
      NOTA: Hay un elemento de 'tk.entry', Esta comentado, pero se mantiene por conveniencia.
    
    
    # Hay que hacer login dentro del programa en vez de poner datos de psycopg en codigo ??
    
    # Agregar Tabs para separar funcionalidades. (Por ahora: Home, Consulta, Registro) --  > Listo. 
                Falta agregar funciones a tab3: REGISTRA.
                    UI de tab3 - LISTO
                    UI de ventanas de opciones tab 3 - Pendiente
                    Extraer informacion de ventanas tab 3 - Pendiente
                    Funciones de Registro que usen la informacion extraida - Pendiente
                    Update a las tablas - Pendiente
    
   
    # Agregar visualizacion de consulta, Puede ser cantidad de prestamos o cant tipos instrumentos
        prestados mensuales. (Mathplot lib??)
        
    # TAB 3 Registros -->
        - Agregar funciones de registro para las 5 opciones.
        - Agregar respectivas ventanas a cada boton de registro.
            - Agregar elementos de UI a cada ventana.
        - Agregar fetch de informacion en ventanas de registro hacia
            las funciones de registro.
        * Por ahora todas estas funciones van a afectar la tabla
            'test_registros', Que fue creada para probar si los UPDATE
            que se crearon para la TAB3 funcionan correctamente.
            Cuando todo este OK, Se van a modificar las funcioens para
            que los cambios se hagan en las tablas correctas.
        * Confirmar con equipo si las UPDATES creadas son todo lo necesario
            para el correcto funcionamiento, O si falta agregar cosas.
        
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
root.geometry("550x440") # Tamano ventana fijo -> Con linea siguiente no es necesario. Se comenta
root.resizable(False, False) # Hace ventana no modificable. Ahorra hacerla dinamica.
root.title("Base de Datos Instrumentos")



# Creacion NOTEBOOK TABS 

# Crea un ttkbootstrap notebook, y agrega a ventana principal
notebook = Notebook(root, style="primary.TNotebook")
#notebook.pack(fill="both", expand=True)
notebook.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

# crea tabs para notebook
tab1 = tk.Frame(notebook)
tab2 = tk.Frame(notebook)
tab3 = tk.Frame(notebook)

# agrega las tabs al notebook
notebook.add(tab1, text="Home")
notebook.add(tab2, text="Consulta")
notebook.add(tab3, text="Registro")


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

# ### UPDATES para registros en las ventanas que se abren desde TAB3

def registrar_profesor():
    rut = entry_rut_profesor.get()
    nombre = entry_nombre_profesor.get()
    app1 = entry_app1_profesor.get()
    app2 = entry_app2_profesor.get()
    
    print("REGISTRA PROFESOR CON ESTOS DATOS")
    print("RUT:", rut)
    print("Nombre:", nombre)
    print("App1:", app1)
    print("App2:", app2)
    
    # Por ahora se esta testeando. Ya se logra actualizar valores hacia la tabla, Hay que copiar
    # el bloque de UPDATE y hacerlo para cada tabla que tiene que poder hacer UPDATE.
    
    
    query_update = f"INSERT INTO Test_Registros (rut_profesor, nombredepila, apellido1, apellido2)\
                        VALUES ('{rut}', '{nombre}', '{app1}', '{app2}')"
    
    update_cursor = connection.cursor() # Cursor para hacer update * TEST
    
    try:
        update_cursor.execute(query_update)
        connection.commit()
        update_cursor.close()
        messagebox.showinfo("Success", "Registro actualizado exitosamente")
        print('Exito: Se actualizo el registro con: ')
        print(f"INSERT INTO Test_Registros (rut_profesor, nombredepila, apellido1, apellido2)\
                        VALUES ('{rut}', '{nombre}', '{app1}', '{app2}')")
    except Exception as error:
        print('ERROR EXCEPT Combobox rgt>> ')
        print(error)
        messagebox.showerror("Error", str(error))




# Elementos U.I. de Home | TAB 1 ---->

# ### TITULO dentro de ventana
label_titulo = ttk.Label(
    tab1,
    text="Central Instrumentos ULS",
    font=("BlinkMacSystemFont", 16, "bold"),
    foreground="White",
    padding=(10, 10),
)
label_titulo.grid(row=0, column=0, padx=10, pady=10, columnspan=20)

# ### Instrucciones de uso.
label_indicaciones = ttk.Label(
    tab1,
    text="Para usar el programa hay que navegar las pestanas en la barra superior.\
        \n\n*Consulta: Se obtiene informacion relevante. Seleccionar categoria en ComboBox\n\t  y hacer consulta.\
            \n\n*Registro: Se Registran nuevos prestamos, Estudiantes, Instrumentos, y Profesores.",
    font=("BlinkMacSystemFont", 10),
    foreground="White",
    padding=(10, 10),
)
label_indicaciones.grid(row=2, column=0, padx=5, pady=10, columnspan=20)

# ### Agrega imagen de ULS. (Preguntar a profesor si esta bien agregar esa imagen.)
image_path = "logo.png"
img = Image.open(image_path)
img = img.resize((300, 150))  # dimension logo
image = ImageTk.PhotoImage(img)

image_label = ttk.Label(tab1, image=image, background="White") # Se agrega fondo blanco porque es un png sin fondo.
image_label.grid(row=3, column=10, padx=10, pady=10)



# Elementos de U.I. De Consultas | TAB 2---->

# ### 1ra consulta - VER ESTUDIANTES
# Label para combobox 1
label_combobox1 = ttk.Label(tab2, text="Ver Estudiantes", font=("Arial", 9, "bold"))
label_combobox1.grid(row=1, column=0, padx=10, pady=10)

# Btn 'Execute Combobox Query' 1
execute_combobox_button1 = ttk.Button(tab2, text="Hacer Consulta", command=execute_combobox_query1, width=20)
execute_combobox_button1.grid(row=1, column=1, padx=10, pady=10)




# ### 2da consulta - VER PRESTAMOS
# Label para combobox 2
label_combobox2 = ttk.Label(tab2, text="Ver Prestamos", font=("Arial", 9, "bold"))
label_combobox2.grid(row=3, column=0, padx=10, pady=10)

# Combobox2
combobox_query_values2 = ["Eventual", "Anual"]
combobox_query2 = ttk.Combobox(tab2, values=combobox_query_values2)
combobox_query2.grid(row=4, column=0, padx=10, pady=10)

# Btn 'Execute Combobox Query' 2
execute_combobox_button2 = ttk.Button(tab2, text="Hacer Consulta", command=execute_combobox_query2, width=20)
execute_combobox_button2.grid(row=4, column=1, padx=10, pady=10)




# ### 3ra consulta - VER INSTRUMENTOS
# Label para combobox 3
label_combobox3 = ttk.Label(tab2, text="Ver Instrumentos", font=("Arial", 9, "bold"))
label_combobox3.grid(row=5, column=0, padx=10, pady=10)

# Combobox 3
combobox_query_values3 = ["Todos", "Baritono", "Clarinete", "Corno", "Trombon", "Trompeta", "Tuba", "Viola", "Violin", "Violoncello"]
combobox_query3 = ttk.Combobox(tab2, values=combobox_query_values3)
combobox_query3.grid(row=6, column=0, padx=10, pady=10)

# Btn 'Execute Combobox Query' 3
execute_combobox_button3 = ttk.Button(tab2, text="Hacer Consulta", command=execute_combobox_query3, width=20)
execute_combobox_button3.grid(row=6, column=1, padx=10, pady=10)




# ### 4ta consulta - VER PRESTAMOS HISTORICOS DE ESTUDIANTE
# Label para combobox 4
label_combobox4 = ttk.Label(tab2, text="Prestamos de un Estudiante", font=("Arial", 9, "bold"))
label_combobox4.grid(row=7, column=0, padx=10, pady=10)

# Combobox4
combobox_query4 = ttk.Entry(tab2, width=25)
combobox_query4.grid(row=8, column=0, padx=10, pady=10)

# Btn 'Execute Combobox Query' 4
execute_combobox_button4 = ttk.Button(tab2, text="Hacer Consulta", command=execute_combobox_query4, width=20)
execute_combobox_button4.grid(row=8, column=1, padx=10, pady=10)

# Centra elementos de Tab1 - Consulta
tab2.columnconfigure(0, weight=1)
tab2.columnconfigure(1, weight=1)




# ### Tab3 | UI de REGISTROS --->

def print_mock():
    print("hola esto es una mock func")
    
# ### TAB3 | Ventanas de registro
def ventana_registro_estudiante():
    # Crea la ventana, La hace de tamano fijo
    ventana_registro = tk.Toplevel(root)
    ventana_registro.title("Registro de Estudiante")
    ventana_registro.geometry("500x460")
    ventana_registro.resizable(False, False)
    
    # Titulo dentro de ventana
    label_titulo_registra_estudiante = ttk.Label(
    ventana_registro,
    text="Registro Estudiante",
    font=("BlinkMacSystemFont", 16, "bold"),
    foreground="White",
    padding=(10, 10),
    )
    label_titulo_registra_estudiante.grid(row=1, column=0, padx=10, pady=10, columnspan=20)
    
    
    # Agrega labels y TextEntries para cada campo.
    
    label_rut_estudiante = ttk.Label(ventana_registro, text="RUT", font=("Arial", 10, "bold"))
    label_rut_estudiante.grid(row=2, column=0, padx=(15,0), pady=(20,0))
    
    entry_rut_estudiante = ttk.Entry(ventana_registro, width=30)
    entry_rut_estudiante.grid(row=3, column=0, padx=(15,0), pady=(0,10))
    
    
    label_nombre_estudiante = ttk.Label(ventana_registro, text="Nombre", font=("Arial", 10, "bold"))
    label_nombre_estudiante.grid(row=2, column=1, padx=(80,0), pady=(20,0))
    
    entry_nombre_estudiante = ttk.Entry(ventana_registro, width=30)
    entry_nombre_estudiante.grid(row=3, column=1, padx=(80,0), pady=(0,10))
    
    
    
    
    label_app1_estudiante = ttk.Label(ventana_registro, text="Apelido Paterno", font=("Arial", 10, "bold"))
    label_app1_estudiante.grid(row=4, column=0, padx=(15,0), pady=(20,0))
    
    entry_app1_estudiante = ttk.Entry(ventana_registro, width=30)
    entry_app1_estudiante.grid(row=5, column=0, padx=(15,0), pady=(0,10))
    
    
    label_app2_estudiante = ttk.Label(ventana_registro, text="Apelido Materno", font=("Arial", 10, "bold"))
    label_app2_estudiante.grid(row=4, column=1, padx=(80,0), pady=(20,0))
    
    entry_app2_estudiante = ttk.Entry(ventana_registro, width=30)
    entry_app2_estudiante.grid(row=5, column=1, padx=(80,0), pady=(0,10))
    
    
    
    
    label_tel_estudiante = ttk.Label(ventana_registro, text="Telefono", font=("Arial", 10, "bold"))
    label_tel_estudiante.grid(row=6, column=0, padx=(15,0), pady=(20,0))
    
    entry_tel_estudiante = ttk.Entry(ventana_registro, width=30)
    entry_tel_estudiante.grid(row=7, column=0, padx=(15,0), pady=(0,10))
    
    
    label_mail_estudiante = ttk.Label(ventana_registro, text="E-Mail", font=("Arial", 10, "bold"))
    label_mail_estudiante.grid(row=6, column=1, padx=(80,0), pady=(20,0))
    
    entry_mail_estudiante = ttk.Entry(ventana_registro, width=30)
    entry_mail_estudiante.grid(row=7, column=1, padx=(80,0), pady=(0,10))
    
    
    
    
    label_Carrera_estudiante = ttk.Label(ventana_registro, text="Carrera", font=("Arial", 10, "bold"))
    label_Carrera_estudiante.grid(row=8, column=0, padx=(15,0), pady=(20,0))
    
    entry_carrera_estudiante = ttk.Entry(ventana_registro, width=30)
    entry_carrera_estudiante.grid(row=9, column=0, padx=(15,0), pady=(0,10))
    
    
    label_CAR_estudiante = ttk.Label(ventana_registro, text="Certificado Alumno Regular", font=("Arial", 10, "bold"))
    label_CAR_estudiante.grid(row=8, column=1, padx=(80,0), pady=(20,0))
    
    entry_CAR_estudiante = ttk.Entry(ventana_registro, width=30)
    entry_CAR_estudiante.grid(row=9, column=1, padx=(80,0), pady=(0,10))
    
    
    # Boton para Completar Registro y sacar informacion.
    btn_registro_estudiante = ttk.Button(ventana_registro, text="Registrar Estudiante", command=print_mock, width=30)
    btn_registro_estudiante.grid(row=10, column=1, padx=(80,0), pady=(25,10))
    
    

def ventana_registro_profesor():
    # Hace las variables globales para poder acceder desde la ventana principal.
    # Quiza hay una mejor manera de hacer esto. Por ahora se usa GLOBAL
    global entry_rut_profesor, entry_nombre_profesor, entry_app1_profesor, entry_app2_profesor
    
    # Crea la ventana, La hace de tamano fijo
    ventana_registro = tk.Toplevel(root)
    ventana_registro.title("Registro de Profesor")
    ventana_registro.geometry("500x460")
    ventana_registro.resizable(False, False)
    
    # Titulo dentro de ventana
    label_titulo_registra_profesor = ttk.Label(
    ventana_registro,
    text="Registro Profesor",
    font=("BlinkMacSystemFont", 16, "bold"),
    foreground="White",
    padding=(10, 10),
    )
    label_titulo_registra_profesor.grid(row=1, column=0, padx=10, pady=10, columnspan=20)
    
    
    # Agrega labels y TextEntries para cada campo.
    
    label_rut_profesor = ttk.Label(ventana_registro, text="RUT", font=("Arial", 10, "bold"))
    label_rut_profesor.grid(row=2, column=0, padx=(15,0), pady=(20,0))
    
    entry_rut_profesor = ttk.Entry(ventana_registro, width=30)
    entry_rut_profesor.grid(row=3, column=0, padx=(15,0), pady=(0,10))
    
    
    label_nombre_profesor = ttk.Label(ventana_registro, text="Nombre", font=("Arial", 10, "bold"))
    label_nombre_profesor.grid(row=2, column=1, padx=(80,0), pady=(20,0))
    
    entry_nombre_profesor = ttk.Entry(ventana_registro, width=30)
    entry_nombre_profesor.grid(row=3, column=1, padx=(80,0), pady=(0,10))
    
    
    
    
    label_app1_profesor = ttk.Label(ventana_registro, text="Apelido Paterno", font=("Arial", 10, "bold"))
    label_app1_profesor.grid(row=4, column=0, padx=(15,0), pady=(20,0))
    
    entry_app1_profesor = ttk.Entry(ventana_registro, width=30)
    entry_app1_profesor.grid(row=5, column=0, padx=(15,0), pady=(0,10))
    
    
    label_app2_profesor = ttk.Label(ventana_registro, text="Apelido Materno", font=("Arial", 10, "bold"))
    label_app2_profesor.grid(row=4, column=1, padx=(80,0), pady=(20,0))
    
    entry_app2_profesor = ttk.Entry(ventana_registro, width=30)
    entry_app2_profesor.grid(row=5, column=1, padx=(80,0), pady=(0,10))
    
    
    
    # Boton para Completar Registro y sacar informacion.
    btn_registro_profesor = ttk.Button(ventana_registro, text="Registrar Profesor", command=registrar_profesor, width=30)
    btn_registro_profesor.grid(row=10, column=1, padx=(80,0), pady=(180,10))
    
    

    
def ventana_registro_instrumento():
    # Crea la ventana, La hace de tamano fijo
    ventana_registro = tk.Toplevel(root)
    ventana_registro.title("Registro de Instrumento")
    ventana_registro.geometry("500x460")
    ventana_registro.resizable(False, False)
    
    # Titulo dentro de ventana
    label_titulo_registra_instrumento = ttk.Label(
    ventana_registro,
    text="Registro Instrumento",
    font=("BlinkMacSystemFont", 16, "bold"),
    foreground="White",
    padding=(10, 10),
    )
    label_titulo_registra_instrumento.grid(row=1, column=0, padx=10, pady=10, columnspan=20)
    
    
    # Agrega labels y TextEntries para cada campo.
    
    label_num_serie_instrumento = ttk.Label(ventana_registro, text="Numero de Serie", font=("Arial", 10, "bold"))
    label_num_serie_instrumento.grid(row=2, column=0, padx=(15,0), pady=(20,0))
    
    entry_num_serie_instrumento = ttk.Entry(ventana_registro, width=30)
    entry_num_serie_instrumento.grid(row=3, column=0, padx=(15,0), pady=(0,10))
    
    
    label_num_inv_instrumento = ttk.Label(ventana_registro, text="Numero de Inventario", font=("Arial", 10, "bold"))
    label_num_inv_instrumento.grid(row=2, column=1, padx=(80,0), pady=(20,0))
    
    entry_num_inv_instrumento = ttk.Entry(ventana_registro, width=30)
    entry_num_inv_instrumento.grid(row=3, column=1, padx=(80,0), pady=(0,10))
    
    
    
    
    label_nombre_instrumento = ttk.Label(ventana_registro, text="Nombre", font=("Arial", 10, "bold"))
    label_nombre_instrumento.grid(row=4, column=0, padx=(15,0), pady=(20,0))
    
    entry_nombre_instrumento = ttk.Entry(ventana_registro, width=30)
    entry_nombre_instrumento.grid(row=5, column=0, padx=(15,0), pady=(0,10))
    
    
    label_marca_instrumento = ttk.Label(ventana_registro, text="Marca", font=("Arial", 10, "bold"))
    label_marca_instrumento.grid(row=4, column=1, padx=(80,0), pady=(20,0))
    
    entry_marca_instrumento = ttk.Entry(ventana_registro, width=30)
    entry_marca_instrumento.grid(row=5, column=1, padx=(80,0), pady=(0,10))
    
    
    
    
    label_medidas_instrumento = ttk.Label(ventana_registro, text="Medidas", font=("Arial", 10, "bold"))
    label_medidas_instrumento.grid(row=6, column=0, padx=(15,0), pady=(20,0))
    
    entry_medidas_instrumento = ttk.Entry(ventana_registro, width=30)
    entry_medidas_instrumento.grid(row=7, column=0, padx=(15,0), pady=(0,10))
    
    
    label_avaluo_instrumento = ttk.Label(ventana_registro, text="Avaluo", font=("Arial", 10, "bold"))
    label_avaluo_instrumento.grid(row=6, column=1, padx=(80,0), pady=(20,0))
    
    entry_avaluo_instrumento = ttk.Entry(ventana_registro, width=30)
    entry_avaluo_instrumento.grid(row=7, column=1, padx=(80,0), pady=(0,10))
    
    
    
    
    label_estado_instrumento = ttk.Label(ventana_registro, text="Estado", font=("Arial", 10, "bold"))
    label_estado_instrumento.grid(row=8, column=0, padx=(15,0), pady=(20,0))
    
    entry_estado_instrumento = ttk.Entry(ventana_registro, width=30)
    entry_estado_instrumento.grid(row=9, column=0, padx=(15,0), pady=(0,10))
    
    
    
    
    # Boton para Completar Registro y sacar informacion.
    btn_registro_instrumento = ttk.Button(ventana_registro, text="Registrar Instrumento", command=print_mock, width=30)
    btn_registro_instrumento.grid(row=10, column=1, padx=(80,0), pady=(25,10))
    


def ventana_registro_eventual():
    # Crea la ventana, La hace de tamano fijo
    ventana_registro = tk.Toplevel(root)
    ventana_registro.title("Registro de Eventual")
    ventana_registro.geometry("500x460")
    ventana_registro.resizable(False, False)
    
    # Titulo dentro de ventana
    label_titulo_registra_eventual = ttk.Label(
    ventana_registro,
    text="Registro Prestamo Eventual",
    font=("BlinkMacSystemFont", 16, "bold"),
    foreground="White",
    padding=(10, 10),
    )
    label_titulo_registra_eventual.grid(row=1, column=0, padx=10, pady=10, columnspan=20)
    
    
    # Agrega labels y TextEntries para cada campo.
    
    label_rut_prestamo_eventual = ttk.Label(ventana_registro, text="Rut Estudiante", font=("Arial", 10, "bold"))
    label_rut_prestamo_eventual.grid(row=2, column=0, padx=(15,0), pady=(20,0))
    
    entry_rut_prestamo_eventual = ttk.Entry(ventana_registro, width=30)
    entry_rut_prestamo_eventual.grid(row=3, column=0, padx=(15,0), pady=(0,10))
    
    
    label_rut2_prestamo_eventual = ttk.Label(ventana_registro, text="Rut Encargado", font=("Arial", 10, "bold"))
    label_rut2_prestamo_eventual.grid(row=2, column=1, padx=(80,0), pady=(20,0))
    
    entry_rut2_prestamo_eventual = ttk.Entry(ventana_registro, width=30)
    entry_rut2_prestamo_eventual.grid(row=3, column=1, padx=(80,0), pady=(0,10))
    
    
    
    
    label_numserie_eventual = ttk.Label(ventana_registro, text="Numero Serie de Instrumento", font=("Arial", 10, "bold"))
    label_numserie_eventual.grid(row=4, column=0, padx=(15,0), pady=(20,0))
    
    entry_numserie_eventual = ttk.Entry(ventana_registro, width=30)
    entry_numserie_eventual.grid(row=5, column=0, padx=(15,0), pady=(0,10))
    
    
    label_fechainicio_eventual = ttk.Label(ventana_registro, text="Fecha Inicio", font=("Arial", 10, "bold"))
    label_fechainicio_eventual.grid(row=4, column=1, padx=(80,0), pady=(20,0))
    
    entry_fechainicio_eventual = ttk.Entry(ventana_registro, width=30)
    entry_fechainicio_eventual.grid(row=5, column=1, padx=(80,0), pady=(0,10))
    
    
    
    
    label_fechatermino_eventual = ttk.Label(ventana_registro, text="Fecha Termino", font=("Arial", 10, "bold"))
    label_fechatermino_eventual.grid(row=6, column=0, padx=(15,0), pady=(20,0))
    
    entry_fechatermino_eventual = ttk.Entry(ventana_registro, width=30)
    entry_fechatermino_eventual.grid(row=7, column=0, padx=(15,0), pady=(0,10))
    
    
    
    label_info = ttk.Label(ventana_registro, text="Formato Fechas: YYYY-MM-DD", font=("Arial", 8, "bold"))
    label_info.grid(row=8, column=0, padx=(15,0), pady=(20,0))
    
    
    
    
    # Boton para Completar Registro y sacar informacion.
    btn_registro_eventual = ttk.Button(ventana_registro, text="Registrar Prestamo", command=print_mock, width=30)
    btn_registro_eventual.grid(row=10, column=1, padx=(80,0), pady=(75,10))
    



def ventana_registro_anual():
    # Crea la ventana, La hace de tamano fijo
    ventana_registro = tk.Toplevel(root)
    ventana_registro.title("Registro de Prestamo Anual")
    ventana_registro.geometry("500x515")
    ventana_registro.resizable(False, False)
    
    # Titulo dentro de ventana
    label_titulo_registra_estudiante = ttk.Label(
    ventana_registro,
    text="Registro Anual",
    font=("BlinkMacSystemFont", 16, "bold"),
    foreground="White",
    padding=(10, 10),
    )
    label_titulo_registra_estudiante.grid(row=1, column=0, padx=10, pady=10, columnspan=20)
    
    
    # Agrega labels y TextEntries para cada campo.
    
    label_codigo_anual = ttk.Label(ventana_registro, text="Codigo Contrato", font=("Arial", 10, "bold"))
    label_codigo_anual.grid(row=2, column=0, padx=(15,0), pady=(20,0))
    
    entry_codigo_anual = ttk.Entry(ventana_registro, width=30)
    entry_codigo_anual.grid(row=3, column=0, padx=(15,0), pady=(0,10))
    
    
    label_calle_anual = ttk.Label(ventana_registro, text="Calle", font=("Arial", 10, "bold"))
    label_calle_anual.grid(row=2, column=1, padx=(80,0), pady=(20,0))
    
    entry_calle_anual = ttk.Entry(ventana_registro, width=30)
    entry_calle_anual.grid(row=3, column=1, padx=(80,0), pady=(0,10))
    
    
    
    
    label_numcalle_anual = ttk.Label(ventana_registro, text="Numero Calle", font=("Arial", 10, "bold"))
    label_numcalle_anual.grid(row=4, column=0, padx=(15,0), pady=(20,0))
    
    entry_numcalle_anual = ttk.Entry(ventana_registro, width=30)
    entry_numcalle_anual.grid(row=5, column=0, padx=(15,0), pady=(0,10))
    
    
    label_comuna_anual = ttk.Label(ventana_registro, text="Comuna", font=("Arial", 10, "bold"))
    label_comuna_anual.grid(row=4, column=1, padx=(80,0), pady=(20,0))
    
    entry_comuna_anual = ttk.Entry(ventana_registro, width=30)
    entry_comuna_anual.grid(row=5, column=1, padx=(80,0), pady=(0,10))
    
    
    
    
    label_tel_anual = ttk.Label(ventana_registro, text="Telefono", font=("Arial", 10, "bold"))
    label_tel_anual.grid(row=6, column=0, padx=(15,0), pady=(20,0))
    
    entry_tel_anual = ttk.Entry(ventana_registro, width=30)
    entry_tel_anual.grid(row=7, column=0, padx=(15,0), pady=(0,10))
    
    
    label_nombre_director_anual = ttk.Label(ventana_registro, text="Nombre Director", font=("Arial", 10, "bold"))
    label_nombre_director_anual.grid(row=6, column=1, padx=(80,0), pady=(20,0))
    
    entry_nombre_director_anual = ttk.Entry(ventana_registro, width=30)
    entry_nombre_director_anual.grid(row=7, column=1, padx=(80,0), pady=(0,10))
    
    
    
    
    label_rut_director_anual = ttk.Label(ventana_registro, text="Rut Director", font=("Arial", 10, "bold"))
    label_rut_director_anual.grid(row=8, column=0, padx=(15,0), pady=(20,0))
    
    entry_rut_director_anual = ttk.Entry(ventana_registro, width=30)
    entry_rut_director_anual.grid(row=9, column=0, padx=(15,0), pady=(0,10))
    
    
    label_fechainicio_anual = ttk.Label(ventana_registro, text="Fecha Inicio", font=("Arial", 10, "bold"))
    label_fechainicio_anual.grid(row=8, column=1, padx=(80,0), pady=(20,0))
    
    entry_fechainicio_anual = ttk.Entry(ventana_registro, width=30)
    entry_fechainicio_anual.grid(row=9, column=1, padx=(80,0), pady=(0,10))
    
    label_fechatermino_anual = ttk.Label(ventana_registro, text="Fecha Termino", font=("Arial", 10, "bold"))
    label_fechatermino_anual.grid(row=10, column=0, padx=(15,0), pady=(20,0))
    
    entry_fechatermino_anual = ttk.Entry(ventana_registro, width=30)
    entry_fechatermino_anual.grid(row=11, column=0, padx=(15,0), pady=(0,10))
    
    
    label_fechacontrato_anual = ttk.Label(ventana_registro, text="Fecha Contrato", font=("Arial", 10, "bold"))
    label_fechacontrato_anual.grid(row=10, column=1, padx=(80,0), pady=(20,0))
    
    entry_fechacontrato_anual = ttk.Entry(ventana_registro, width=30)
    entry_fechacontrato_anual.grid(row=11, column=1, padx=(80,0), pady=(0,10))
    
    
    
    
    btn_registro_anual = ttk.Button(ventana_registro, text="Registrar Prestamo", command=print_mock, width=27)
    btn_registro_anual.grid(row=14, column=1, padx=(83, 0), pady=(10, 10))
   
    


# ### 1er Registro - Registrar Prestamo Eventual
# Btn para Registro 1
btn_registro1 = ttk.Button(tab3, text="Registrar Prestamo Eventual", command=ventana_registro_eventual, width=50)
btn_registro1.grid(row=2, column=0, padx=10, pady=(30,10))




# ### 2er Registro - Registrar Prestamo Anual
# Btn para Registro 2
btn_registro2 = ttk.Button(tab3, text="Registrar Prestamo Anual", command=ventana_registro_anual, width=50)
btn_registro2.grid(row=4, column=0, padx=10, pady=10)



# ### 3er Registro - Registrar Estudiante
# Btn para Registro 3
btn_registro3 = ttk.Button(tab3, text="Registrar Estudiante", command=ventana_registro_estudiante, width=40)
btn_registro3.grid(row=6, column=0, padx=10, pady=(40,10))



# ### 4er Registro - Registrar Instrumento
# Btn para Registro 4
btn_registro4 = ttk.Button(tab3, text="Registrar Instrumento", command=ventana_registro_instrumento, width=40)
btn_registro4.grid(row=8, column=0, padx=10, pady=10)



# ### 5er Registro - Registrar Profesor
# Btn para Registro 5
btn_registro5 = ttk.Button(tab3, text="Registrar Profesor", command=ventana_registro_profesor, width=40)
btn_registro5.grid(row=10, column=0, padx=10, pady=10)

# Centra los elementos de la Tab3 - Registra
tab3.columnconfigure(0, weight=1)
tab3.columnconfigure(0, weight=1)



# ### Ventanas que se abren desde TAB3 REGISTRA





# ### Fin codigo, Las lineas siguientes tienen que estar al final del archivo para que funcione correctamente.

# Inicia y refresca la ventana de la UI.
root.mainloop()

# Cierra la connection y el cursor al salir de la aplicación.

crsr.close()
connection.close()
