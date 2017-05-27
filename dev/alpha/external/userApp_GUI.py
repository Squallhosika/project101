#!/usr/bin/python

import tkinter as tk
import userApp as u
import pandas as pd
import os
import sys
import json

input_dir = sys.path.append(os.getcwd())

def list_clients():

    for wid in client_bottom.winfo_children():
        wid.destroy()


    client_list = u.client_around()
    json_string = json.dumps(client_list)
    # c = str(type(client_list)) #json.loads(json_string)
    # c = client_list
    # c = ''

    for client in client_list:
        name = client['name']
        id = client['id']

        create_client_btn(client_bottom, name, id)

    # label.config(text=str('List of clients'))
    # label.config(text=str('List of clients - test'))

def create_client_btn(frame, name, id):
    button = tk.Button(frame, text=name, width=25,  command=lambda: create_menu(id))
    button.grid() #.pack()

def create_item(frame, item, client_id):
    item_id = item['item_id']
    price = item['price']
    id = item['id']

    txt = '{"client_id":' + str(client_id) + ', "item_id":' + str(item_id) + ', "price":' + str(price) + ', "qty":0}'

    # v=tk.IntVar()
    lbl_item = tk.Label(frame, text="item " + str(item_id) + ' @ £' + str(price), name=str(item_id), fg="black")
    # lbl_price = tk.Label(frame, text="price: " + str(price), name=str(item_id) + '_' + str(price), fg="black")
    e = tk.Entry(frame)
    e.insert(tk.END, txt)

    lbl_item.grid(column=0)
    # lbl_price.grid(column=1)
    e.grid(column=2)

    # return v

def get_entries():
    entries = []
    for wid in menu_bottom.winfo_children():
        if wid.winfo_class() == 'Entry':
            txt = str(wid.get())
            dic = json.loads(txt)

            entries.append(dic)
            # item_id = dic["item_id"]
            # price = dic["price"]
            # qty = dic["qty"]
            #
            # entries[item_id] = qty * price
            # for d in a:
            #     b=1

    return entries

def create_menu(client_id):

    for wid in menu_bottom.winfo_children():
        wid.destroy()


    menu = u.get_menu(client_id)

    for item in menu:
        menu_id = item['menu_id']
        create_item(menu_bottom, item, client_id)

    lbl = tk.Label(menu_bottom, text='Menu: ' + str(menu_id), fg="black")
    lbl.grid()


def create_order():
    entries = get_entries()
    u.create_order(entries)

    return c

def init_client_frame(root):
    client_frame = tk.Frame(root)
    client_frame.grid(row=0, column=0)

    top=tk.Frame(client_frame)
    client_bottom =tk.Frame(client_frame)

    top.grid(row=0)
    client_bottom.grid(row=1)

    label = tk.Label(top, text='List of clients', fg="dark green")
    label.grid(row=0, column=0, columnspan=2)

    button = tk.Button(top, text='List', width=25, command=lambda: list_clients())
    button.grid(row=1, column=0)

    button1 = tk.Button(top, text='Stop', width=25, command=root.destroy)
    button1.grid(row=1, column=1)

    return client_bottom

def init_menu_frame(root):
    menu_frame = tk.Frame(root)
    menu_frame.grid(row=0, column=1)

    top=tk.Frame(menu_frame)
    bottom =tk.Frame(menu_frame)

    top.grid(row=0)
    bottom.grid(row=1)

    label = tk.Label(top, text='List of items', fg="dark green")
    label.grid(row=0, column=0, columnspan=2)

    button = tk.Button(top, text='Price', width=25, command='1')
    button.grid(row=1, column=0)

    button1 = tk.Button(top, text='Order', width=25, command=lambda: create_order())
    button1.grid(row=1, column=1)

    return bottom


def init_order_frame(root):
    order_frame = tk.Frame(root)
    order_frame.grid(row=0, column=2)

    top=tk.Frame(order_frame)
    bottom =tk.Frame(order_frame)

    top.grid(row=0)
    bottom.grid(row=1)

    label = tk.Label(top, text='List of orders', fg="dark green")
    label.grid(row=0, column=0, columnspan=2)

    button = tk.Button(top, text='Histo', width=25, command='1')
    button.grid(row=1, column=0)

    button1 = tk.Button(top, text='Refresh', width=25, command='1')
    button1.grid(row=1, column=1)

    return bottom

if __name__ == "__main__":
    # sys.stdout.write("######################")

    root = tk.Tk()
    root.title("Client List")
    root["padx"] = 60
    root["pady"] = 40

    main_frame = tk.Frame(root)
    main_frame.grid(row=0, column=0)

    client_bottom = init_client_frame(root)

    menu_bottom = init_menu_frame(root)

    order_bottom = init_order_frame(root)

    root.mainloop()