UNIC_ROOT = r'C:\Users\Keuvin\DOCUME~1\Unicorn\GIT\UNICOR~1\dev\alpha'

SERVICES = {
    'client': {
        'HOST': '127.0.0.1',
        'PORT': '8000',
        'ROOT': '\clientroot',
        'CMD': 'start cmd /k'
    },
    'order': {
        'HOST': '127.0.0.1',
        'PORT': '8003',
        'ROOT': 'orderroot',
        'CMD': 'start cmd /k'
    }
}

APPS = {
    'user': {
        'ROOT': '\core\app\gui',
        'GUI': 'userApp_GUI',
        'CMD': 'start cmd /k'
    },
    'client': {
        'ROOT': '\core\app\gui',
        'GUI': 'clientApp_GUI',
        'CMD': 'start cmd /k'
    }
}

DATABASES = {

}