#!/usr/bin/python

import tkinter as tk
import userApp as u
import pandas as pd
import os
import sys
import json

input_dir = sys.path.append(os.getcwd())

def list_clients(label, client_frame):
    client_frame.destroy()
    client_frame = tk.Frame(root)
    client_frame.pack()

    client_list = u.client_around()
    json_string = json.dumps(client_list)
    # c = str(type(client_list)) #json.loads(json_string)
    # c = client_list
    # c = ''

    for d in client_list:
        for key in d:
            # c = c + str(key)
            if key == 'name':
                create_client_btn(d[key], client_frame)

    # df = pd.read_json(client_list)
    # for d in df:
    #     c = c + str(d)
    label.config(text=str('List of clients'))
    # label.config(text=str('List of clients - test'))

def create_client_btn(name, client_frame):
    button = tk.Button(client_frame, text=name, width=25)
    button.pack()

def create_menu(client_id):
    menu = u.get_menu(client_id)

    client_frame.pack_forget()
    menu_frame = tk.Frame(root)
    menu_frame.pack(side='bottom')


if __name__ == "__main__":
    # sys.stdout.write("######################")

    root = tk.Tk()
    root.title("Client List")
    root["padx"] = 30
    root["pady"] = 20

    frame = tk.Frame(root)
    frame.pack()

    client_frame = tk.Frame(root)
    client_frame.pack(side='bottom')

    label = tk.Label(frame, text='List of clients', fg="dark green")
    label.pack()

    button = tk.Button(frame, text='List', width=25, command=lambda: list_clients(label, client_frame))
    button.pack()

    button1 = tk.Button(frame, text='Stop', width=25, command=root.destroy)
    button1.pack()



    root.mainloop()