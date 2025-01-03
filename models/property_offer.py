from odoo import fields, models, api
import datetime
from odoo.exceptions import ValidationError
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
				rec.deadline = None;
	def _inverse_deadline(self):
		for rec in self:
			if rec.deadline and rec.createion_date:
				rec.validity = (rec.deadline - rec.createion_date).days
	@api.model_create_multi
	def create(self, vals):
		for rec in vals:
			if not rec.get('createion_date'):
				rec['createion_date'] = fields.Date.today()
		return super(PropertyOffer, self).create(vals)
	@api.constrains('deadline', 'createion_date')
	def _check_validity(self):
		for rec in self:
			if rec.deadline <= rec.createion_date:
				raise ValidationError("Deadline cannot be beofore or equal to the creation date.")

