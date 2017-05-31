import __init__

import core.app.api.clientApp as ca
from core.app.gui.base_GUI import Checkbar, Dropdownbar

import tkinter as tk

class ClientAppGUI():
    def __init__(self):
        self.clientAPP = ca.ClientApp(1)

        self.init_cmd()
        self.init_root()
        self.frames = {}

        self.parts = ['admin', 'created', 'validated', 'pickup']
        for name in self.parts:
            self.init_frame(name)

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

        self.main_frame = tk.Frame(self.root)
        self.main_frame.grid(row=0, column=0)

    def init_frame(self, name):

        frame = tk.Frame(self.root)

        if name == 'admin':
            frame.grid(row=0, column=0, columnspan=3)
        elif name == 'created':
            frame.grid(row=1, column=0)
        elif name == 'validated':
            frame.grid(row=1, column=1)
        elif name == 'pickup':
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
            self.create_admin()
            # button = tk.Button(top, text='Refresh', width=15, command=lambda: self.create_pending_queue(1))
            # button1 = tk.Button(top, text='Validate', width=15, command=lambda: self.validate_orders())
            # button2 = tk.Button(top, text='Reject', width=15, command=lambda: self.reject_orders())

        elif name == 'created':
            label = tk.Label(top, text='List of created orders', fg="dark green")
            button = tk.Button(top, text='Refresh', width=15, command=lambda: self.create_pending_queue(1))
            button1 = tk.Button(top, text='Validate', width=15, command=lambda: self.validate_orders())
            button2 = tk.Button(top, text='Reject', width=15, command=lambda: self.reject_orders())

        elif name == 'validated':
            label = tk.Label(top, text='List of validated orders', fg="dark green")
            button = tk.Button(top, text='Refresh', width=15, command=lambda: self.create_validated_queue(1))
            button1 = tk.Button(top, text='Pick Up Request', width=15, command='1')
            button2 = tk.Button(top, text='Complete', width=15, command='1')

        elif name == 'pickup':
            label = tk.Label(top, text='List of orders pending pick up', fg="dark green")
            button = tk.Button(top, text='Refresh', width=15, command='1')
            button1 = tk.Button(top, text='Pick Up Completed', width=15, command='1')
            button2 = tk.Button(top, text='Replace in Queue', width=15, command='1')

        label.grid(row=0, column=0, columnspan=3)
        if name != 'admin':
            button.grid(row=1, column=0)
            button1.grid(row=1, column=1)
            button2.grid(row=1, column=2)

    def run(self):
        self.root.mainloop()

    #REFRESH BOTTOM FRAMES
    def create_admin(self):
        bottom = self.frames['admin_bottom']
        for wid in bottom.winfo_children():
            wid.destroy()

        clients = [client['id'] for client in self.clientAPP.get_all_clients()]
        self.admin_clients = Dropdownbar(bottom, clients, self.clientAPP.client_id)
        self.admin_clients.grid()

    def create_pending_queue(self, client_id):
        bottom = self.frames['created_bottom']
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

        self.created_orders = Checkbar(bottom, order_ids)
        self.created_orders.grid()

    def create_validated_queue(self, client_id):
        bottom = self.frames['validated_bottom']
        for wid in bottom.winfo_children():
            wid.destroy()

        orders = self.clientAPP.get_validated_orders()
        print('validated orders: ' + str(len(orders)))

        order_ids = []
        for order in orders:
            id = order['id']
            menu_id = order['menu_id']
            user_id = order['user_id']
            order_ids.append('id:' + str(id) + ' - user:' + str(user_id) + ' - menu:' +str(menu_id))

        self.validated_orders = Checkbar(bottom, order_ids)
        self.validated_orders.grid()


    #ACTIONS
    def validate_orders(self):
        print(self.created_orders.state())

        validated_orders = []
        for k,v in self.created_orders.state().items():
            if v > 0:
                validated_orders.append(k)

        orders = self.clientAPP.validate_orders(validated_orders)

    def reject_orders(self):
        print(self.created_orders.state())


if __name__ == "__main__":

    clientGUI = ClientAppGUI()
    clientGUI.run()

