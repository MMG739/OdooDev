{
    "name": "Library Management",
    "version": "1.0",
    "author": "mmgdev",
    "category": "Tools",
    "summary": "Manage books, authors, and library members",
    "depends": ["base"],
    "data": [
        'security/ir.model.access.csv',
        "views/library_book_views.xml"
    ],
    "installable": True,
    "application": True,
}
