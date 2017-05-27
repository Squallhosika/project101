from external.userApp import call_function
import pandas as pd


def csv_to_dicts(path):
    for _, series in pd.read_csv(path).iterrows():
        yield series.to_dict()


def csv_to_req(path, method_name, service_name, function_name):
    for params in csv_to_dicts(path):
        req = call_function(method_name, service_name, function_name, params)
        print(req.status_code)

