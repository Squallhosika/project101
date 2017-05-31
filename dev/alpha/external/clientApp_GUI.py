
import tkinter as tk
import clientApp as ca

import pandas as pd
import os
import sys
import json


def validate_next_pending_order(client, listbox):
    client.validate_next_pending_order()
    listbox.delete(0, tk.END)
    for item in client.pending_order_ids():
        listbox.insert(tk.END, item)


def reject_next_pending_order(client, listbox):
    client.reject_next_pending_order()
    listbox.delete(0, tk.END)
    for item in client.pending_order_ids():
        listbox.insert(tk.END, item)


def init_pending_frame(root, client):
    pending_frame = tk.Frame(root)
    pending_frame.grid(row=0, column=0)

    top=tk.Frame(pending_frame)
    bottom =tk.Frame(pending_frame)

    top.grid(row=0)
    bottom.grid(row=1)

    label = tk.Label(top, text='List of pending orders', fg="dark green")
    label.grid(row=0, column=0, columnspan=2)

    listbox = tk.Listbox(bottom)
    listbox.pack()

    for item in client.pending_order_ids():
        listbox.insert(tk.END, item)

    button = tk.Button(top, text='Validate', width=25, command=lambda: validate_next_pending_order(client, listbox))
    button.grid(row=1, column=0)

    button1 = tk.Button(top, text='Reject', width=25, command=lambda: reject_next_pending_order(client, listbox))
    button1.grid(row=1, column=1)

    return bottom

def init_employee_frame(root, client):
    pass


def update_listbox_order_frame(listbox1, listbox2):
    listbox1.delete(0, tk.END)
    for item in client.beingserve_order_ids():
        listbox1.insert(tk.END, item)
    listbox2.delete(0, tk.END)
    for item in client.inqueue_order_ids():
        listbox2.insert(tk.END, item)


def pick_up_request(client, listbox1, listbox2):
    # TODO here we are suposing one employee !!
    client.attribute_next_order(1)
    update_listbox_order_frame(listbox1, listbox2)


def complete(client, listbox1, listbox2):
    # TODO here we are suposing one employee !!
    client.complete_order_by_employee_id(1)
    update_listbox_order_frame(listbox1, listbox2)


def init_order_frame(root, client):
    order_frame = tk.Frame(root)
    order_frame.grid(row=0, column=1)

    top=tk.Frame(order_frame)
    bottom =tk.Frame(order_frame)

    top.grid(row=0)
    bottom.grid(row=1)

    label = tk.Label(top, text='List of orders', fg="dark green")
    label.grid(row=0, column=0, columnspan=2)

    listbox = tk.Listbox(bottom)
    listbox.pack()

    for item in client.beingserve_order_ids():
        listbox.insert(tk.END, item)

    listbox2 = tk.Listbox(bottom)
    listbox2.pack()

    for item in client.inqueue_order_ids():
        listbox2.insert(tk.END, item)

    button = tk.Button(top, text='Pick Up Request', width=25,
                       command=lambda: pick_up_request(client, listbox, listbox2))
    button.grid(row=1, column=0)

    button1 = tk.Button(top, text='Complete', width=25, command=lambda: complete(client, listbox, listbox2))
    button1.grid(row=1, column=1)

    return bottom


if __name__ == "__main__":
    client = ca.ClientApp(1)

    root = tk.Tk()
    root.title("Client Unicorn App")
    root["padx"] = 60
    root["pady"] = 40

    main_frame = tk.Frame(root)
    main_frame.grid(row=0, column=0)

    pending_bottom = init_pending_frame(root, client)

    order_bottom = init_order_frame(root, client)

    employee_bottom = init_employee_frame(root, client)

    root.mainloop()
