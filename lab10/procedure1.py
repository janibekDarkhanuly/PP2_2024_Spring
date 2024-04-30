import psycopg2

# Connect to your PostgreSQL database
conn = psycopg2.connect(
    dbname="suppliers",
    user="postgres",
    password="12345",
    host="localhost"
)

# Create a cursor object using the connection
cursor = conn.cursor()

try:
    # Call the delete_phonebook_data procedure with delete_by and delete_value parameters
    cursor.callproc("delete_phonebook_data", ["klnlln", "23234"])

    # Commit the transactionx
    conn.commit()
    print("Procedure executed successfully!")
except Exception as e:
    # Rollback the transaction if an error occurs
    conn.rollback()
    print(f"Error executing procedure: {e}")
finally:
    # Close the cursor and connection
    cursor.close()
    conn.close()
