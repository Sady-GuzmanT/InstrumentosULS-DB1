import tkinter as tk
from tkinter import ttk
import psycopg2
from config import config


def execute_query():
    # Retrieve the SQL query from the entry field
    query = query_entry.get()

    # Connect to the PostgreSQL database (replace these values with your database information)
    connection = psycopg2.connect(
        host="10.4.3.195",
        port="5432",
        database="instrumentos",
        user="instrumentos_dev",
        password="5jaLgi6" # PUERTO 5432
    )

    # Create a cursor
    cursor = connection.cursor()

    try:
        # Execute the SQL query
        cursor.execute(query)
        
        # Fetch all the results
        results = cursor.fetchall()

        # Display the results in the treeview widget
        display_results(results)

    except Exception as e:
        # Display any error that occurs during query execution
        result_tree.delete(*result_tree.get_children())  # Clear previous results
        result_tree.insert("", "end", values=("Error", str(e)))

    finally:
        # Close the cursor and connection
        cursor.close()
        connection.close()

def display_results(results):
    # Clear previous results
    result_tree.delete(*result_tree.get_children())

    # Display column names
    columns = [desc[0] for desc in cursor.description]
    result_tree["columns"] = columns
    result_tree.heading("#0", text="Row")
    for col in columns:
        result_tree.heading(col, text=col)
        result_tree.column(col, anchor=tk.CENTER)

    # Display data
    for i, row in enumerate(results, 1):
        result_tree.insert("", "end", iid=i, values=(i,) + tuple(row))

# Create the main window
root = tk.Tk()
root.title("Base de Datos Instrumentos")

# Create an entry for SQL queries
query_entry = ttk.Entry(root, width=50)
query_entry.grid(row=0, column=0, padx=10, pady=10, columnspan=2)

# Create a button to execute the query
execute_button = ttk.Button(root, text="Execute Query", command=execute_query)
execute_button.grid(row=0, column=2, padx=10, pady=10)

# Create a treeview widget to display the results
result_tree = ttk.Treeview(root)
result_tree.grid(row=1, column=0, padx=10, pady=10, columnspan=3)

# Start the Tkinter event loop
root.mainloop()