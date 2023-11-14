import psycopg2

# Replace these values with your PostgreSQL database information
connection = psycopg2.connect(
    host="10.4.3.195",
    database="instrumentos",
    user="instrumentos_dev",
    password="5jaLgi6" # PUERTO 5432
)


# Create a cursor
crsr = connection.cursor()

# Now you can perform database operations using the cursor
print('Version database: ')
crsr.execute('SELECT * FROM estudiante')
db_version =crsr.fetchone()
print(db_version)

# Close the cursor and connection when done
crsr.close()
connection.close()
