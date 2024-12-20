from odoo import fields, models
class Property(models.Model):
	_name = 'estate.property'
	_description = "Real estate property"
	name = fields.Char(string="Name")
	description = fields.Text(string="Description")
	postcode = fields.Char(string="Postcode")
	date_availability = fields.Date(string="Available From")
	expected_price = fields.Float(string="Expected Price")
	selling_price = fields.Float(string="Selling Price")
	bedrooms = fields.Integer(string="Bedrooms")
	living_area = fields.Integer(string="Living Area")
	facades = fields.Integer(string="Facades")
	garage = fields.Boolean(string="Garage")
	garden = fields.Boolean(string="Garden")
	garden_area = fields.Integer(string="Garden Area")
	garden_orientation = fields.Selection(string="Garden Orientation", 
		selection=[('north', 'North'), ('west', 'West'), ('south', "South"), ('east', "East")], 
		help="This is your garden orientation. You can use compass to check it.")
	
class PropertyType(models.Model):
	_name= 'estate.property.type'
	name = fields.Char(string="Name", required=True)