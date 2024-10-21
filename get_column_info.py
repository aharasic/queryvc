def get_column_info():
    print("Executing Function: get_column_info (hardcoded values)")

    # Hardcoded column names
    columns = ['StartupName', 'Industries', 'HeadquartersLocation', 'Description', 
               'LastFundingDate', 'LastFundingAmount', 'NumberofFundingRounds', 
               'LastFundingType', 'StartupCountry', 'GeographyRegion', 'Top5Investors']

    # Hardcoded data types
    data_types = ['VARCHAR', 'VARCHAR', 'VARCHAR', 'TEXT', 
                  'DATE', 'DECIMAL', 'INTEGER', 
                  'VARCHAR', 'VARCHAR', 'VARCHAR', 'TEXT']

    # Combine columns and data types
    columns_and_types = list(zip(columns, data_types))

    # Print the hardcoded columns and data types
    print("Columnas:", columns_and_types)
    print("--------------------------------\n")

    return columns, data_types, columns_and_types
