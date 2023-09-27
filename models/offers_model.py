from datetime import datetime, timedelta
from odoo import models, fields, api


class OffersModel(models.Model):
    _name = "offers_model"
    _description = "Offers Model"

    validity_days = fields.Integer(default=7)
    partner_id = fields.Many2one('res.partner',required = False)
    property_id = fields.Many2one('test_model',required = True)
    status = fields.Selection(
        copy = False,
        selection = [
                ('accepted','Accepted'),
                ('refused', 'Refused'),
            ],
        string = 'status'
    )
    price = fields.Float()
    create_date = fields.Date(default = lambda self:(datetime.now()))
    date_deadline = fields.Date(
        compute = "_compute_deadline",
        inverse="_inverse_deadline"
    )
    def action_confirm(self):
        for record in self:
            record.status = "accepted"
        return True
    def action_refuse(self):
        for record in self:
            record.status = "refused"
        return True
    #Depends
    @api.depends('date_deadline','create_date', 'validity_days')
    def _compute_deadline(self):
        for record in self:
            create_date = record.create_date or fields.Datetime.now()
            validity_days = record.validity_days or 0
            delta = timedelta(days=validity_days)
            record.date_deadline = create_date + delta

    def _inverse_deadline(self):
        for record in self:
            if record.create_date and record.date_deadline:
                delta = record.date_deadline - record.create_date
                record.validity_days = delta.days
    #Costraint
    _sql_constraints = [
        ('check_price',
        'CHECK(price > 0)',
        'The price must be better than 0')
        ]
