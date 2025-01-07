# -*- coding: utf-8 -*-
{
    'name': "HR Dashboard",
    
    'description': """
        a dashboard for HR module that will complete the hr_custom
    """,

    'author': "MmgDev",
    'version': '0.1',
    'application': True,
    'installable': True,
    'depends': ['base', 'web', 'hr', 'hr_custom'],

    'data': [
        'views/views.xml',
    ],
    'assets': {
        'web.assets_backend': [
            'hr_dashboard/static/src/**/*',
        ],
    },
    'license': 'AGPL-3'
}
