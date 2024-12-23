from odoo import fields, models, api
class Property(models.Model):
	_name = 'estate.property'
	_description = "Real estate property"
	name = fields.Char(string="Name")
	tag_id = fields.Many2many('estate.property.tag',string="Tag")
	type_id = fields.Many2one('estate.property.type', string="Property Type")
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
	offer_ids = fields.One2many('estate.property.offer', 'property_id', string="Offers")
	sales_id = fields.Many2one('res.users', string="Salesman")
	buyer_id = fields.Many2one("res.partner", string="Buyer")
	@api.depends('living_area', 'garden_area')
	def _compute_total_area(self):
		for rec in self:
			rec.total_area = rec .living_area + rec.garden_area
	total_area = fields.Integer(string="Total Area", compute=_compute_total_area)

class PropertyType(models.Model):
	_name= 'estate.property.type'
	_description = 'Type of property'
	name = fields.Char(string="Name", required=True)
class PropertyTag(models.Model):
	_name = 'estate.property.tag'
	_description = 'Property tag'
	name = fields.Char(string="Name", required=True)