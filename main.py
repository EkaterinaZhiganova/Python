from typing import List
from fastapi import FastAPI
from pydantic import BaseModel

from database import DataBase

class Act (BaseModel):
    id: int = None
    name: str
    surname: str
    account: int

app = FastAPI()

db = DataBase ()
app.curr_id = 1
app.actions : List [Act] = []

@app.get ("/")
def root():
    return "Hello and welcome to Ekaterinas Python assignment"

@app.get ("/get_action")
def get_action():
    get_action_query = """
    SELECT * FROM action
    """
    data = db.call_database(get_action_query)
    actions = []
    for element in data:
        id, name, surname, account = element
        actions.append(Act(id=id, name=name, surname=surname, account=account))
    return actions

@app.get ("/get_action/{id}")
def get_action (id: int):
    get_action_query = """
    SELECT * FROM action WHERE id = ?
    """
    data = db.call_database(get_action_query, id)
    actions = []
    for element in data:
        id, name, surname, account = element
        actions.append(Act(id=id, name=name, surname=surname, account=account))
    return actions

@app.post ("/add_action")
def add_action (action : Act):
    insert_query = """
    INSERT INTO action (name, surname, account)
    VALUES(?, ?, ?)
    """
    db.call_database(insert_query, action.name, action.surname, action.account)
    return ("Added")

@app.delete ("/delete_action/{id}")
def delete_action (id: int):
    delete_query = """
    DELETE FROM action WHERE id = ?
    """
    db.call_database (delete_query, id)
    return (f"Id {id} deleted")

@app.put ("/update_action/{id}")
def update_action(id: int, new_action: Act):
    update_action_query = """
    UPDATE action
    SET name = ?, surname = ?, account = ?
    WHERE id = ?
    """
    db.call_database(update_action_query, new_action.name, new_action.surname, new_action.account, id)
    return True

