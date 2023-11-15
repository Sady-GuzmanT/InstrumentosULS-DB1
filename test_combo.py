import tkinter as tk
from tkinter import ttk

def retrieve_selected_item():
    selected_item = combobox.get()
    result_label.config(text=f"Selected Item: {selected_item}")

# Create the main window
root = tk.Tk()
root.title("ULS 2")

# First layout
# Create a Label above the Combobox
label_above_combobox = ttk.Label(root, text="Ver Instrumentos")
label_above_combobox.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

# Create a Combobox
combobox_values = ["Todos", "Violines", "Cornos"]
combobox = ttk.Combobox(root, values=combobox_values)
combobox.grid(row=1, column=0, padx=10, pady=10)

# Create a Button to retrieve the selected item
retrieve_button = ttk.Button(root, text="Consultar", command=retrieve_selected_item)
retrieve_button.grid(row=1, column=1, padx=10, pady=10)

# Create a Label to display the result
result_label = ttk.Label(root, text="")
result_label.grid(row=2, column=0, columnspan=2, pady=10)

# Second layout (duplicated below the first layout)
# Create a Label above the Combobox
label_above_combobox2 = ttk.Label(root, text="Ver Prestamos")
label_above_combobox2.grid(row=3, column=0, padx=10, pady=10, columnspan=2)

# Create another Combobox
combobox2_values = ["Eventuales", "Anuales"]
combobox2 = ttk.Combobox(root, values=combobox2_values)
combobox2.grid(row=4, column=0, padx=10, pady=10)

# Create another Button to retrieve the selected item
retrieve_button2 = ttk.Button(root, text="Consultar", command=retrieve_selected_item)
retrieve_button2.grid(row=4, column=1, padx=10, pady=10)

# Create another Label to display the result
result_label2 = ttk.Label(root, text="")
result_label2.grid(row=5, column=0, columnspan=2, pady=10)

# Third layout (duplicated below the second layout)
# Create a Label above the Combobox
label_above_combobox3 = ttk.Label(root, text="Ver Disponibles")
label_above_combobox3.grid(row=6, column=0, padx=10, pady=10, columnspan=2)

# Create another Combobox
combobox3_values = ["Todos", "Guitarras", "Violines"]
combobox3 = ttk.Combobox(root, values=combobox3_values)
combobox3.grid(row=7, column=0, padx=10, pady=10)

# Create another Button to retrieve the selected item
retrieve_button3 = ttk.Button(root, text="Consultar", command=retrieve_selected_item)
retrieve_button3.grid(row=7, column=1, padx=10, pady=10)

# Create another Label to display the result
result_label3 = ttk.Label(root, text="")
result_label3.grid(row=8, column=0, columnspan=2, pady=10)

# Start the Tkinter event loop
root.mainloop()
