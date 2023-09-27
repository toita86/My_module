from odoo import models, fields

class TagModel(models.Model):
    _name = "tag_model"
    _description = "Tags for the entries"

    name = fields.Char(required=True, default = "Unknown")
    #Costraint
    _sql_constraints = [
        ('check_tag_unique',
        'unique(name)',
        'The tag must be different')
        ]
