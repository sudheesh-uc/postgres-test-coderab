import psycopg2
import csv

# Database connection parameters
db_params = {
    'dbname':   'search',
    'user':     'codaxtr_user',
    'password': 'c0d@xtr',
    'host':     '192.168.43.221',
    'port':     '5435'  # Default PostgreSQL port is 5432
}

# Connect to the PostgreSQL database
try:
    connection = psycopg2.connect(**db_params)
    cursor = connection.cursor()

    # Execute a query to retrieve data
    cursor.execute("SELECT * FROM index_server_map")
    rows = cursor.fetchone()

    # Specify the CSV file name
    csv_file = 'output.csv'

    # Write data to CSV file
    with open(csv_file, mode='w', newline='') as file:
        writer = csv.writer(file)

        # Write the header (optional)
        column_names = [desc[0] for desc in cursor.description]
        writer.writerow(column_names)

        if rows:
            # Write the data
            writer.writerows(rows)

    print(f"Data has been written to {csv_file}")

except (Exception, psycopg2.DatabaseError) as error:
    print(f"Error: {error}")
finally:
    # Close the cursor and connection
    if cursor:
        cursor.close()
    if connection:
        connection.close()
