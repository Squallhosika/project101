import os
import sys
import collections
sys.path.extend(['C:\\Users\\Keuvin\\Documents\\Unicorn\\GIT\\unicorn_master\\dev\\alpha'])

# from external.userApp import call_function
import external.userApp as u
import pandas as pd


# sys.path.append('C:\\Users\\Keuvin\\DOCUME~1\\Unicorn\\GIT\\UNICOR~1\\dev\\alpha\\')  #os.getcwd())
input_dir = os.path.join(os.getcwd(), 'play', 'input')


def csv_to_dicts(path):
    for _, series in pd.read_csv(path).iterrows():
        yield series.to_dict()


def csv_to_req(path, method_name, service_name, function_name):
    for params in csv_to_dicts(path):
        req = u.call_function(method_name, service_name, function_name, params)
        print(service_name + '.' + function_name + ' ' + str(req.status_code))


def getopts(argv):
    opts = {}  # Empty dictionary to store key-value pairs.
    while argv:  # While there are arguments left to parse...
        if argv[0][0] == '-':  # Found a "-name value" pair.
            opts[argv[0]] = argv[1]  # Add key and value to the dictionary.
        argv = argv[1:]  # Reduce the argument list by copying it starting from index 1.
    return opts

def prepare_dic(service):
    input = {}

    if service == 'all':
        for s in ('client'):
            input[s] = prepare_dic_files(service)

    else:
        input[service] = prepare_dic_files(service)

    return input

def prepare_dic_files(service):
    # input_files = {}
    input_files = collections.OrderedDict()
    if service == 'client':
        # input_files = {
        #     'createclient': 'clients.csv',
        #     'createmenu': 'menus.csv',
        #     'createitem': 'items.csv',
        #     'additemmenu': 'rnn_menu_item.csv',
        # }
        input_files['createclient'] = 'clients.csv'
        input_files['createmenu'] = 'menus.csv'
        input_files['createitem'] = 'items.csv'
        input_files['additemmenu'] = 'rnn_menu_item.csv'
        input_files['addmenuclient'] = 'rnn_client_menu.csv'

    elif service == 'order':
        input_files = {
            'createitem': 'items.csv',
        }

    return input_files

def get_table(fct):
    if fct == 'createclient': table = 'client'
    elif fct == 'createmenu': table = 'menu'
    elif fct == 'createitem': table = 'item'
    elif fct == 'additemmenu': table = 'menuitem'

    return table

def get_table_key(table):
    if table == 'client': fct = 'createclient'
    elif table == 'menu': fct = 'createmenu'
    elif table == 'item': fct = 'createitem'
    elif table == 'menuitem': fct = 'additemmenu'

    return fct


if __name__ == '__main__':
    from sys import argv
    myargs = getopts(argv)

    # input_files = {}
    input_files = collections.OrderedDict()
    if '-s' in myargs:
        service = myargs['-s']
        input_files = prepare_dic_files(service)
        print(service)

        if '-t' in myargs:
            table = myargs['-t']
            print(table)

            fct = get_table_key(table)
            csv_to_req(os.path.join(input_dir, service, input_files[fct]), 'POST', service, fct)

        else:
            for fct in input_files:
                csv_to_req(os.path.join(input_dir, service, input_files[fct]), 'POST', service, fct)


    # Client
    # csv_to_req(os.path.join(input_dir, 'client', 'menus.csv'), 'POST', 'client', 'createmenu')
    # csv_to_req(os.path.join(input_dir, 'client', 'clients.csv'), 'POST', 'client', 'createclient')
    # csv_to_req(os.path.join(input_dir, 'client', 'items.csv'), 'POST', 'client', 'createitem')
    # csv_to_req(os.path.join(input_dir, 'client', 'items.csv'), 'POST', 'client', 'createitem')


