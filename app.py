import os
import requests
from typing import List
from main import Act

def url (route: str):
    return f"http://127.0.0.1:8000{route}"

def menu():
    print("""
          1 - Add a customer
          2 - Get customer(s) info
          3 - Update customer info
          4 - Delete a customer
          5 - Exit
          """)
    pass

def add_action():
    print ("Add a customer")
    name = input ("Customer name: ")
    if not name != "" or str.isdigit(name):
        print ("Wrong format (use letters):")
        return
    surname = input ("Customer surname: ")
    if not surname != "" or str.isdigit(surname):
        print ("Wrong format (use letters):")
        return
    account = input ("Account number: ")
    if not str.isdigit(account):
        if not account != "":
            print ("Wrong account format (use numbers)")           
            return
    new_action = Act(name = name, surname = surname, account=account)
    res = requests.post(url("/add_action"), json = new_action.dict())
    print(res)
    
def get_action():
    actions = []
    print ("Get a customer")
    id = input_id("get a customer or leave it blank to get all")
    res = requests.get(url(f"/get_action{id}"))
    if not res.status_code == 200:
        return
    data = res.json()

    for action in data:
        action = Act(**action)
        print (f"ID: {action.id}")
        print (f"Name : {action.name}")
        print (f"Surname : {action.surname}")
        print (f"Account number : {action.account}")
        actions.append(action)
    return actions

def update_action():
    id = input_id ("update a customer")
    if id == "/":
        return
    
    res = requests.get(url(f"/get_action{id}"))
    data = res.json()
    if res.json() == []:
        print (f"Customer id {id} not found")
        return

    name = input("New name: ")
    if str.isdigit(name):
        print ("Wrong format (use letters):")
        return
    surname = input("New surname: ")
    if str.isdigit(surname):
        print ("Wrong format (use letters):")
        return
    account = input("New account number: ")
    if not str.isdigit(account):
        if account != "":
            print ("Wrong account format (use numbers)")           
            return
    for action in data:
        action = Act(**action) 
     
    if not name:
        name = action.name
    if not surname:
        surname = action.surname
    if not account:
        account = action.account

    new_action = Act(name=name, surname=surname, account=account)
    res = requests.put(url(f"/update_action{id}"), json=new_action.dict())
    print(res.json())

def delete_action ():
    id = input_id ("delete a customer")
    if id == "/":
        return
    
    res = requests.delete (url(f"/delete_action{id}"))
    print(res.json())

def input_id(action_type):
    flag = True
    while flag:
        id = input(f"Type an id to {action_type}: ")
        if str.isdigit (id):
            flag = False
        elif not id:
            flag = False
        else:
            print ("Error id, please try again: ")
    return (f"/{id}")
        
def main():
    menu()
    choice = input ("Please choose your action: ")
    choice = choice.strip()
    if not str.isdigit (choice):
        print ("Wrong action, please try again: ")
        return
    
    match int(choice):
        case 1:
            add_action()
        case 2:
            get_action()
        case 3:
            update_action()
        case 4:
            delete_action()
        case 5:
            exit()
        case _:
            print ("Please enter a valid action")
                       
    pass

while __name__ == "__main__":
    main()