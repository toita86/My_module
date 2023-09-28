from odoo import models, fields

class TagModel(models.Model):
    _name = "tag_model"
    _description = "Tags for the entries"
    _order = "name"

    name = fields.Char(required=True, default = "Unknown")
    color = fields.Integer('color')

    #Costraint
    _sql_constraints = [
        ('check_tag_unique',
        'unique(name)',
        'The tag must be different')
        ]
