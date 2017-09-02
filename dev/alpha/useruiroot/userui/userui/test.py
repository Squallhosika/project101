import requests

if __name__ == '__main__':
    r = requests.get('http://localhost:8003/order/orders/')
    print(r)