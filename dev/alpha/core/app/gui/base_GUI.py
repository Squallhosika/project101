import tkinter as tk

class Checkbar(tk.Frame):
    def __init__(self, parent=None, picks=[], category='default', side=tk.LEFT, anchor=tk.N):
        tk.Frame.__init__(self, parent)
        self.category = category
        # self.vars = []
        self.vars = {}
        self.ct=0
        for pick in picks:
            var = tk.IntVar()
            chk = tk.Checkbutton(self, text=pick, variable=var)
            chk.grid(row=self.ct, sticky=tk.W)
            # chk.pack(side=side, anchor=anchor, expand=tk.YES)
            # self.vars.append(var)
            self.vars[str(pick)] = var
            self.ct = self.ct + 1

    def state(self):
        if self.category == 'default':
            return {k: v.get() for k, v in self.vars.items()}
        elif self.category == 'id':
            return {(k.split('-')[0]).split(':')[1].strip(): v.get() for k, v in self.vars.items()}

        # return map((lambda var: var.get()), self.vars)

class Dropdownbar(tk.Frame):
    def __init__(self, parent=None, picks=[], initial_value=None, lbl_params=None):
        tk.Frame.__init__(self, parent)
        self.picks = picks
        self.selection = initial_value

        self.label = tk.Label(parent, **lbl_params)

        var = tk.StringVar()
        if initial_value is not None and initial_value in picks:
            var.set(initial_value)
        self.option = tk.OptionMenu(parent, var, *picks, command=self.store)

        self.label.grid(row=0, column=0)
        self.option.grid(row=0, column=1)

        # option.grid()

    def selected(self):
        return self.selection

    def store(self, value):
        self.selection = value

class Inputbar(tk.Frame):
    def __init__(self, parent=None, elements={}):
        tk.Frame.__init__(self, parent)

        self.elements = []
        self.ct=0

        for key, element in elements.items():
            if self.ct == 0:
                label = tk.Label(parent, text=element['title'])
                label.grid()
                self.ct = self.ct + 1

            params = element['params']
            lbl_params = element['label_params']
            name = element['name']

            entry_label = EntryLabel(parent,params, lbl_params)
            entry_label.grid({'row':self.ct})

            self.elements.append(entry_label)
            # self.elements[name] = entry_label #{'var':var, 'frame':frame, 'params': params}
            self.ct = self.ct + 1

    def state(self):
        view = {}
        for elem in self.elements:
            var = elem.var
            params = elem.params
            id = params['id']
            view[id] = {'value':var.get(), 'params':params}
        return view


class EntryLabel(tk.Frame):
    def __init__(self, parent, params, lbl_params):
        tk.Frame.__init__(self, parent)
        self.params = params

        self.frame = tk.Frame(parent)
        self.label = tk.Label(self.frame, **lbl_params)

        self.var = tk.StringVar()
        self.entry = tk.Entry(self.frame, textvariable=self.var)

        self.label.grid(row=0, column=0)
        self.entry.grid(row=0, column=1)



    def grid(self, position={}):
        self.frame.grid(**position)

    def get_params(self):
        return self.params

    def get_value(self):
        return self.var.get()

    def get_frame(self):
        return  self.frame