#!/usr/bin/python
import __init__

import core.app.api.userApp as ua
from core.app.gui.base_GUI import Inputbar, Checkbar

import collections
import tkinter as tk
from tkinter import ttk

import os
import sys
import json

input_dir = sys.path.append(os.getcwd())



class UserAppGUI():
    def __init__(self):
        self.tabs = {}
        self.frames = {}

        self.init_APP()
        self.init_cmd()
        self.init_root()
        self.init_notebook()

        self.root.mainloop()

        # self.init_root()
        #
        # self.parts = ['client', 'menu', 'order']
        # for name in self.parts:
        #     self.init_frame(name)

    def init_APP(self):
        self.userAPP = ua.UserApp(1)
        self.userAPP.latitude = float(51.521219) #51.521219 -0.0777986
        self.userAPP.longitude = float(-0.0777986)
        self.userAPP.radius = float(5/10)

    def init_cmd(self):

        txt = ['*****************************************',
               '******                          *********',
               '******      INIT USER APP       *********',
               '******                          *********',
               '*****************************************'
               ]
        print('\n'.join(txt))

    def init_root(self):
        self.root = tk.Tk()

        self.root.title("User Unicorn App")
        self.root["padx"] = 60
        self.root["pady"] = 40

    def init_notebook(self):
        self.note = ttk.Notebook(self.root)
        tab_dic = self.get_tabs()

        for k,v in tab_dic.items():
            tab = ttk.Frame(self.note)
            self.tabs[str(k)] = tab

            self.note.add(tab, text=k)
            self.init_tab(k)

        self.note.grid()


    def init_tab(self, tab_name):
        tab_dic = self.get_tabs()
        panel_list = tab_dic[tab_name]

        for idx,panel_name in enumerate(panel_list):
            self.init_panel(tab_name, panel_name, idx)

    def init_panel(self, tab_name, panel_name, position):
        tab =  self.tabs[tab_name]

        frame = tk.Frame(tab)
        frame.grid(row=1, column=position)

        #STYLE OF FRAME
        frame["bd"] = 2
        frame["relief"] = tk.GROOVE
        frame["padx"] = self.root["padx"] / 3
        frame["pady"] = self.root["pady"]

        #INITIATING SUB FRAMES
        top=tk.Frame(frame)
        bottom =tk.Frame(frame)

        top.grid(row=0)
        bottom.grid(row=1)

        self.frames[tab_name + '_' + str(panel_name)] = frame
        self.frames[tab_name + '_' + str(panel_name) + '_control'] = top
        self.frames[tab_name + '_' + str(panel_name) + '_bottom'] = bottom

        self.init_panel_control(tab_name, panel_name)


    #PANEL CONTROLS
    def init_panel_control(self, tab_name, panel_name):
        top = self.frames[tab_name + '_' + str(panel_name) + '_control']

        if tab_name == 'Admin':
            self.create_admin_control(top, panel_name)

        elif tab_name == 'Orders':
            self.create_order_control(top, panel_name)

    def create_admin_control(self, top, panel_name):

        panel_elements = {}

        if panel_name == 'main':
            el = tk.Label(top, text='Main', fg="dark green")
            panel_elements['order_' + panel_name + '_lbl'] = {'element':el, 'position': {'row':0, 'column':0, 'columnspan':3}}

            # self.admin_client = Inputbar(top, elements=elements)
            # self.admin_client.grid()

        for name, element in panel_elements.items():
            el = element['element']
            pos = element['position']
            if el.winfo_exists(): el.grid(**pos)

    def create_order_control(self, top, panel_name):

        panel_elements = {}

        if panel_name == 'clients':
            el = tk.Label(top, text='List of clients around you', fg="dark green")
            panel_elements['order_' + panel_name + '_lbl'] = {'element':el, 'position': {'row':0, 'column':0, 'columnspan':3}}

            el = tk.Button(top, text='Get clients around', command=lambda: self.create_client_list())
            panel_elements['order_' + panel_name + '_btn1'] = {'element':el, 'position': {'row':1, 'column':0}}

        elif panel_name == 'menu':
            el = tk.Label(top, text='List of items in menu', fg="dark green")
            panel_elements['order_' + panel_name + '_lbl'] = {'element':el, 'position': {'row':0, 'column':0, 'columnspan':3}}

            el = tk.Button(top, text='Place order', command=lambda: self.place_order())
            panel_elements['order_' + panel_name + '_btn1'] = {'element':el, 'position': {'row':1, 'column':0}}

        elif panel_name == 'orders':
            el = tk.Label(top, text='List of your orders', fg="dark green")
            panel_elements['order_' + panel_name + '_lbl'] = {'element':el, 'position': {'row':0, 'column':0, 'columnspan':3}}

            el = tk.Button(top, text='Refresh', command=lambda: self.create_order_list())
            panel_elements['order_' + panel_name + '_btn1'] = {'element':el, 'position': {'row':1, 'column':0}}


        for name, element in panel_elements.items():
            el = element['element']
            pos = element['position']
            if el.winfo_exists(): el.grid(**pos)


    #REFRESH BOTTOM FRAMES

    #ORDERS TAB
    def create_client_list(self):
        bottom = self.frames['Orders_clients_bottom']
        for wid in bottom.winfo_children():
            wid.destroy()

        client_list = self.userAPP.client_around()
        print('clients around: ' + str(len(client_list)))
        for client in client_list['features']:
            name = client['properties']['name']
            id = client['id']

            self.create_client_btn(bottom, name, id)

    def create_menu_list(self, client_id):
        bottom = self.frames['Orders_menu_bottom']
        for wid in bottom.winfo_children():
            wid.destroy()

        menu = self.userAPP.get_menu(client_id)

        elements = {}

        for item in menu:
            element = {}
            item_id = item['item_id']
            item_price = item['price']
            menu_id = item['menu_id']

            element['name'] = str(menu_id) + '_' + str(item_id)
            element['title'] = 'Menu: ' + str(menu_id) + ' of client: ' + str(client_id)
            element['label_params'] = {'text':"item " + str(item_id) + ' @ £' + str(item_price), 'name':str(item_id), 'fg':"black"}
            element['params'] = {'id':item_id, 'item_id': item_id, 'item_price': item_price, 'menu_id':menu_id,'client_id':client_id, 'qty':0}

            elements[str(menu_id) + '_' + str(item_id)] = element

        self.selected_menu = Inputbar(bottom, elements=elements)
        self.selected_menu.grid()
        print('menu selected: ' + str(menu_id))

    def create_order_list(self):
        bottom = self.frames['Orders_orders_bottom']
        for wid in bottom.winfo_children():
            wid.destroy()

        orders = self.userAPP.client_pending_orders()
        print('pending orders: ' + str(len(orders)))

        order_ids = []
        for order in orders:
            id = order['id']
            menu_id = order['menu_id']
            user_id = order['user_id']
            order_ids.append('order: ' + str(id) + ' - user: ' + str(user_id) + ' - menu: ' +str(menu_id))

            # self.create_order_lbl(bottom, client_id, id)

        self.created_orders = Checkbar(bottom, order_ids,'id')
        self.created_orders.grid()



    #FUNCTIONS
    def get_tabs(self):
        tab_dic = collections.OrderedDict()
        tab_list = ['Orders', 'Admin']

        for t in tab_list:
            if t == 'Orders':
                panels = ['clients', 'menu', 'orders']
            elif t == 'Admin':
                panels = ['main']

            tab_dic[t] = panels

        return tab_dic


    #RUN GUI
    def run(self):
        self.init_cmd()
        self.root.mainloop()

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
        button = tk.Button(frame, text=name, width=20,  command=lambda: self.create_menu_list(id))
        button.grid()


    def create_order_lbl(self, frame, client_id, order_id):
        label = tk.Label(frame, text='Order: ' + str(order_id) + '- Client: ' + str(client_id),fg="black")
        label.grid()


    #ACTIONS
    def place_order(self):
        items = self.selected_menu.state()

        order = {}
        nb_items = 0
        for item_id, item in items.items():
            # item = {}
            qty = 0 if item['value'] == '' else int(item['value'])
            price = item['params']['item_price']
            client_id = item['params']['client_id']
            menu_id = item['params']['menu_id']
            order[item_id] = {'item_id':item_id, 'client_id':client_id, 'menu_id':menu_id, 'price':price, 'qty':qty}

            nb_items = nb_items + qty

        if nb_items > 0:
            order_id = self.userAPP.create_order(order)
            print('order created: ' + str(order_id))
        print(order)


if __name__ == "__main__":

    userGUI = UserAppGUI()
    userGUI.create_client_list()
    userGUI.run()