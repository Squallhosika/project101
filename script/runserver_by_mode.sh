
# admin
python3 ./georoot/manage.py runserver 0.0.0.0:8001
python3 ./orderroot/manage.py runserver 0.0.0.0:8003
python3 ./clientroot/manage.py runserver 0.0.0.0:8004

# apigateway
python3 ./georoot/manage.py runserver localhost:7001
python3 ./orderroot/manage.py runserver localhost:7003
python3 ./clientroot/manage.py runserver localhost:7004
python3 ./useruiroot/manage.py runserver 0.0.0.0:8000

# Local
python3 ./georoot/manage.py runserver localhost:8001
python3 ./orderroot/manage.py runserver localhost:8003
python3 ./clientroot/manage.py runserver localhost:8004
python3 ./useruiroot/manage.py runserver localhost:8000
