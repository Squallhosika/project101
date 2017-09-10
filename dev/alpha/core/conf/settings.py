import collections
import os

UNIC_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))


SERVICES = {
    'userui': {
        'HOST': '127.0.0.1',
        'PORT': '8000',
        'ROOT': r'\useruiroot',
        'CMD': r'\manage.py runserver'
    },
    'client': {
        'HOST': '127.0.0.1',
        'PORT': '8004',
        'ROOT': r'\clientroot',
        'CMD': r'\manage.py runserver'
    },
    'order': {
        'HOST': '0.0.0.0',
        'PORT': '8003',
        'ROOT': r'\orderroot',
        'CMD': r'\manage.py runserver'
    },
    'geo': {
        'HOST': '127.0.0.1',
        'PORT': '8001',
        'ROOT': r'\georoot',
        'CMD': r'\manage.py runserver'
    },
    'dqueue': {
        'HOST': '127.0.0.1',
        'PORT': '8002',
        'ROOT': r'\dqueueroot',
        'CMD': r'\manage.py runserver'
    },
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

DATABASES = {
    'UPDATE_ALL': {
        'client': True,
        'order': True,
        'dqueue': True,
    },
    'SERVICES': {
        'client': {
            'DB_ROOT': r'\core\db',
            'SERVICE_ROOT': r'\clientroot'
        },
        'order': {
            'DB_ROOT': r'\core\db',
            'SERVICE_ROOT': r'\orderroot'
        },
        'geo': {
            'DB_ROOT': r'\core\db',
            'SERVICE_ROOT': r'\georoot'
        },
        'dqueue': {
            'DB_ROOT': r'\core\db',
            'SERVICE_ROOT': r'\dqueueroot'
        }

    },
    'CMD': {
        'FLUSH_CMD': r'\manage.py flush',
        'SAVE_CMD': r'\core\db\setup_dbs.py'
    }
}

DB_INPUTS = {
    'client': {
        'INPUT_ROOT': r'\core\db\input\client',
        'UPDATE': collections.OrderedDict([
            ('client', True),
            ('menu', True),
            ('item', True),
            ('employee', True),
            ('shift', True),
            ('menuitem', True),
            ('clientmenu', True),
        ]),
        'FILES': collections.OrderedDict([
            ('client', {'fct': 'createclient', 'file': 'clients.csv'}),
            ('menu', {'fct': 'createmenu', 'file': 'menus.csv'}),
            ('item', {'fct': 'createitem', 'file': 'items.csv'}),
            ('employee', {'fct': 'createemployee', 'file': 'employees.csv'}),
            ('shift', {'fct': 'createshift', 'file': 'shifts.csv'}),
            ('menuitem', {'fct': 'additemmenu', 'file': 'rnn_menu_item.csv'}),
            ('clientmenu', {'fct': 'addmenuclient', 'file': 'rnn_client_menu.csv'}),
        ])
    },
    'order': {
        'INPUT_ROOT': r'\core\db\input\order',
        'UPDATE': collections.OrderedDict([
            ('item', True),
            ('order', True),
        ]),
        'FILES': collections.OrderedDict([
            ('item', {'fct': 'createitem', 'file': 'items.csv'}),
            ('order', {'fct': 'createorder', 'file': 'orders.csv'}),
        ])
    },
    'geo': {
        'INPUT_ROOT': r'\core\db\input\geo',
        'UPDATE': collections.OrderedDict([
            ('client', True),
            ('user', True),
        ]),
        'FILES': collections.OrderedDict([
            ('client', {'fct': 'createclient', 'file': 'clients.csv'}),
            ('user', {'fct': 'createuser', 'file': 'users.csv'}),
        ])
    },
    'dqueue': {
        'INPUT_ROOT': r'\core\db\input\dqueue',
        'UPDATE': collections.OrderedDict([
            ('queue', True),
        ]),
        'FILES': collections.OrderedDict([
            ('queue', {'fct': 'createqueue', 'file': 'queue.csv'}),
        ])
    }

}