import duckdb
import json

# Ejecuta una consulta sobre la relación cargada
duckdb.execute("""
    CREATE OR REPLACE TEMP TABLE temp_table (StartupName VARCHAR, Industries VARCHAR, HeadquartersLocation VARCHAR, Description VARCHAR, LastFundingDate DATE, LastFundingAmount INTEGER, NumberofFundingRounds INTEGER, LastFundingType VARCHAR, IPOStatus VARCHAR, Top5Investors VARCHAR)
""").fetchall()

duckdb.execute("""
INSERT INTO temp_table (SELECT * FROM read_csv_auto('chile.csv'))
""").fetchall()

result = duckdb.query("""
SELECT COUNT(StartupName::VARCHAR) FROM temp_table WHERE LastFundingAmount > 10000 AND DATE_PART('YEAR', TRY_CAST(LastFundingDate AS DATE)) = 2024
""").fetchall()

# Imprimir el resultado en formato JSON
print(result)

# Imprimir el resultado en formato JSON
#print(json.dumps(result, indent=4))
