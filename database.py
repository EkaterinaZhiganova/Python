import pyodbc

db_server = "LAPTOP-SHIBSGPL\SQLEXPRESS"
db_name = "FA"
db_driver = "ODBC Driver 17 for SQL Server"

connection_string = f"""
DRIVER={db_driver};
SERVER={db_server};
DATABASE={db_name};
trusted_connection=yes;
"""

class DataBase:
    
    def call_database(self, query, *args):
        data = None
        conn = pyodbc.connect(connection_string)
        cur = conn.cursor()
        if "SELECT" in query:
            res = cur.execute(query, args)
            data = res.fetchall()
            cur.close()
        else:
            conn.execute(query, args)
        conn.commit()
        conn.close()
        return data

    def init_database(self):
        init_database_query = """
        DROP TABLE IF EXISTS action
        IF NOT EXISTS (SELECT * FROM SYSOBJECTS WHERE name='action' and xtype='U')
        CREATE TABLE  action (
            id INTEGER PRIMARY KEY IDENTITY(1,1) NOT NULL,
            name VARCHAR (255) NOT NULL,
            surname VARCHAR (255) NOT NULL,
            account INT NOT NULL
        );
        """
        insert_query = """
        INSERT INTO action (name, surname, account)
        VALUES 
        ('John','Andersson', 21), 
        ('Ada','Berg', 22),
        ('Kristen', 'Ek', 23),
        ('Markus', 'Maserus', 24);
        """
        conn = pyodbc.connect(connection_string)
        conn.execute(init_database_query)
        conn.execute(insert_query)
        conn.commit()
        conn.close()

if __name__ == "__main__":
    db = DataBase()
    db.init_database()