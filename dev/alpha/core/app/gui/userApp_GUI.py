#!/usr/bin/python
import __init__

import core.app.api.userApp as ua

import tkinter as tk
import os
import sys
import json

input_dir = sys.path.append(os.getcwd())



class UserAppGUI():
    def __init__(self):
        self.userAPP = ua.UserApp(1)

        self.init_root()
        self.frames = {}

        self.parts = ['client', 'menu', 'order']
        for name in self.parts:
            self.init_frame(name)


    def init_root(self):
        self.root = tk.Tk()

        self.root.title("User Unicorn App")
        self.root["padx"] = 60
        self.root["pady"] = 40

        self.main_frame = tk.Frame(self.root)
        self.main_frame.grid(row=0, column=0)

    def init_frame(self, name):

        frame = tk.Frame(self.root)

        if name == 'admin':
            frame.grid(row=0, column=0, columnspan=3)
        elif name == 'client':
            frame.grid(row=1, column=0)
        elif name == 'menu':
            frame.grid(row=1, column=1)
        elif name == 'order':
            frame.grid(row=1, column=2)

        #STYLE OF FRAME
        frame["bd"] = 2
        frame["relief"] = tk.GROOVE
        frame["padx"] = self.root["padx"] / len(self.parts)
        frame["pady"] = self.root["pady"]


        #INITIATING SUB FRAMES
        top=tk.Frame(frame)
        bottom =tk.Frame(frame)

        top.grid(row=0)
        bottom.grid(row=1)

        self.frames[str(name)] = frame
        self.frames[str(name) + '_top'] = top
        self.frames[str(name) + '_bottom'] = bottom

        self.init_bottom(name)

    def init_bottom(self,name):
        top = self.frames[str(name) + '_top']

        if name == 'admin':
            label = tk.Label(top, text='Admin', fg="dark green")
            # self.create_admin()
            # button = tk.Button(top, text='Refresh', width=15, command=lambda: self.create_pending_queue(1))
            # button1 = tk.Button(top, text='Validate', width=15, command=lambda: self.validate_orders())
            # button2 = tk.Button(top, text='Reject', width=15, command=lambda: self.reject_orders())

        elif name == 'client':
            label = tk.Label(top, text='List of clients around', fg="dark green")
            button = tk.Button(top, text='Clients Around', width=15, command=lambda: self.create_clients_around())
            # button1 = tk.Button(top, text='Validate', width=15, command=lambda: self.validate_orders())
            # button2 = tk.Button(top, text='Reject', width=15, command=lambda: self.reject_orders())

        elif name == 'menu':
            label = tk.Label(top, text='Menu', fg="dark green")
            button = tk.Button(top, text='Refresh', width=15, command='1')
            button1 = tk.Button(top, text='Order', width=15, command=lambda: self.create_order())
            # button2 = tk.Button(top, text='Co', width=15, command='1')

        elif name == 'order':
            label = tk.Label(top, text='List of orders', fg="dark green")
            button = tk.Button(top, text='Refresh', width=15, command='1')
            button1 = tk.Button(top, text='Confirm Pick Up', width=15, command='1')
            # button2 = tk.Button(top, text='Replace in Queue', width=15, command='1')

        label.grid(row=0, column=0, columnspan=3)
        button.grid(row=1, column=0)
        if name != 'admin' and name != 'client':
            button1.grid(row=1, column=1)
            # button2.grid(row=1, column=2)


    #RUN GUI
    def run(self):
        self.init_cmd()
        self.root.mainloop()

    def init_cmd(self):

        txt = ['*****************************************',
               '******                          *********',
               '******      INIT USER APP       *********',
               '******                          *********',
               '*****************************************'
               ]
        print('\n'.join(txt))


    #REFRESH BOTTOM FRAMES
    def create_clients_around(self):
        bottom = self.frames['client_bottom']
        for wid in bottom.winfo_children():
            wid.destroy()

        client_list = self.userAPP.client_around()
        print('clients around: ' + str(len(client_list)))
        for client in client_list:
            name = client['name']
            id = client['id']

            self.create_client_btn(bottom, name, id)

    def create_menu(self, client_id):
        bottom = self.frames['menu_bottom']
        for wid in bottom.winfo_children():
            wid.destroy()

        menu = self.userAPP.get_menu(client_id)

        for item in menu:
            menu_id = item['menu_id']
            self.create_item(bottom, item, client_id)

        print('menu selected: ' + str(menu_id))

    def create_order(self):
        bottom = self.frames['order_bottom']
        for wid in bottom.winfo_children():
            wid.destroy()

        order_list = self.userAPP.client_pending_orders()

        for order in order_list:
            user_id = order['user_id']
            client_id = order['client_id']
            id = order['id']

            self.create_order_lbl(bottom, client_id, id)

    def create_client_btn(self, frame, name, id):
        button = tk.Button(frame, text=name, width=15,  command=lambda: self.create_menu(id))
        button.grid()

    def create_item(self, frame, item, client_id):
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

    def create_order_lbl(self, frame, client_id, order_id):
        label = tk.Label(frame, text='Order: ' + str(order_id) + '- Client: ' + str(client_id),fg="black")
        label.grid()


    #ACTIONS
    def create_order(self):
        entries = self.get_entries()
        order_id = self.userAPP.create_order(entries)

        print('order created: ' + str(order_id))

    def get_entries(self):
        entries = []
        bottom = self.frames['menu_bottom']
        for wid in bottom.winfo_children():
            if wid.winfo_class() == 'Entry':
                txt = str(wid.get())
                dic = json.loads(txt)

                entries.append(dic)
        return entries



if __name__ == "__main__":

    userGUI = UserAppGUI()
    userGUI.run()