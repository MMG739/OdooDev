{
    'name': 'Exco Management',
    'summary': 'Exco Management Software',
    'description': 'Exco Management Software',
    'author': 'MmgDev',
    'category': 'Tools',
    'version': '0.1',
    'depends': ['base','web'],
    'data': [
        'security/ir.model.access.csv',
        'views/assets.xml',
        'views/color_custom_views.xml',  
    ],
    'assets': {
        'web.assets_backend': [
            'exco_management/static/src/**/*',
        ],
    },
    'installable': True,
    'application': True,
    
}