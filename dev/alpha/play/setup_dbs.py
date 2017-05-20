from external.userApp import call_function
import pandas as pd
import os

input_dir = os.path.join(os.getcwd(), 'play', 'input')


def csv_to_dicts(path):
    for _, series in pd.read_csv(path).iterrows():
        yield series.to_dict()


def csv_to_req(path, method_name, service_name, function_name):
    for params in csv_to_dicts(path):
        req = call_function(method_name, service_name, function_name, params)
        print(req.status_code)


# Client
csv_to_req(os.path.join(input_dir, 'client', 'clients.csv'), 'POST', 'client', 'createclient')
csv_to_req(os.path.join(input_dir, 'client', 'items.csv'), 'POST', 'client', 'createitem')
csv_to_req(os.path.join(input_dir, 'client', 'items.csv'), 'POST', 'client', 'createitem')


