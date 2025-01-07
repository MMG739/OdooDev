from odoo import models, fields

class LibraryBook(models.Model):
    _name = 'library.book'
    _description = 'Library Book'

    name = fields.Char(string='Title', required=True)
    author = fields.Char(string='Author', required=True)
    description = fields.Text(string='Description')
    published_date = fields.Date(string='Published Date')
    isbn = fields.Char(string='ISBN')
    available_copies = fields.Integer(string='Available Copies', default=1)
