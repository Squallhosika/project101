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
    def __init__(self, parent=None, picks=[], initial_value=None):
        tk.Frame.__init__(self, parent)
        self.picks = picks
        self.selection = initial_value

        var = tk.StringVar()
        if initial_value is not None and initial_value in picks:
            var.set(initial_value)
        option = tk.OptionMenu(parent, var, *picks, command=self.store)
        option.grid()

    def selected(self):
        return self.selection

    def store(self, value):
        self.selection = value

class Inputbar(tk.Frame):
    def __init__(self, parent=None, picks=[], side=tk.LEFT, anchor=tk.N):
        tk.Frame.__init__(self, parent)
        self.vars = []
        self.ct=0
        for pick in picks:
            var = tk.IntVar()
            chk = tk.Checkbutton(self, text=pick, variable=var)
            chk.grid(row=self.ct, sticky=tk.W)
            # chk.pack(side=side, anchor=anchor, expand=tk.YES)
            self.vars.append(var)
            self.ct = self.ct + 1
    def state(self):
        return map((lambda var: var.get()), self.vars)

