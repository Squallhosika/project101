import __init__

import core.app.api.clientApp as ca
from core.app.gui.base_GUI import Checkbar, Dropdownbar

import collections
import tkinter as tk
from tkinter import ttk

class ClientAppGUI():
    def __init__(self):
        self.clientAPP = ca.ClientApp(1)
        self.client_id = self.clientAPP.client_id

        self.tabs = {}
        self.frames = {}

        self.init_cmd()
        self.init_root()
        self.init_notebook()


        self.created_orders = []

        self.root.mainloop()

    #INIT FRAMES

    def init_cmd(self):

        txt = ['*****************************************',
               '******                          *********',
               '******      INIT CLIENT APP     *********',
               '******                          *********',
               '*****************************************'
               ]
        print('\n'.join(txt))

    def init_root(self):
        self.root = tk.Tk()

        self.root.title("Client Unicorn App")
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


    def init_panel_control(self, tab_name, panel_name):
        top = self.frames[tab_name + '_' + str(panel_name) + '_control']

        if tab_name == 'Admin':
            label = tk.Label(top, text='Admin', fg="dark green")
            self.create_admin()
            label.grid(row=0, column=0, columnspan=3)

        elif tab_name == 'Orders':
            self.create_order_control(top, panel_name)

        elif tab_name == 'Shifts':
            self.create_shift_control(top, panel_name)


    def create_order_control(self, top, panel_name):
        if panel_name == 'created':
            label = tk.Label(top, text='List of created orders', fg="dark green")
            button = tk.Button(top, text='Refresh', width=15, command=lambda: self.create_pending_queue(self.client_id))
            button1 = tk.Button(top, text='Validate', width=15, command=lambda: self.validate_orders())
            button2 = tk.Button(top, text='Reject', width=15, command=lambda: self.reject_orders())

        elif panel_name == 'validated':
            label = tk.Label(top, text='List of validated orders', fg="dark green")
            button = tk.Button(top, text='Refresh', width=15, command=lambda: self.create_validated_queue(self.client_id))
            button1 = tk.Button(top, text='Pick Up Request', width=15, command=lambda: self.request_pickup_orders())
            button2 = tk.Button(top, text='Complete', width=15, command='1')

        elif panel_name == 'pickup':
            label = tk.Label(top, text='List of orders pending pick up', fg="dark green")
            button = tk.Button(top, text='Refresh', width=15, command=lambda: self.create_pickup_queue(self.client_id))
            button1 = tk.Button(top, text='Pick Up Completed', width=15, command='1')
            button2 = tk.Button(top, text='Replace in Queue', width=15, command='1')

        if label.winfo_exists(): label.grid(row=0, column=0, columnspan=3)
        if button.winfo_exists(): button.grid(row=1, column=0)
        if button1.winfo_exists(): button1.grid(row=1, column=1)
        if button2.winfo_exists(): button2.grid(row=1, column=2)

    def create_shift_control(self, top, panel_name):
        if panel_name == 'employees':
            label = tk.Label(top, text='List of employees', fg="dark green")
            button = tk.Button(top, text='Refresh', width=15, command=lambda: self.create_pending_queue(self.client_id))
            button1 = tk.Button(top, text='Add tp shift', width=15, command=lambda: self.validate_orders())
            button2 = tk.Button(top, text='Delete', width=15, command=lambda: self.reject_orders())

        elif panel_name == 'active':
            label = tk.Label(top, text='Active shift employees', fg="dark green")
            button = tk.Button(top, text='Refresh', width=15, command=lambda: self.create_validated_queue(self.client_id))
            button1 = tk.Button(top, text='Remove Employee', width=15, command=lambda: self.request_pickup_orders())
            button2 = tk.Button(top, text='Unactivate Shift', width=15, command='1')

        elif panel_name == 'shifts':
            label = tk.Label(top, text='List of available shifts', fg="dark green")
            button = tk.Button(top, text='Refresh', width=15, command=lambda: self.create_pickup_queue(self.client_id))
            button1 = tk.Button(top, text='Activate shift', width=15, command='1')
            button2 = tk.Button(top, text='Remove Shift', width=15, command='1')

        if label.winfo_exists(): label.grid(row=0, column=0, columnspan=3)
        if button.winfo_exists(): button.grid(row=1, column=0)
        if button1.winfo_exists(): button1.grid(row=1, column=1)
        if button2.winfo_exists(): button2.grid(row=1, column=2)




    def run(self):
        self.root.mainloop()

    #FUNCTIONS
    def get_tabs(self):
        tab_dic = collections.OrderedDict()
        # tab_list = ['Orders', 'Shifts', 'Menus', 'Admin']
        tab_list = ['Orders', 'Shifts', 'Admin']

        for t in tab_list:
            if t == 'Orders':
                panels = ['created', 'validated', 'pickup']
            elif t == 'Admin':
                panels = ['client']
            elif t == 'Shifts':
                panels = ['employees', 'active', 'shifts']
            elif t == 'Menus':
                panels = ['items', 'active', 'menus']

            # tab = {}
            # for idx,panel in enumerate(panels):
            #     tab[idx] = panel
            #
            # tab_dic[t] = tab
            tab_dic[t] = panels

        return tab_dic



    #REFRESH BOTTOM FRAMES
    def create_admin(self):
        bottom = self.frames['Admin_client_bottom']
        for wid in bottom.winfo_children():
            wid.destroy()

        clients = [client['id'] for client in self.clientAPP.get_all_clients()]
        self.admin_clients = Dropdownbar(bottom, clients, self.clientAPP.client_id)
        self.admin_clients.grid()

    #ORDERS
    def create_pending_queue(self, client_id):
        bottom = self.frames['Orders_created_bottom']
        for wid in bottom.winfo_children():
            wid.destroy()

        orders = self.clientAPP.get_pending_orders()
        print('pending orders: ' + str(len(orders)))

        order_ids = []
        for order in orders:
            id = order['id']
            menu_id = order['menu_id']
            user_id = order['user_id']
            order_ids.append('order: ' + str(id) + ' - user: ' + str(user_id) + ' - menu: ' +str(menu_id))

        self.created_orders = Checkbar(bottom, order_ids,'id')
        self.created_orders.grid()

    def create_validated_queue(self, client_id):
        bottom = self.frames['Orders_validated_bottom']
        for wid in bottom.winfo_children():
            wid.destroy()

        orders = self.clientAPP.get_validated_orders()
        print('validated orders: ' + str(len(orders)))

        order_ids = []
        for order in orders:
            id = order['id']
            menu_id = order['menu_id']
            user_id = order['user_id']
            order_ids.append('order:' + str(id) + ' - user:' + str(user_id) + ' - menu:' +str(menu_id))

        self.validated_orders = Checkbar(bottom, order_ids,'id')
        self.validated_orders.grid()

    def create_pickup_queue(self, client_id):
        bottom = self.frames['Orders_pickup_bottom']
        for wid in bottom.winfo_children():
            wid.destroy()

        orders = self.clientAPP.get_pickup_orders()
        print('pickup orders: ' + str(len(orders)))

        order_ids = []
        for order in orders:
            id = order['id']
            menu_id = order['menu_id']
            user_id = order['user_id']
            order_ids.append('order:' + str(id) + ' - user:' + str(user_id) + ' - menu:' +str(menu_id))

        self.pickup_orders = Checkbar(bottom, order_ids,'id')
        self.pickup_orders.grid()

    #SHIFTS
    def create_employees_list(self, client_id):
        bottom = self.frames['Shifts_employees_bottom']
        for wid in bottom.winfo_children():
            wid.destroy()

        employees = self.clientAPP.get_pending_orders()
        print('available employees: ' + str(len(employees)))

        order_ids = []
        for order in orders:
            id = order['id']
            menu_id = order['menu_id']
            user_id = order['user_id']
            order_ids.append('order: ' + str(id) + ' - user: ' + str(user_id) + ' - menu: ' +str(menu_id))

        self.created_orders = Checkbar(bottom, order_ids,'id')
        self.created_orders.grid()








    #ACTIONS
    def validate_orders(self):
        print(self.created_orders.state())

        validated_orders = []
        for k,v in self.created_orders.state().items():
            if v > 0:
                validated_orders.append(k)

        orders = self.clientAPP.validate_orders(validated_orders)

        self.create_pending_queue(self.client_id)
        self.create_validated_queue(self.client_id)

    def reject_orders(self):
        print(self.created_orders.state())

        rejected_orders = []
        for k,v in self.created_orders.state().items():
            if v > 0:
                rejected_orders.append(k)

        orders = self.clientAPP.validate_orders(rejected_orders)

    def request_pickup_orders(self):
        print(self.validated_orders.state())

        pickedup_orders = []
        for k,v in self.validated_orders.state().items():
            if v > 0:
                pickedup_orders.append(k)

        orders = self.clientAPP.pickup_orders(pickedup_orders)

        # self.create_pending_queue(self.client_id)
        self.create_validated_queue(self.client_id)
        self.create_pickup_queue(self.client_id)

if __name__ == "__main__":

    clientGUI = ClientAppGUI()
    clientGUI.run()

