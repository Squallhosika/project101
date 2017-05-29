
import tkinter as tk
import clientApp as ca

import pandas as pd
import os
import sys
import json


def init_pending_frame(root):
    pending_frame = tk.Frame(root)
    pending_frame.grid(row=0, column=0)

    top=tk.Frame(pending_frame)
    bottom =tk.Frame(pending_frame)

    top.grid(row=0)
    bottom.grid(row=1)

    label = tk.Label(top, text='List of pending orders', fg="dark green")
    label.grid(row=0, column=0, columnspan=2)

    button = tk.Button(top, text='Validate', width=25, command='1')
    button.grid(row=1, column=0)

    button1 = tk.Button(top, text='Reject', width=25, command='1')
    button1.grid(row=1, column=1)

    return bottom

def init_employee_frame(root):
    pass

def init_order_frame(root):
    order_frame = tk.Frame(root)
    order_frame.grid(row=0, column=1)

    top=tk.Frame(order_frame)
    bottom =tk.Frame(order_frame)

    top.grid(row=0)
    bottom.grid(row=1)

    label = tk.Label(top, text='List of orders', fg="dark green")
    label.grid(row=0, column=0, columnspan=2)

    button = tk.Button(top, text='Pick Up Request', width=25, command='1')
    button.grid(row=1, column=0)

    button1 = tk.Button(top, text='Complete', width=25, command='1')
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

    pending_bottom = init_pending_frame(root)

    order_bottom = init_order_frame(root)

    employee_bottom = init_employee_frame(root)

    root.mainloop()
