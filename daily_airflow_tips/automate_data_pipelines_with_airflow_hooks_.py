from airflow.hooks.base_hook import BaseHook
import psycopg2

def fetch_data():
    # Get connection settings using BaseHook
    connection = BaseHook.get_connection('my_postgres_conn_id')
    
    # Connect to the database
    conn = psycopg2.connect(
        host=connection.host,
        database=connection.schema,
        user=connection.login,
        password=connection.password
    )
    cur = conn.cursor()
    cur.execute('SELECT * FROM my_table;')
    rows = cur.fetchall()
    
    for row in rows:
        print(row)

fetch_data()