#import sqlite3
#from fastapi import FastAPI
import json
from database import DataBase

#app = FastAPI()

db = DataBase()

# def populate_database():
#     connection = sqlite3.connect("customer.db")
#     cur = connection.cursor
#     cur.execute (
#     "CREATE TABLE  action (id INTEGER PRIMARY KEY IDENTITY(1,1) NOT NULL, name VARCHAR (255) NOT NULL, surname VARCHAR (255) NOT NULL, account INT NOT NULL"
#     )
#     cur.execute("INSERT INTO action (name, surname, account) VALUES ('Ada', 'Olafsson', 19)")
#     cur.close()
#     connection.commit()
#     connection.close()
#     pass

# @app.get("/")
# def root():
#     return "Hello all"

# @app.get("/customers")
# def root():
#     populate_database()
#     return "Database is populated"

create_customer = """
    INSERT INTO action (name, surname, account)
    VALUES(?, ?, ?);
"""

with open("seed.json", "r") as seed:
    data = json.load(seed)

    for customer in data["customers"]:
        db.call_database(create_customer, customer["name"], customer["surname"], customer["account"])
