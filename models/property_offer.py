from odoo import fields, models

class PropertyOffer(models.Model):
	_name = "estate.property.offer"
	_description = "Property Offer"
	partner_id = fields.Many2one('res.partner', string="Customer")
	property_id = fields.Many2one('estate.property', string="Property")
	price = fields.Float(string="Price")
	validity = fields.Integer(string="Validity")
	deadline = fields.Date(string="Deadline")

	status = fields.Selection(string="Status", 
		selection=[('accepted', 'Accepted'), ('refused', 'Refused')])