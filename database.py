import pyodbc

cnxn = pyodbc.connect(
    "Driver={SQL Server};"
    "Server=MANHAS-GTE-HYD\\SQLEXPRESS;"
    "Database=python;"
    "Trusted_Connection=yes;"
)

cursor = cnxn.cursor()
print(cnxn)
