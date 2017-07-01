

import requests

if __name__ == '__main__':
    response = requests.get('https://maps.googleapis.com/maps/api/geocode/json?address=157+Commercial+Street,+LONDON,+E1 6BJ')

    resp_json_payload = response.json()

    print(resp_json_payload['results'][0]['geometry']['location'])