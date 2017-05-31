import os
import sys
import collections
sys.path.extend(['C:\\Users\\Keuvin\\Documents\\Unicorn\\GIT\\unicorn_master\\dev\\alpha'])

# from external.userApp import call_function
# import external.userApp as u
import core.app.api.base as u
import core.conf as conf

import pandas as pd


# sys.path.append('C:\\Users\\Keuvin\\DOCUME~1\\Unicorn\\GIT\\UNICOR~1\\dev\\alpha\\')  #os.getcwd())
input_dir = os.path.join(os.getcwd(), 'core', 'db', 'input')


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

def prepare_dic_files(service, settings):
    input_files = collections.OrderedDict()
    db_inputs = settings.DB_INPUTS

    for serv, params in db_inputs.items():
        if serv == service:
            input_dir = params['INPUT_ROOT']
            update = params['UPDATE']
            files = params['FILES']

            for tab,to_update in update.items():
                if to_update:
                    input_files[files[tab]['fct']] = files[tab]['file']

    return input_files


def get_table_fct(table, service, settings):
    db_inputs = settings.DB_INPUTS

    fct = ''
    for serv, params in db_inputs.items():
        if serv == service:
            files = params['FILES']
            fct = files[table]['fct']

    return fct


if __name__ == '__main__':
    from sys import argv
    myargs = getopts(argv)

    settings = conf.Settings()

    # input_files = {}
    input_files = collections.OrderedDict()
    if '-s' in myargs:
        service = myargs['-s']
        input_files = prepare_dic_files(service, settings)
        print(service)

        if '-t' in myargs:
            table = myargs['-t']
            print(table)

            fct = get_table_fct(table, service, settings)
            csv_to_req(os.path.join(input_dir, service, input_files[fct]), 'POST', service, fct)

        else:
            for fct in input_files:
                csv_to_req(os.path.join(input_dir, service, input_files[fct]), 'POST', service, fct)

    else:
        pass