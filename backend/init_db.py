import os
import time
import psycopg2
from psycopg2 import sql

# Load environment variables
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_PORT = os.getenv('DB_PORT', '5432')
DB_USER = os.getenv('DB_USER', 'user')
DB_PASSWORD = os.getenv('DB_PASSWORD', 'password')
DB_NAME = os.getenv('DB_NAME', 'bridgebulks')

def create_tables(cursor):
    create_table_commands = ("""
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        username VARCHAR(50) NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );

    CREATE TABLE IF NOT EXISTS products (
        id SERIAL PRIMARY KEY,
        name VARCHAR(255) NOT NULL,
        price DECIMAL(10, 2) NOT NULL,
        created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
    """
    )

    for command in create_table_commands.split(';
'):
        if command.strip():  # If command is not empty
            cursor.execute(command)

def wait_for_postgresql():
    while True:
        try:
            connection = psycopg2.connect(
                host=DB_HOST,
                port=DB_PORT,
                user=DB_USER,
                password=DB_PASSWORD
            )
            return connection
        except psycopg2.OperationalError:
            print("Waiting for PostgreSQL to be available...")
            time.sleep(5)  # Wait before trying again

if __name__ == '__main__':
    connection = wait_for_postgresql()
    cursor = connection.cursor()
    create_tables(cursor)
    connection.commit()
    cursor.close()
    connection.close()
    print("Database tables created successfully.")