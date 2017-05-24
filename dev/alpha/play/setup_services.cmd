#..\env\Scripts\activate.bat
set "VIRTUAL_ROOT=C:\Users\Keuvin\DOCUME~1\Unicorn\GIT\UNICOR~1\dev\alpha\"
start cmd /k %VIRTUAL_ROOT%\clientroot\manage.py runserver 127.0.0.1:8000
start cmd /k %VIRTUAL_ROOT%\orderroot\manage.py runserver 127.0.0.1:8001
#..\clientroot\manage.py runserver 127.0.0.1:8001
#..\orderroot\manage.py runserver 127.0.0.1:8002