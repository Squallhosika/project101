
import tkinter as tk
import clientApp as ca

import pandas as pd
import os
import sys
import json


if __name__ == "__main__":
    # sys.stdout.write("######################")

    client = ca.ClientApp(1)

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

    listbox = tk.Listbox(root)
    listbox.pack()

    listbox.insert(tk.END, "a list entry")

    for item in ["one", "two", "three", "four"]:
        listbox.insert(tk.END, item)

    root.mainloop()
