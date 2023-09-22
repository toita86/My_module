from odoo import models, fields


class OffersModel(models.Model):
    _name = "offers_model"
    _description = "Offers Model"

    partner_id = fields.Many2one('res.partner',required =False)
    property_id = fields.Many2one('test_model',required = True)
    status = fields.Selection(
        copy = False,
        selection = [
                ('accepted','Accepted'),
                ('refused', 'Refused'),
            ],
        string = 'List of Choises'
    )
    price = fields.Float()
