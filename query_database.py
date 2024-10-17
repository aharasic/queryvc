import pandas as pd
import duckdb
import datetime
import json

def execute_sql_query(sql_query, columns, data_types, csv_file):
    print("\n\nExecuting Function: execute_sql_query from query_database.py\n")
    # Leer los datos reales desde la tercera fila (fila 2 en adelante)
    data_df = pd.read_csv(csv_file, header=0, sep=";")

    # Cargar los datos leídos en DuckDB como una tabla temporal
    column_definitions = ", ".join([f"{col} {dtype}" for col, dtype in zip(columns, data_types)])

    #print("\nSQL Query:\n")
    if sql_query.endswith(";"):
        sql_query = sql_query[:-1] 
    #print(sql_query)

    duckdb.execute(f"CREATE OR REPLACE TEMP TABLE temp_table ({column_definitions})")
    duckdb.execute(f"INSERT INTO temp_table (SELECT * FROM data_df)")
    duckdb.execute(f"CREATE OR REPLACE TEMP TABLE temp_query AS ({sql_query})")

    result = duckdb.execute("select * from temp_query").fetchall()
    headers = duckdb.execute("PRAGMA TABLE_INFO('temp_query')").fetchall()
    header = [record[1] for record in headers]
    
    print("\nResults:\n")
    print(header)
    print(result)

    if not result:
        result = "[('Response', 'No Results were found')]"

    # Mapeo para traducir los tipos de datos SQL a tipos nativos de Python
    type_mapping = {
        'INTEGER': int,
        'BIGINT': int,
        'VARCHAR': str,
        'DATE': str,  # Las fechas están en formato 'yyyy-mm-dd'
        'FLOAT': float,
        'DOUBLE': float
    }

    # Convertir el resultado a JSON basado en las columnas obtenidas en el resultado SQL
    print("\nResults JSON:\n")
    data = []
    for row in result:
        data.append({header: value for header, value in zip(header, row)})

    #json_data = json.dumps({
    #    "headers": headers,
    #    "content": data
    #})

    print(data)

    # Imprimir el JSON resultante
    print("\nResultado en formato JSON:\n", data)
    print("--------------------------------\n")

    return data