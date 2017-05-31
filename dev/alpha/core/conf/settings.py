UNIC_ROOT = r'C:\Users\Keuvin\DOCUME~1\Unicorn\GIT\UNICOR~1\dev\alpha'

SERVICES = {
    'client': {
        'HOST': '127.0.0.1',
        'PORT': '8000',
        'ROOT': r'\clientroot',
        'CMD': r'\manage.py runserver'
    },
    'order': {
        'HOST': '127.0.0.1',
        'PORT': '8003',
        'ROOT': r'\orderroot',
        'CMD': r'\manage.py runserver'
    }
}

APPS = {
    'user': {
        'ROOT': r'\core\app\gui',
        'GUI': r'\userApp_GUI.py'
    },
    'client': {
        'ROOT': r'\core\app\gui',
        'GUI': r'\clientApp_GUI.py'
    }
}