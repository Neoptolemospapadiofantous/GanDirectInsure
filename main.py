from utils.database_connection import DatabaseConnection

# Example usage of the DatabaseConnection singleton
# Replace the placeholders with your actual database credentials
host = 'your_host'
user = 'your_user'
password = 'your_password'
database = 'your_database_name'

# Initialize the database connection
db_instance = DatabaseConnection(host, user, password, database)
cursor = db_instance.cursor

# Here you can perform operations with the cursor.
# When done, close the connection.
# db_instance.close()
