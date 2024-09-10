from odoo import models, fields

class EstateProperty(models.Model):
    _name = 'estate.property'
    _description = 'Estate Property'

    name = fields.Char(string='Title')  # Campo 'name' de tipo Char
    description = fields.Text(string='Description')  # Campo 'description' de tipo Text
    postcode = fields.Char(string='Postcode')  # Campo 'postcode' de tipo Char
    date_availability = fields.Date(string='Available From')  # Campo 'date_availability' de tipo Date
    expected_price = fields.Float(string='Expected Price')  # Campo 'expected_price' de tipo Float (double precision)
    selling_price = fields.Float(string='Selling Price')  # Campo 'selling_price' de tipo Float (double precision)
    bedrooms = fields.Integer(string='Bedrooms')  # Campo 'bedrooms' de tipo Integer
    living_area = fields.Integer(string='Living Area (sqm)')  # Campo 'living_area' de tipo Integer
    facades = fields.Integer(string='Facades')  # Campo 'facades' de tipo Integer
    garage = fields.Boolean(string='Garage')  # Campo 'garage' de tipo Boolean
    garden = fields.Boolean(string='Garden')  # Campo 'garden' de tipo Boolean
    garden_area = fields.Integer(string='Garden Area (sqm)')  # Campo 'garden_area' de tipo Integer
    garden_orientation = fields.Char(string='Garden Orientation')  # Campo 'garden_orientation' de tipo Char

    # Los campos 'create_uid', 'create_date', 'write_uid', 'write_date' se crean automáticamente por Odoo
