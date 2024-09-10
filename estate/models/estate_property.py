from odoo import models, fields

class EstateProperty(models.Model):
    _name = 'estate.property'
    _description = 'Estate Property'

    name = fields.Char(string='Title', store=True, required=True)  # Campo 'name' de tipo Char
    description = fields.Text(string='Description', store=True)  # Campo 'description' de tipo Text
    postcode = fields.Char(string='Postcode', store=True)  # Campo 'postcode' de tipo Char
    date_availability = fields.Date(string='Available From', store=True)  # Campo 'date_availability' de tipo Date
    expected_price = fields.Float(string='Expected Price', store=True, required=True)  # Campo 'expected_price' de tipo Float (double precision)
    selling_price = fields.Float(string='Selling Price', store=True)  # Campo 'selling_price' de tipo Float (double precision)
    bedrooms = fields.Integer(string='Bedrooms', store=True)  # Campo 'bedrooms' de tipo Integer
    living_area = fields.Integer(string='Living Area (sqm)', store=True)  # Campo 'living_area' de tipo Integer
    facades = fields.Integer(string='Facades', store=True)  # Campo 'facades' de tipo Integer
    garage = fields.Boolean(string='Garage', store=True)  # Campo 'garage' de tipo Boolean
    garden = fields.Boolean(string='Garden', store=True)  # Campo 'garden' de tipo Boolean
    garden_area = fields.Integer(string='Garden Area (sqm)', store=True)  # Campo 'garden_area' de tipo Integer
    garden_orientation = fields.Char(string='Garden Orientation', store=True)  # Campo 'garden_orientation' de tipo Char

    # Los campos 'create_uid', 'create_date', 'write_uid', 'write_date' se crean automáticamente por Odoo
