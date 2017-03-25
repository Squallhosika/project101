import os, django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "user.settings")
django.setup()
import requests
import user.user.serializers as ser

req = requests.get('http://127.0.0.1:8000/items/2')
req_json = req.json()

item_ser = ser.ItemSerializer(data=req_json)
item_ser.is_valid()
item_ser.validated_data
item_ser.save()

# data = ser.ItemSerializer.create(item_ser.validated_data)

import user.user.models as mo
mo.Item.objects.all().delete()