from odoo import fields, models, api
import datetime
class PropertyOffer(models.Model):
	_name = "estate.property.offer"
	_description = "Property Offer"
	partner_id = fields.Many2one('res.partner', string="Customer")
	property_id = fields.Many2one('estate.property', string="Property")
	price = fields.Float(string="Price")
	validity = fields.Integer(string="Validity")
	deadline = fields.Date(string="Deadline", compute="_compute_deadline", inverse='_inverse_deadline')
	createion_date = fields.Date(string="Create date")
	status = fields.Selection(string="Status", 
		selection=[('accepted', 'Accepted'), ('refused', 'Refused')])
	@api.depends('validity', 'createion_date')
	def _compute_deadline(self):
		for rec in self:
			if rec.createion_date and rec.validity:
				rec.deadline = rec.createion_date + datetime.timedelta(days=rec.validity)
			else:
				rec.deadline = False;
	def _inverse_deadline(self):
		for rec in self:
			rec.validity = (rec.deadline - rec.createion_date).days