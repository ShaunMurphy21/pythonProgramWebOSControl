from pywebostv.discovery import *   
from pywebostv.connection import *
from pywebostv.controls import *
import ast

def your_custom_storage_is_empty():
    with open("store.txt", "r") as f:
        if len(f.readlines()) < 1:
            return True
def load_from_your_custom_storage():
    with open("store.txt", "r") as f:
        data = f.read()

    try:
        my_dict = ast.literal_eval(data)
    except SyntaxError:
        print("Error: Invalid dictionary format in file")
        my_dict = {}

    print(my_dict)
    return my_dict
def persist_to_your_custom_storage(store):
    with open("store.txt", "w") as f:
        print(store, file=f)
def initiate_remote():

    if your_custom_storage_is_empty():
        store = {}
    else:
        store = load_from_your_custom_storage()

    client = WebOSClient("192.168.1.137", secure=True)
    client.connect()
    for status in client.register(store):
        if status == WebOSClient.PROMPTED:
            print("Accept Prompt on TV!")
        elif status == WebOSClient.REGISTERED:
            print("Registration with TV sucessful")
    print(store) 

    persist_to_your_custom_storage(store)
    return client
