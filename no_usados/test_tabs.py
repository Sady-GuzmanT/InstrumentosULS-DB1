import tkinter as tk
from ttkbootstrap import Style, Notebook
import ttkbootstrap as ttk
from tkinter import messagebox



    
# Create a root window
root = tk.Tk()
root.title("Code in Notebook")

# Create a ttkbootstrap style
style = Style(theme="yeti")  # You can choose a different theme

# Create a ttkbootstrap notebook
notebook = Notebook(root, style="primary.TNotebook")
notebook.pack(fill="both", expand=True)

# Create tabs in the notebook
tab1 = tk.Frame(notebook)
tab2 = tk.Frame(notebook)

# Add tabs to the notebook
notebook.add(tab1, text="Tab 1")
notebook.add(tab2, text="Tab 2")

# Your existing code (replace this with your actual code)
def hola():
    print("hola")


# TAB 1

# ### 2da consulta - VER PRESTAMOS
# Label para combobox 2
label_combobox2 = ttk.Label(tab1, text="Ver Prestamos", font=("Arial", 9, "bold"))
label_combobox2.grid(row=3, column=0, padx=10, pady=10)

# Combobox2
combobox_query_values2 = ["Eventual", "Anual"]
combobox_query2 = ttk.Combobox(tab1, values=combobox_query_values2)
combobox_query2.grid(row=4, column=0, padx=10, pady=10)

# Btn 'Execute Combobox Query' 2
execute_combobox_button2 = ttk.Button(tab1, text="Hacer Consulta", command=hola)
execute_combobox_button2.grid(row=4, column=1, padx=10, pady=10)


# TAB 2

# ### 2da consulta - VER PRESTAMOS --> COPIA 
# Label para combobox 2
label_combobox2 = ttk.Label(tab2, text="Ver Prestamos copia", font=("Arial", 9, "bold"))
label_combobox2.grid(row=3, column=0, padx=10, pady=10)

# Combobox2
combobox_query_values2 = ["Eventual", "Anual"]
combobox_query2 = ttk.Combobox(tab2, values=combobox_query_values2)
combobox_query2.grid(row=4, column=0, padx=10, pady=10)

# Btn 'Execute Combobox Query' 2
execute_combobox_button2 = ttk.Button(tab2, text="Hacer Consulta", command=hola)
execute_combobox_button2.grid(row=4, column=1, padx=10, pady=10)

# Run the Tkinter event loop
root.mainloop()