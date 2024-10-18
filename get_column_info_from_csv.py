import pandas as pd

def get_column_info():
    print("Executing Function: get_column_info from get_column_info.py")
    df = pd.read_csv("csv/data.csv", nrows=5, header=None, sep=";")

    # Primera fila contiene los nombres de las columnas
    columns = df.iloc[0].tolist()
    print(columns)

    # Segunda fila contiene los tipos de datos
    data_types = df.iloc[1].tolist()
    print(data_types)

    # Extraer las filas de la 2 a la 4
    #examples = df.iloc[2:5].values.tolist()  # Convertir a lista para facilitar el manejo
    #print(examples)

    columns_and_types = list(zip(columns, data_types))
    print(columns_and_types)

    # Imprimir los nombres de las columnas y los tipos de datos
    print("Columnas:", columns_and_types)
    print("--------------------------------\n")

    return columns, data_types, columns_and_types
