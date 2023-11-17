import pyodbc

conx = pyodbc.connect('DRIVER={SQL Server}; SERVER=DESKTOP-TOA1H2R; Database=AdventureWorks; Trusted_Connection=yes;')
pyodbc.drivers()
conx_string = "driver={SQL Server}; server=DESKTOP-TOA1H2R; database=AdventureWorks; Trusted_Connection=yes;"
query = "SELECT Name, CreditRating FROM Purchasing.Vendor WHERE CreditRating < 3"
conx = pyodbc.connect(conx_string);
cursor = conx.cursor();
cursor.execute(query);
data = cursor.fetchall();
print(data[:5])
conx.close()

